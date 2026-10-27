#!/usr/bin/env python3
"""angr_solver_template.py — symbolic execution skeleton, three input modes.

Use when the branch tree is small enough that SMT beats reversing it by hand.
Three modes match how challenges take input: `stdin`, `argv`, or an already
`blank_state` (you set registers/stack yourself).

  python3 scripts/ctf/templates/angr_solver_template.py chall --mode stdin --find 0x401256
  python3 scripts/ctf/templates/angr_solver_template.py chall --mode argv --avoid 0x401230 --find 0x401256
  python3 scripts/ctf/templates/angr_solver_template.py chall --mode blank --entry 0x401200

Prints the concrete stdin/stdout for the first path that reaches `--find`.
Install: uv pip install angr. Run binaries through scripts/ctf/sandbox.sh when
the binary is untrusted and you are still exploring by hand.
"""
from __future__ import annotations

import argparse
import logging

import angr
import claripy

logging.getLogger("angr").setLevel("ERROR")


def build(proj, mode: str, entry: int | None):
    if mode == "stdin":
        stdin = angr.SimFileStream(name="stdin", content=claripy.BVS("stdin", 8 * 64), has_end=False)
        return proj.factory.entry_state(stdin=stdin), stdin
    if mode == "argv":
        argv = [claripy.BVS("argv", 8 * 32)]
        return proj.factory.entry_state(args=[proj.filename, *argv]), argv[0]
    state = proj.factory.blank_state(addr=entry)
    return state, None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("binary")
    ap.add_argument("--mode", choices=["stdin", "argv", "blank"], default="stdin")
    ap.add_argument("--find", type=lambda v: int(v, 0), required=True, help="success address")
    ap.add_argument("--avoid", type=lambda v: int(v, 0), action="append", default=[])
    ap.add_argument("--entry", type=lambda v: int(v, 0), help="required for --mode blank")
    ap.add_argument("--max-steps", type=int, default=2000)
    a = ap.parse_args()

    if a.mode == "blank" and not a.entry:
        ap.error("--mode blank needs --entry")

    proj = angr.Project(a.binary, auto_load_libs=False)
    state, sym = build(proj, a.mode, a.entry)
    simgr = proj.factory.simgr(state)
    simgr.explore(find=a.find, avoid=a.avoid, num_find=1, n=a.max_steps)

    if not simgr.found:
        print(f"no path to {a.find:#x} in {a.max_steps} steps")
        return 1
    found = simgr.found[0]
    print("✅ reachable")
    if sym is not None:
        print("input:", repr(found.solver.eval(sym, cast_to=bytes)))
    out = found.posix.dumps(1)
    if out:
        print("stdout:", out[:400])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
