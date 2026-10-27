#!/usr/bin/env bash
# sandbox.sh — run an untrusted CTF binary in a throwaway Docker container.
# Network off by default (set CTF_NET=1 for remote-aware binaries), no host FS
# beyond the challenge dir, CPU/mem/pid capped, wall-clock timeout enforced.
#
#   scripts/ctf/sandbox.sh ./chall            # stdin from tty
#   CTF_ARGS="AAAA" scripts/ctf/sandbox.sh ./chall
#   CTF_IMAGE=ubuntu:22.04 CTF_TIMEOUT=30 scripts/ctf/sandbox.sh ./chall
#
# Inside the container the binary sits at /chal/<name> with /chal as cwd.
set -euo pipefail

[ $# -ge 1 ] || { sed -n '2,9p' "$0"; exit 2; }
BIN="$1"; shift
[ -f "$BIN" ] || { echo "no such binary: $BIN" >&2; exit 2; }
command -v docker >/dev/null || { echo "docker missing — install it or fall back to firejail" >&2; exit 2; }
docker info >/dev/null 2>&1 || { echo "docker daemon not running — start it (e.g. 'sudo dockerd &') or use firejail" >&2; exit 2; }

DIR="$(cd "$(dirname "$BIN")" && pwd)"
NAME="$(basename "$BIN")"
IMAGE="${CTF_IMAGE:-ubuntu:22.04}"
NET="${CTF_NET:-0}"
TIME="${CTF_TIMEOUT:-60}"
ARGS=("$@")

docker run --rm -i \
  --network "$([ "$NET" = 1 ] && echo bridge || echo none)" \
  --memory 512m --cpus 1 --pids-limit 256 \
  -v "$DIR":/chal:ro -w /chal \
  -e LD_PRELOAD= \
  "$IMAGE" timeout "$TIME" "./$NAME" ${ARGS[*]+"${ARGS[@]}"}
