#!/usr/bin/env python3
"""check_identity_refs.py — the identity docs must only reference paths that exist.

`docs/identity/SOUL.md` and `AGENTS.md` are the system prompt: every backticked
path in them is an instruction the agent will try to open. Renaming a folder and
forgetting one reference produces a silent "no such file" at run time, so CI
fails instead.

Skipped on purpose: placeholders (`<category>`, `INSERT_PROVIDER`), prose tokens
without a slash, and skill *names* (matched against skills/<cat>/<name>/SKILL.md).
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = [ROOT / "docs/identity/SOUL.md", ROOT / "AGENTS.md"]
PLACEHOLDER = re.compile(r"[<>]|INSERT_")
EXTERNAL = ("Downloads/", "~", "/")  # outside the repo: not checked
errors: list[str] = []

skills = {p.parent.name for p in (ROOT / "skills").rglob("SKILL.md")}
categories = {p.parent.name for p in (ROOT / "skills").glob("*/SKILL.md")} | {
    p.name for p in (ROOT / "skills").iterdir() if p.is_dir()
}

for doc in DOCS:
    if not doc.exists():
        errors.append(f"{doc.relative_to(ROOT)}: missing")
        continue
    for match in re.finditer(r"`([A-Za-z0-9_./*-]+)`", doc.read_text(encoding="utf-8")):
        token = match.group(1).strip()
        if PLACEHOLDER.search(token) or "/" not in token or token.startswith(EXTERNAL):
            continue
        target = token.rstrip("/")
        if (
            list(ROOT.glob(target))
            or target.split("/")[-1] in skills
            or target in skills
            or target == f"skills/{target}"
            or target in categories
        ):
            continue
        errors.append(f"{doc.relative_to(ROOT)}: dead reference `{token}`")

if errors:
    print(f"✗ {len(errors)} dead identity reference(s):")
    for err in errors:
        print(f"  {err}")
    sys.exit(1)
print(f"✅ identity refs resolve ({len(DOCS)} docs)")
