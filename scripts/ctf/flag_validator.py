#!/usr/bin/env python3
"""flag_validator.py — reject garbage before it costs a submission.

A wrong flag on a CTF platform burns an attempt and a cooldown; a "flag" that
merely looks like text wastes minutes. This checks a candidate against the flag
format(s) of the event, then optionally submits it.

  python3 scripts/ctf/flag_validator.py --format 'CTF{...}' --flag 'CTF{abc}'
  python3 scripts/ctf/flag_validator.py --format 'picoCTF{...}' --flag X --post https://x/submit

Formats are shell-style patterns where `...` means "must be non-empty". Without
--format the generic `*{...}` family is accepted.
"""
from __future__ import annotations

import argparse
import re
import sys
import urllib.request

GENERIC = ["*{*}", "[A-Z0-9_]*{[!-~]*}", "flag{*}", "FLAG{*}"]


def to_regex(pattern: str) -> re.Pattern[str]:
    """Shell-ish pattern → anchored regex: `*` = anything, `...` = non-empty, `{ }` literal."""
    raw = re.escape(pattern).replace(r"\[", "[").replace(r"\]", "]")
    raw = raw.replace(r"\.\.\.", r"[!-~]+").replace(r"\*", ".*")
    return re.compile("^" + raw + "$")


def matches(flag: str, patterns: list[str]) -> bool:
    return any(to_regex(p).match(flag) for p in patterns)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--flag", required=True)
    ap.add_argument("--format", action="append", default=[])
    ap.add_argument("--post", help="submit URL; flag is sent as form field 'flag'")
    a = ap.parse_args()

    flag = a.flag.strip()
    patterns = a.format or GENERIC
    if any(c.isspace() for c in flag) or len(flag) < 4:
        print(f"✗ shape: whitespace/too short ({flag!r})")
        return 1
    if not matches(flag, patterns):
        print(f"✗ {flag!r} matches none of {patterns}")
        return 1
    print(f"✅ shape ok: {flag}")

    if a.post:
        data = urllib.parse.urlencode({"flag": flag}).encode()
        with urllib.request.urlopen(urllib.request.Request(a.post, data=data), timeout=20) as res:
            body = res.read(400).decode(errors="replace")
        print(f"→ HTTP {res.status}: {body.strip()[:200]}")
        return 0 if res.status < 400 else 1
    return 0


if __name__ == "__main__":
    import urllib.parse  # noqa: E402 — only needed for --post

    sys.exit(main())
