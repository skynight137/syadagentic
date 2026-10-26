#!/usr/bin/env python3
"""checkpoint.py — Auto-backup + rollback untuk file penting (SYADAGENTIC v6.0).
Sebelum modifikasi file penting → backup .bak-TIMESTAMP + log.
Kalau rusak → rollback dari backup terakhir.
Pakai ini SEBELUM edit 9router DB, hermes config, memory, dll.
"""
import shutil, datetime, os, sys, glob

# Path resolver: satu titik. Windows pakai AppData, Unix pakai XDG/HERMES_HOME.
# Jangan hardcode "~/AppData" di daftar PROTECTED — di Linux path itu tidak ada.
HOME = os.path.expanduser("~")
if os.name == "nt":
    _ROAMING = os.path.join(HOME, "AppData", "Roaming")
    _LOCAL = os.path.join(HOME, "AppData", "Local")
else:
    _ROAMING = os.environ.get("XDG_CONFIG_HOME") or os.path.join(HOME, ".config")
    _LOCAL = os.environ.get("XDG_DATA_HOME") or os.path.join(HOME, ".local", "share")
HERMES_HOME = os.environ.get("HERMES_HOME") or os.path.join(_LOCAL, "hermes")

LOG = os.path.join(HOME, ".backup-log.txt")
PROTECTED = [
    os.path.join(_ROAMING, "9router", "db", "data.sqlite"),
    os.path.join(HERMES_HOME, "config.yaml"),
    os.path.join(HERMES_HOME, "memories", "MEMORY.md"),
    os.path.join(HERMES_HOME, "memories", "USER.md"),
    os.path.join(HOME, ".ssh", "ssh-key"),
]

def backup(path):
    path = os.path.expanduser(path)
    if not os.path.exists(path):
        return None, "tidak ada"
    ts = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    bak = f"{path}.bak-{ts}"
    shutil.copy2(path, bak)
    with open(LOG, "a") as f:
        f.write(f"{ts} BACKUP {path}\n")
    return bak, "OK"

def list_backups(path):
    path = os.path.expanduser(path)
    return sorted(glob.glob(path + ".bak-*"), key=os.path.getmtime, reverse=True)

def restore(path):
    """Restore file dari backup terakhir. Args: restore <path>"""
    baks = list_backups(path)
    if not baks:
        print(f"  NO backup utk {path}")
        return
    shutil.copy2(baks[0], path)
    with open(LOG, "a") as f:
        f.write(f"{datetime.datetime.now():%Y%m%d%H%M%S} RESTORE {path} <- {os.path.basename(baks[0])}\n")
    print(f"  RESTORED {path} dari {os.path.basename(baks[0])}")

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print("Usage: checkpoint.py [backup-all | backup <path> | restore <path> | list <path>]")
        sys.exit(0)
    cmd = args[0]
    if cmd == "backup-all":
        for p in PROTECTED:
            b, s = backup(p)
            print(f"  {s}: {os.path.basename(p)} -> {os.path.basename(b) if b else 'N/A'}")
    elif cmd == "backup" and len(args) > 1:
        b, s = backup(args[1])
        print(f"  {s}: {b or args[1]}")
    elif cmd == "restore" and len(args) > 1:
        restore(args[1])
    elif cmd == "list" and len(args) > 1:
        for b in list_backups(args[1])[:5]:
            print(f"  {os.path.basename(b)} ({os.path.getmtime(b):.0f})")