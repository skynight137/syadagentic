#!/usr/bin/env python3
"""scope_guard.py — decide whether a host is inside the authorized scope.

CTF/bounty work dies from one out-of-scope request. This reads a scope file that
lists in-scope entries (one per line, `#` comments, `*` wildcards) and answers
in/out. Deny-by-default: an empty or missing scope file is a failure, not an OK.

  python3 scripts/ctf/scope_guard.py --scope scope.txt --host chall.ctf.io
  python3 scripts/ctf/scope_guard.py --scope scope.txt --host evil.io --quiet; echo $?

exit 0 = in scope, 3 = out of scope, 2 = usage/error.
"""
from __future__ import annotations

import argparse
import fnmatch
import sys


def load(path: str) -> list[str]:
    entries = []
    for raw in open(path, encoding="utf-8"):
        line = raw.split("#", 1)[0].strip().lower().rstrip(".")
        if line:
            entries.append(line.lstrip("*.") if line.startswith("*.") else line)
    return entries


def in_scope(host: str, entries: list[str]) -> bool:
    host = host.strip().lower().rstrip(".")
    return any(host == e or host.endswith("." + e) or fnmatch.fnmatch(host, e) for e in entries)


def main() -> int:
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("--scope", required=True, help="scope file, one host/pattern per line")
    ap.add_argument("--host", required=True, help="host or URL to test")
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()

    host = a.host.split("//")[-1].split("/")[0].split(":")[0]
    try:
        entries = load(a.scope)
    except OSError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    if not entries:
        print(f"error: {a.scope} lists nothing — treat as out of scope", file=sys.stderr)
        return 2

    verdict = in_scope(host, entries)
    if not a.quiet:
        print(f"{'IN' if verdict else 'OUT'} SCOPE: {host} ({len(entries)} entries)")
    return 0 if verdict else 3


if __name__ == "__main__":
    sys.exit(main())
