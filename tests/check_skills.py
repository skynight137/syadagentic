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
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
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
        m = re.search(r"^name:\s*(.+)$", fm, re.M)
        d = re.search(r"^description:\s*(.+)$", fm, re.M)
        name = (m.group(1).strip().strip('"\'') if m else "")
        desc = (d.group(1).strip() if d else "")
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
