#!/usr/bin/env python3
"""skill_integrity.py — per-file SHA-256 manifest for the skill tree.

Drift is silent without a lock: a patched or half-synced SKILL.md reads exactly
like the original. This writes SKILLS.lock over skills/, and verify() fails on
any changed, added or removed file.

  python3 scripts/skill_integrity.py generate        # from a trusted tree
  python3 scripts/skill_integrity.py verify          # 0 clean, 1 drift, 2 error

`generate --sign` additionally writes SKILLS.lock.sig (Ed25519, key from
$HERMES_SIGNING_KEY PEM file); `verify` checks it when present. Both steps are
stdlib-only until signing is used, then they need `cryptography`.
"""
from __future__ import annotations

import hashlib
import os
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
TARGET = ROOT / "skills"
LOCK = ROOT / "SKILLS.lock"
SIG = ROOT / "SKILLS.lock.sig"


def digest(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def walk() -> list[pathlib.Path]:
    return sorted(p for p in TARGET.rglob("*") if p.is_file() and "__pycache__" not in p.parts)


def build() -> str:
    return "".join(f"{digest(p)}  {p.relative_to(ROOT).as_posix()}\n" for p in walk())


def generate(sign: bool) -> int:
    body = build()
    LOCK.write_text(body, encoding="utf-8")
    print(f"wrote {LOCK.relative_to(ROOT)} ({len(body.splitlines())} files)")
    if not sign:
        return 0
    key = os.environ.get("HERMES_SIGNING_KEY")
    if not key:
        print("HERMES_SIGNING_KEY not set — unsigned lock", file=sys.stderr)
        return 2
    from cryptography.hazmat.primitives import serialization

    priv = serialization.load_pem_private_key(pathlib.Path(key).read_bytes(), password=None)
    SIG.write_bytes(priv.sign(body.encode()))
    print(f"wrote {SIG.relative_to(ROOT)}")
    return 0


def verify() -> int:
    if not LOCK.exists():
        print(f"no {LOCK.name} — run generate first", file=sys.stderr)
        return 2
    body = build()
    if SIG.exists():
        from cryptography.hazmat.primitives import serialization

        key = pathlib.Path(os.environ.get("HERMES_SIGNING_KEY", ""))
        pub = serialization.load_pem_private_key(key.read_bytes(), password=None).public_key()
        pub.verify(SIG.read_bytes(), LOCK.read_bytes())
    if body == LOCK.read_text(encoding="utf-8"):
        print(f"✅ {len(body.splitlines())} files match {LOCK.name}")
        return 0
    before = dict(reversed(line.split("  ", 1)) for line in LOCK.read_text(encoding="utf-8").splitlines())
    after = dict(reversed(line.split("  ", 1)) for line in body.splitlines())
    for path in sorted(set(before) | set(after)):
        if before.get(path) != after.get(path):
            state = "changed" if path in before and path in after else ("added" if path in after else "removed")
            print(f"✗ {state}: {path}")
    return 1


if __name__ == "__main__":
    action = sys.argv[1] if len(sys.argv) > 1 else "verify"
    try:
        if action == "generate":
            sys.exit(generate("--sign" in sys.argv))
        if action == "verify":
            sys.exit(verify())
    except Exception as exc:  # noqa: BLE001 — one line beats a traceback for CLI use
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(2)
    print(__doc__)
    sys.exit(2)
