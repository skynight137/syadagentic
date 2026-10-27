#!/usr/bin/env python3
"""run.py — one entry point for an in-scope challenge.

Keeps the operator in one path: scope check → file triage → sandboxed run.
Everything here is offline except the optional scope check and the remote run.

  python3 scripts/ctf/run.py --scope scope.txt --target ./chall
  python3 scripts/ctf/run.py --scope scope.txt --target ./chall --run
  python3 scripts/ctf/run.py --scope scope.txt --target http://chall.ctf.io:1337

Triage prints `file`, `checksec`, embedded strings hits and the interpreter.
`--run` executes a local binary through scripts/ctf/sandbox.sh.
"""
from __future__ import annotations

import argparse
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent


def sh(cmd: list[str]) -> str:
    try:
        return subprocess.run(cmd, capture_output=True, text=True, timeout=120).stdout.strip()
    except (OSError, subprocess.SubprocessError) as exc:
        return f"({cmd[0]} unavailable: {exc.__class__.__name__})"


def triage(path: pathlib.Path) -> None:
    print(sh(["file", "-b", str(path)]))
    print(sh(["checksec", "--file", str(path)]) or "(install pwntools for checksec)")
    strings = sh(["strings", "-n", "6", str(path)]).splitlines()
    hits = [s for s in strings if any(k in s for k in ("flag", "CTF{", "/bin/sh", "system", "gets", "printf"))]
    for line in hits[:15]:
        print(f"  str: {line[:120]}")
    print(f"({len(strings)} strings, {len(hits)} interesting)")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--scope", required=True)
    ap.add_argument("--target", required=True, help="local path or URL")
    ap.add_argument("--run", action="store_true", help="execute a local binary in the sandbox")
    a = ap.parse_args()

    host = a.target.split("//")[-1].split("/")[0].split(":")[0]
    local = pathlib.Path(a.target)
    if not local.exists():
        rc = subprocess.run(
            [sys.executable, str(HERE / "scope_guard.py"), "--scope", a.scope, "--host", host]
        ).returncode
        if rc != 0:
            print("⛔ out of scope — stop here")
            return rc
        print(f"remote target in scope: {a.target} (connect with nc/pwntools)")
        return 0

    if not local.is_file():
        print(f"not a file: {local}", file=sys.stderr)
        return 2
    triage(local)
    if a.run:
        print("\n=== sandboxed run ===")
        return subprocess.run(["bash", str(HERE / "sandbox.sh"), str(local)]).returncode
    print("\nadd --run to execute it, or use scripts/ctf/templates/pwn_template.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
