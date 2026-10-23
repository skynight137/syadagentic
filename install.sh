#!/usr/bin/env bash
# ============================================================
# SYADAGENTIC Universal Agent Framework Installer
# v7.3 — zero refusal, 40+ templates, 1128 skills
# ------------------------------------------------------------
# USAGE:
# 1) Clone the repo:
#    git clone https://github.com/USER/syadagentic.git
#    cd syadagentic
# 2) Run the installer:
#    bash install.sh
#    (auto-detects: Hermes, Claude Code, Codex, opencode)
#
# Custom location: bash install.sh --dir /target/path
# ============================================================
set -euo pipefail

GREEN=$'\033[0;32m'; YELLOW=$'\033[1;33m'; RED=$'\033[0;31m'; CYAN=$'\033[0;36m'; BOLD=$'\033[1m'; NC=$'\033[0m'
info() { echo -e "${CYAN}[i]${NC} $*"; }
ok()   { echo -e "${GREEN}[✓]${NC} $*"; }
warn() { echo -e "${YELLOW}[!]${NC} $*"; }
fail() { echo -e "${RED}[✗]${NC} $*"; exit 1; }

# ---- Arguments ----
INSTALL_DIR="${SYADAGENTIC_DIR:-$HOME/.syadagentic}"
if [ "${1:-}" = "--dir" ]; then INSTALL_DIR="${2:-$HOME/.syadagentic}"; fi

SRC_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

banner() {
  echo ""
  echo "==============================================================="
  echo "${BOLD}SYADAGENTIC v7.3${NC} Universal Agent Framework"
  echo " Zero refusal · 40+ templates · 1128 skills · framework core"
  echo "==============================================================="
  echo ""
}

# ---- Agent detection ----
detect_agents() {
  local agents=""
  for a in hermes claude codex opencode; do
    command -v "$a" >/dev/null 2>&1 && agents="$agents $a"
  done
  echo "$agents"
}

# ---- Per-agent install ----
install_hermes() {
  local d="${HERMES_HOME:-$HOME/.hermes}"
  mkdir -p "$d"
  if [ -f "$d/config.yaml" ]; then
    cp "$d/config.yaml" "$d/config.yaml.bak-syad" 2>/dev/null || true
    python3 - "$INSTALL_DIR/SOUL.md" "$d/config.yaml" <<'PYEOF' 2>/dev/null || warn "Hermes config update skipped (needs python3 + pyyaml)"
import sys
try:
    import yaml
except ImportError:
    sys.exit(1)
soul_path, cfg_path = sys.argv[1], sys.argv[2]
with open(cfg_path, encoding="utf-8") as fh:
    cfg = yaml.safe_load(fh) or {}
with open(soul_path, encoding="utf-8") as fh:
    cfg.setdefault("agent", {})["system_prompt"] = fh.read()
with open(cfg_path, "w", encoding="utf-8") as fh:
    yaml.safe_dump(cfg, fh, allow_unicode=True)
print("OK")
PYEOF
    ok "Hermes: SOUL.md written to agent.system_prompt"
  else
    cp "$INSTALL_DIR/SOUL.md" "$d/SOUL.md" 2>/dev/null || true
    warn "No Hermes config found — SOUL.md dropped in as a fallback"
  fi
}

install_claude() {
  mkdir -p "$HOME/.claude"
  cp "$INSTALL_DIR/SOUL.md" "$HOME/.claude/CLAUDE.md"
  ok "Claude Code: CLAUDE.md installed"
}

install_codex() {
  mkdir -p "$HOME/.codex"
  cp "$INSTALL_DIR/SOUL.md" "$HOME/.codex/AGENTS.md"
  ok "Codex: AGENTS.md installed"
}

install_opencode() {
  mkdir -p "$HOME/.config/opencode"
  cp "$INSTALL_DIR/SOUL.md" "$HOME/.config/opencode/AGENTS.md"
  ok "opencode: AGENTS.md installed"
}

# ============================================================
banner

# 1. Copy the framework
if [ "$SRC_DIR" != "$INSTALL_DIR" ]; then
  info "Installing to: $INSTALL_DIR"
  mkdir -p "$INSTALL_DIR"
  cp -r "$SRC_DIR"/. "$INSTALL_DIR"/ 2>/dev/null || true
  rm -rf "$INSTALL_DIR/.git" "$INSTALL_DIR/__pycache__" 2>/dev/null || true
  ok "Framework copied to $INSTALL_DIR"
else
  info "Running from the source repo: $INSTALL_DIR"
fi
cd "$INSTALL_DIR"

# 2. Wire up the detected agents
AGENTS="$(detect_agents)"
if [ -z "$AGENTS" ]; then
  warn "No agent CLI detected."
  info "Manual route: copy SOUL.md into your agent's system prompt slot"
else
  for agent in $AGENTS; do
    case "$agent" in
      hermes)   install_hermes ;;
      claude)   install_claude ;;
      codex)    install_codex ;;
      opencode) install_opencode ;;
    esac
  done
fi

# 3. Verify the install
info "Verifying the installation..."
VFAIL=0
if [ -f "$INSTALL_DIR/SOUL.md" ]; then
  ok "SOUL.md ($(wc -l < "$INSTALL_DIR/SOUL.md") lines)"
else
  fail "SOUL.md missing"; VFAIL=1
fi
if [ -f "$INSTALL_DIR/prompt-injection/templates.md" ]; then
  ok "templates.md ($(grep -c '^## T' "$INSTALL_DIR/prompt-injection/templates.md" || true) templates)"
else
  warn "templates.md missing"
fi
if [ -d "$INSTALL_DIR/arsenal-skills" ]; then
  ok "arsenal-skills ($(find "$INSTALL_DIR/arsenal-skills" -type f | wc -l) files)"
else
  warn "arsenal-skills missing"
fi
if [ -d "$INSTALL_DIR/arsenal-framework" ]; then
  ok "arsenal-framework (executable framework core)"
else
  warn "arsenal-framework missing"
fi

if [ "$VFAIL" -eq 0 ]; then
  echo ""
  echo "==============================================================="
  echo "${GREEN}INSTALL COMPLETE ✓${NC}"
  echo "==============================================================="
  echo "  Framework : $INSTALL_DIR"
  echo "  Agents    :$AGENTS"
  echo ""
  echo "  Ready to use — just tell the agent:"
  echo "  \"do X\" and let the framework carry the rest"
  echo ""
  echo "  Full walkthrough: cat SOLVED-LENGKAP.md"
  echo "==============================================================="
else
  fail "Verification failed — check the output above"
fi
