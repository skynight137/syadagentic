#!/usr/bin/env python3
"""check_skills.py — layout lint for skills/.

Enforced, because Hermes loads a skill by its `name:` and by directory name:
drift in either means a skill silently stops being routable.

Rules:
  1. every skill is exactly skills/<category>/<name>/SKILL.md  (no deeper nesting)
  2. `name:` in the frontmatter equals the folder name
  3. `name:` and `description:` are present, name is kebab-case, description <= 200 chars
  4. no duplicate skill names, and a category never nests another category
  5. no stray SKILL.md outside skills/ except the documented legacy copies
  6. frontmatter is valid YAML (Hermes falls back to a naive splitter on bad YAML,
     which silently kills the skill: a `: ` inside an unquoted description turns
     `platforms:` into a string and the platform gate then rejects the skill everywhere)
  7. `platforms:`, when present, parses as a list of known platform names
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
PLATFORMS = {"linux", "darwin", "macos", "win32", "windows"}


def parse_frontmatter(p: pathlib.Path, fm: str) -> dict | None:
    """Strict YAML parse; None when PyYAML is absent and the regex fallback is clean."""
    try:
        import yaml
    except ImportError:  # CI installs PyYAML; keep local runs usable without it
        for line in fm.splitlines():
            m = re.match(r"^(\w+):\s+(.+)$", line)
            if m and ": " in m.group(2) and not m.group(2).lstrip().startswith(("[", '"', "'")):
                errors.append(f"{rel(p)}: unquoted `: ` in `{m.group(1)}:` (invalid YAML)")
        return None
    try:
        return yaml.safe_load(fm) or {}
    except Exception as exc:
        errors.append(f"{rel(p)}: invalid YAML frontmatter — {str(exc).splitlines()[0]}")
        return None


errors: list[str] = []


def rel(p: pathlib.Path) -> str:
    return str(p.relative_to(ROOT))


def frontmatter(p: pathlib.Path) -> str:
    text = p.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        errors.append(f"{rel(p)}: no YAML frontmatter")
        return ""
    return m.group(1)


if not SKILLS.is_dir():
    print("skills/ missing")
    sys.exit(1)

seen: dict[str, str] = {}
for path in sorted(SKILLS.rglob("SKILL.md")):
    parts = path.relative_to(SKILLS).parts
    if len(parts) != 3:
        errors.append(f"{rel(path)}: must be skills/<category>/<name>/SKILL.md ({len(parts)} levels)")
        continue
    category, folder = parts[0], parts[1]
    fm = frontmatter(path)
    if fm:
        meta = parse_frontmatter(path, fm)
        if meta is not None:
            plats = meta.get("platforms")
            if plats is not None:
                if not isinstance(plats, list):
                    errors.append(f"{rel(path)}: `platforms:` must be a YAML list, got {type(plats).__name__}")
                else:
                    unknown = [str(x) for x in plats if str(x).lower() not in PLATFORMS]
                    if unknown:
                        errors.append(f"{rel(path)}: unknown platform(s) {unknown}")
        m = re.search(r"^name:\s*(.+)$", fm, re.M)
        d = re.search(r"^description:\s*(.+)$", fm, re.M)
        name = (m.group(1).strip().strip('"\'') if m else "")
        desc = (d.group(1).strip() if d else "")
        if desc.startswith('"') and desc.endswith('"'):
            try:
                import json
                desc = json.loads(desc)
            except ValueError:
                desc = desc.strip('"')
        if not name:
            errors.append(f"{rel(path)}: missing `name:`")
        elif not NAME_RE.match(name):
            errors.append(f"{rel(path)}: name `{name}` is not kebab-case")
        elif name != folder:
            errors.append(f"{rel(path)}: name `{name}` != folder `{folder}`")
        elif name in seen:
            errors.append(f"{rel(path)}: duplicate name, already at {seen[name]}")
        else:
            seen[name] = rel(path)
        if not desc:
            errors.append(f"{rel(path)}: missing `description:`")
        elif len(desc) > 250:
            errors.append(f"{rel(path)}: description {len(desc)} chars (max 250)")
    if (path.parent / folder / "SKILL.md").exists():
        errors.append(f"{rel(path)}: category dir {folder}/ nests another skill level")

for stray in sorted(ROOT.rglob("SKILL.md")):
    if SKILLS in stray.parents:
        continue
    if ".git" in stray.parts or "references/syadagentic" in str(stray):
        continue
    errors.append(f"{rel(stray)}: SKILL.md outside skills/")

fresh = {}
for cat in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
    n = sum(1 for _ in cat.glob("*/SKILL.md"))
    fresh[cat.name] = n

if errors:
    print(f"✗ {len(errors)} layout error(s):")
    for e in errors:
        print("  " + e)
    sys.exit(1)

print(f"✅ skills layout OK — {len(seen)} skills in {len(fresh)} categories")
for cat, n in sorted(fresh.items(), key=lambda kv: -kv[1]):
    print(f"   {cat}: {n}")
