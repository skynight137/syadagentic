#!/usr/bin/env python3
"""install_universal.py — install SYADAGENTIC identity into a Hermes *profile*.

Profile-first and idempotent:
  1. profile missing  -> `hermes profile create <name> --clone` (working config + .env)
  2. profile present  -> patch only, nothing is recreated
  3. target `default` -> the same files PLUS `agent.system_prompt` in config.yaml

Payload per target: identity (SOUL.md + AGENTS.md), full repo mirror under
references/syadagentic/, and the arsenal skills. A durable launcher alias goes to
the persistent bin dir ($XDG_BIN_HOME, else $REPL_HOME/.local/bin, else
~/.local/bin) — $HOME is wiped on hosted sandboxes (Replit, Codespaces), $HERMES_HOME
survives.

Other targets (opt-in):
  opencode     ~/.config/opencode/AGENTS.md (global) + project root AGENTS.md
  Claude Code  ~/.claude/CLAUDE.md
  Cursor       ~/.cursorrules (global) + project AGENTS.md / CLAUDE.md

Usage:
  python3 install_universal.py                       # profile `syad`
  python3 install_universal.py --profile other       # profile `other`
  python3 install_universal.py --profile default     # default profile + system_prompt
  python3 install_universal.py --no-create           # fail instead of creating
  python3 install_universal.py --all-agents          # + opencode / Claude / Cursor
  python3 install_universal.py /path/project         # + files into that project root
"""
import argparse
import os
import pathlib
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent
SOURCE = ROOT / "SOUL.md"
SOURCE_SHORT = ROOT / "SYADAGENTIC-SHORT.md"
ROUTING = ROOT / "AGENTS.md"
HOME = pathlib.Path.home()
IGNORE = shutil.ignore_patterns(".git", ".worktrees", "__pycache__", "*.guardrail-bak")

# repo path -> category/name inside the target's skills dir
PROFILE_SKILLS = [
    ("arsenal-skills/hermes-bypass", "devops/hermes-guardrail-bypass"),
    ("arsenal-skills/security", "security/web-exploit-test"),
    ("arsenal-skills/automation", "automation/arsenal-automation"),
    ("arsenal-skills/captcha", "captcha/web-bot-protection"),
]

# arsenal category -> skills category (existing names are kept, never overwritten)
SKILL_CATEGORY = {
    "bug-bounty": "security", "security": "security", "ctf": "ctf", "web-dev": "web-dev",
    "affiliate": "affiliate", "content": "content", "intelligence": "osint",
    "automation": "automation", "captcha": "captcha", "devops": "devops",
    "engineering": "engineering", "meta": "meta", "monetization": "monetization",
    "team": "team", "hermes-bypass": "devops",
}


def banner(title: str) -> None:
    print(f"\n=== {title} ===")


def install_file(dst: pathlib.Path, copy: bool = True, src=None) -> bool:
    src = src or SOURCE
    try:
        dst.parent.mkdir(parents=True, exist_ok=True)
        if copy:
            shutil.copy(src, dst)
        print(f"  ✅ {dst}")
        return True
    except Exception as exc:
        print(f"  ❌ {dst}: {exc}")
        return False


def _hermes_home() -> pathlib.Path:
    return pathlib.Path(os.environ.get("HERMES_HOME") or HOME / ".hermes")


def _hermes_cli():
    return shutil.which("hermes")


def identity_text() -> str:
    """SOUL.md + the AGENTS.md dispatch table, as one identity block."""
    text = SOURCE.read_text(encoding="utf-8")
    if ROUTING.exists():
        text += "\n\n---\n\n" + ROUTING.read_text(encoding="utf-8")
    return text


def alias_dir() -> pathlib.Path:
    """Persistent bin dir first: $HOME is wiped on Replit/Codespaces."""
    xdg = os.environ.get("XDG_BIN_HOME")
    if xdg:
        return pathlib.Path(xdg)
    repl = os.environ.get("REPL_HOME")
    if repl:
        return pathlib.Path(repl) / ".local" / "bin"
    return HOME / ".local" / "bin"


def write_alias(name: str) -> None:
    d = alias_dir()
    wrapper = d / name
    try:
        d.mkdir(parents=True, exist_ok=True)
        cli = _hermes_cli() or "hermes"
        wrapper.write_text(f'#!/bin/sh\nexec "{cli}" -p {name} "$@"\n', encoding="utf-8")
        wrapper.chmod(0o755)
        print(f"  ✅ alias {wrapper}")
        if str(d) not in os.environ.get("PATH", "").split(":"):
            print(f'  ⚠ add to PATH: export PATH="{d}:$PATH"')
    except Exception as exc:
        print(f"  ❌ alias {wrapper}: {exc}")


def ensure_profile(name: str, create: bool, clone: bool, alias: bool):
    """Resolve the target dir, creating the profile when missing. `default` needs no create."""
    home = _hermes_home()
    if name == "default":
        banner("HERMES PROFILE: default (files + agent.system_prompt)")
        return home
    prof = home / "profiles" / name
    banner(f"HERMES PROFILE: {name}")
    if prof.exists():
        print(f"  ℹ  profile exists — patch only ({prof})")
        return prof
    if not create:
        print(f"  ❌ profile '{name}' missing and --no-create was given")
        return None
    cli = _hermes_cli()
    if not cli:
        prof.mkdir(parents=True, exist_ok=True)
        print("  ⚠ hermes CLI not on PATH — bare dir created; finish with: "
              f"hermes profile create {name}")
        return prof
    cmd = [cli, "profile", "create", name, "--no-alias"]
    if clone:
        cmd.append("--clone")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        print(f"  ✅ created {prof} ({'cloned from the active profile' if clone else 'bare'})")
    else:
        prof.mkdir(parents=True, exist_ok=True)
        err = (res.stderr or res.stdout).strip().splitlines()
        print(f"  ⚠ profile create failed ({err[-1] if err else 'unknown error'}) "
              "— bare dir created instead")
    if alias:
        write_alias(name)
    return prof


def ensure_alias(name: str) -> None:
    """Re-create a wiped alias on a profile that already exists."""
    if not (alias_dir() / name).exists():
        write_alias(name)


def link_skill(src: pathlib.Path, dst: pathlib.Path) -> bool:
    """Symlink (stays in sync with the mirror); copy on filesystems without links."""
    if dst.exists() or dst.is_symlink():
        return True
    try:
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.symlink_to(src.resolve(), target_is_directory=True)
        return True
    except OSError:
        try:
            shutil.copytree(src, dst, dirs_exist_ok=True)
            return True
        except Exception as exc:
            print(f"  ❌ {dst}: {exc}")
            return False


def install_payload(prof: pathlib.Path) -> None:
    """Identity + repo mirror + arsenal skills into one profile dir."""
    try:
        (prof / "SOUL.md").write_text(identity_text(), encoding="utf-8")
        print(f"  ✅ {prof / 'SOUL.md'} (SOUL.md + AGENTS.md)")
    except Exception as exc:
        print(f"  ❌ {prof / 'SOUL.md'}: {exc}")
    refs = prof / "references" / "syadagentic"
    try:  # full repo mirror so SOUL.md's relative links (arsenal-*, prompt-injection) resolve
        shutil.copytree(ROOT, refs, dirs_exist_ok=True, ignore=IGNORE)
        print(f"  ✅ {refs}/ (repo mirror)")
    except Exception as exc:
        print(f"  ❌ {refs}: {exc}")
    for rel, sub in PROFILE_SKILLS:
        src = ROOT / rel
        if not src.exists():
            print(f"  ❌ {rel} missing in repo")
            continue
        link_skill(src, prof / "skills" / sub)
    made = 0  # register the rest of the arsenal, skipping whatever is already in place
    for skill_md in sorted(ROOT.glob("arsenal-skills/**/SKILL.md")):
        src = skill_md.parent
        parts = src.relative_to(ROOT).parts
        if parts[1] == "skills-lengkap" and len(parts) >= 4:
            category, name = SKILL_CATEGORY.get(parts[2], parts[2]), parts[-1]
        elif len(parts) == 3:
            category, name = SKILL_CATEGORY.get(parts[1], parts[1]), parts[-1]
        else:
            continue
        dst = prof / "skills" / category / name
        fresh = not (dst.exists() or dst.is_symlink())
        if link_skill(src, dst) and fresh:
            made += 1
    print(f"  ✅ arsenal skills: {made} added (already-present skills kept)")
    print("  ℹ  no tirith key needed: security.tirith_* was dropped in Hermes config v50")


PROMPT_KEY = "system_prompt"


def _write_prompt_yaml(cfg: pathlib.Path, text: str) -> None:
    """Replace agent.system_prompt in place with a block scalar; comments stay untouched.

    (`hermes config set` stores one escaped line, which leaves literal \\n in the prompt.)
    """
    lines = cfg.read_text(encoding="utf-8").splitlines()
    block = [f"  {PROMPT_KEY}: |"] + [
        ("    " + line) if line.strip() else "" for line in text.rstrip("\n").splitlines()
    ]
    try:
        anchor = next(i for i, line in enumerate(lines) if line.rstrip() == "agent:")
    except StopIteration:  # no agent: section at all
        cfg.write_text("\n".join(lines + ["", "agent:"] + block) + "\n", encoding="utf-8")
        return
    block_end = len(lines)
    for i in range(anchor + 1, len(lines)):
        line = lines[i]
        if line.strip() and not line.startswith((" ", "\t")):
            block_end = i
            break
    key = next((i for i in range(anchor + 1, block_end)
                if lines[i].lstrip().startswith(PROMPT_KEY + ":")), None)
    if key is None:  # key absent: put it first in the section
        lines[anchor + 1:anchor + 1] = block
    else:  # consume the old (possibly multi-line) value
        end = key + 1
        while end < block_end and (not lines[end].strip() or lines[end].startswith("   ")):
            end += 1
        lines[key:end] = block
    cfg.write_text("\n".join(lines) + "\n", encoding="utf-8")


def apply_system_prompt() -> None:
    """`default` only: identity into agent.system_prompt, the layer that profile reads."""
    cfg = _hermes_home() / "config.yaml"
    if not cfg.exists():
        print(f"  ❌ {cfg} not found — nothing to patch")
        return
    backup = cfg.with_name(cfg.name + ".bak-syad")
    shutil.copy(cfg, backup)
    print(f"  ✅ backup {backup}")
    try:
        _write_prompt_yaml(cfg, identity_text())
    except Exception as exc:
        print(f"  ❌ config write failed: {exc}")
        shutil.copy(backup, cfg)
        print("  ↩ config restored from backup")
        return
    cli = _hermes_cli()
    if cli and "SYADAGENTIC" not in subprocess.run(
            [cli, "-p", "default", "config", "get", f"agent.{PROMPT_KEY}"],
            capture_output=True, text=True).stdout:
        print("  ❌ verification failed: agent.system_prompt does not read back")
        shutil.copy(backup, cfg)
        print("  ↩ config restored from backup")
        return
    print(f"  ✅ agent.{PROMPT_KEY} written to {cfg} (verified by config get)")


def opencode_setup() -> None:
    banner("OPENCODE")
    install_file(HOME / ".config" / "opencode" / "AGENTS.md")
    install_file(HOME / ".config" / "opencode" / "GLOBAL_RULES.md", copy=False)


def claude_setup() -> None:
    banner("CLAUDE CODE")
    install_file(HOME / ".claude" / "CLAUDE.md")
    install_file(HOME / ".claude" / "CLAUDE.local.md")


def cursor_setup() -> None:
    banner("CURSOR")
    install_file(HOME / ".cursorrules")


def project_setup(root: pathlib.Path) -> None:
    banner(f"PROJECT ROOT: {root}")
    for name in ("AGENTS.md", "CLAUDE.md"):
        install_file(root / name)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("root", nargs="?", default=None, help="project root for AGENTS.md / CLAUDE.md")
    ap.add_argument("--hermes", action="store_true", help="Hermes only (already the default)")
    ap.add_argument("--all-agents", action="store_true", help="also opencode / Claude / Cursor")
    ap.add_argument("--home", action="store_true", help="same as --profile default (legacy)")
    ap.add_argument("--profile", default="syad", help="target Hermes profile (default: syad)")
    ap.add_argument("--no-create", action="store_true", help="fail if the profile does not exist")
    ap.add_argument("--bare", action="store_true", help="create without cloning the active profile")
    ap.add_argument("--no-alias", action="store_true", help="skip the launcher alias")
    args = ap.parse_args()

    for needed in (SOURCE, ROUTING):
        if not needed.exists():
            print(f"❌ {needed.name} missing next to this script")
            return 1

    name = "default" if args.home else args.profile
    print(f"SOURCE {SOURCE} ({SOURCE.stat().st_size} bytes) · TARGET profile: {name}")

    prof = ensure_profile(name, not args.no_create, not args.bare, not args.no_alias)
    if prof is None:
        return 1
    install_payload(prof)
    if name == "default":
        apply_system_prompt()
    elif not args.no_alias:
        ensure_alias(name)

    if args.all_agents and not args.hermes:
        print("\n  note: ~/.claude, ~/.config, ~/.cursorrules are wiped on sandbox restart")
        opencode_setup()
        claude_setup()
        cursor_setup()
        if SOURCE_SHORT.exists():  # variant for frontier models with big context
            install_file(HOME / ".config" / "opencode" / "SYADAGENTIC-SHORT.md", src=SOURCE_SHORT)
            install_file(HOME / ".claude" / "SYADAGENTIC-SHORT.md", src=SOURCE_SHORT)
    if args.root:
        project_setup(pathlib.Path(args.root))

    print(f"\nDONE — {name}. Activate: hermes -p {name}"
          + ("" if name == "default" else f"  (gateway: profile_routes -> profile: {name})"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
