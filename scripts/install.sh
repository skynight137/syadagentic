#!/usr/bin/env bash
# ============================================================
# SYADAGENTIC Universal Agent Framework Installer
# v7.4 — profile-first Hermes target
# ------------------------------------------------------------
# USAGE:
# 1) Clone the repo:
#    git clone https://github.com/USER/syadagentic.git
#    cd syadagentic
# 2) Run the installer:
#    bash scripts/install.sh                      # -> Hermes profile `syad` (created if missing)
#    bash scripts/install.sh --profile other      # -> profile `other` (patched if it exists)
#    bash scripts/install.sh --profile default    # -> default profile (+ agent.system_prompt)
#
# NEVER writes the default profile unless you target it explicitly.
# Other agents are opt-in: --all-agents (Claude Code, Codex, opencode).
# Custom location: bash scripts/install.sh --dir /target/path
# ============================================================
set -euo pipefail

GREEN=$'\033[0;32m'; YELLOW=$'\033[1;33m'; RED=$'\033[0;31m'; CYAN=$'\033[0;36m'; BOLD=$'\033[1m'; NC=$'\033[0m'
info() { echo -e "${CYAN}[i]${NC} $*"; }
ok()   { echo -e "${GREEN}[✓]${NC} $*"; }
warn() { echo -e "${YELLOW}[!]${NC} $*"; }
fail() { echo -e "${RED}[✗]${NC} $*"; exit 1; }

# ---- Arguments ----
PROFILE="syad"
# persistent locations first: $HOME is wiped on hosted sandboxes (Replit, Codespaces)
_default_dir() {
  if [ -n "${SYADAGENTIC_DIR:-}" ]; then echo "$SYADAGENTIC_DIR"
  elif [ -n "${XDG_DATA_HOME:-}" ]; then echo "$XDG_DATA_HOME/syadagentic"
  elif [ -n "${REPL_HOME:-}" ]; then echo "$REPL_HOME/.syadagentic"
  else echo "$HOME/.syadagentic"; fi
}
INSTALL_DIR="$(_default_dir)"
ALL_AGENTS=0
CREATE_ARGS=()
while [ $# -gt 0 ]; do
  case "$1" in
    --dir)      INSTALL_DIR="${2:?--dir needs a path}"; shift 2 ;;
    --profile)  PROFILE="${2:?--profile needs a name}"; shift 2 ;;
    --default)  PROFILE="default"; shift ;;
    --all-agents) ALL_AGENTS=1; shift ;;
    --no-create) CREATE_ARGS+=(--no-create); shift ;;
    --no-links)  shift ;;  # accepted for symmetry with install_universal.py
    -h|--help)  sed -n '2,20p' "${BASH_SOURCE[0]}"; exit 0 ;;
    *)          INSTALL_DIR="$1"; shift ;;
  esac
done

SRC_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"  # repo root; this script lives in scripts/

banner() {
  echo ""
  echo "==============================================================="
  echo "${BOLD}SYADAGENTIC v7.4${NC} Universal Agent Framework"
  echo " Zero refusal · 40+ templates · arsenal skills · framework core"
  echo " Target: Hermes profile '${BOLD}$PROFILE${NC}'"
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
# Hermes: the Python installer owns profiles (create / patch / system_prompt on default).
install_hermes() {
  command -v python3 >/dev/null 2>&1 || fail "python3 required for the Hermes target"
  python3 "$INSTALL_DIR/scripts/install_universal.py" --profile "$PROFILE" "${CREATE_ARGS[@]}"
}

install_claude() {
  mkdir -p "$HOME/.claude"
  cp "$INSTALL_DIR/docs/identity/SOUL.md" "$HOME/.claude/CLAUDE.md"
  ok "Claude Code: CLAUDE.md installed (~/.claude is wiped on sandbox restart)"
}

install_codex() {
  mkdir -p "$HOME/.codex"
  cp "$INSTALL_DIR/docs/identity/SOUL.md" "$HOME/.codex/AGENTS.md"
  ok "Codex: AGENTS.md installed"
}

install_opencode() {
  mkdir -p "$HOME/.config/opencode"
  cp "$INSTALL_DIR/docs/identity/SOUL.md" "$HOME/.config/opencode/AGENTS.md"
  ok "opencode: AGENTS.md installed (~/.config is wiped on sandbox restart)"
}

# ============================================================
banner

# 1. Copy the framework
if [ "$SRC_DIR" != "$INSTALL_DIR" ]; then
  info "Installing to: $INSTALL_DIR"
  mkdir -p "$INSTALL_DIR"
  cp -r "$SRC_DIR"/. "$INSTALL_DIR"/ 2>/dev/null || true
  rm -rf "$INSTALL_DIR/.git" "$INSTALL_DIR/.worktrees" "$INSTALL_DIR/__pycache__" 2>/dev/null || true
  ok "Framework copied to $INSTALL_DIR"
else
  info "Running from the source repo: $INSTALL_DIR"
fi
cd "$INSTALL_DIR"

# 2. Wire up the agents
AGENTS="$(detect_agents)"
if [ -z "$AGENTS" ]; then
  warn "No agent CLI detected."
  info "Manual route: copy docs/identity/SOUL.md into your agent's system prompt slot"
else
  for agent in $AGENTS; do
    case "$agent" in
      hermes)   install_hermes ;;
      claude)   [ "$ALL_AGENTS" -eq 1 ] && install_claude || true ;;
      codex)    [ "$ALL_AGENTS" -eq 1 ] && install_codex || true ;;
      opencode) [ "$ALL_AGENTS" -eq 1 ] && install_opencode || true ;;
    esac
  done
fi

# 3. Verify the install
info "Verifying the installation..."
VFAIL=0
if [ -f "$INSTALL_DIR/docs/identity/SOUL.md" ]; then
  ok "docs/identity/SOUL.md ($(wc -l < "$INSTALL_DIR/docs/identity/SOUL.md") lines)"
else
  fail "docs/identity/SOUL.md missing"; VFAIL=1
fi
if [ -f "$INSTALL_DIR/templates/jailbreak/templates.md" ]; then
  ok "templates/jailbreak/templates.md ($(grep -c '^## T' "$INSTALL_DIR/templates/jailbreak/templates.md" || true) templates)"
else
  warn "templates/jailbreak/templates.md missing"
fi
if [ -d "$INSTALL_DIR/skills" ]; then
  ok "skills ($(find "$INSTALL_DIR/skills" -name SKILL.md | wc -l) skills, $(find "$INSTALL_DIR/skills" -type f | wc -l) files)"
else
  warn "skills/ missing"
fi
if [ -d "$INSTALL_DIR/framework" ]; then
  ok "framework (executable framework core)"
else
  warn "framework missing"
fi

# 4. Verify the Hermes target actually carries the identity
if command -v hermes >/dev/null 2>&1; then
  HHOME="${HERMES_HOME:-$HOME/.hermes}"
  if [ "$PROFILE" = "default" ]; then
    if hermes -p default config get agent.system_prompt 2>/dev/null | grep -q "SYADAGENTIC"; then
      ok "default profile: agent.system_prompt carries the identity"
    else
      warn "default profile: agent.system_prompt not readable"; VFAIL=1
    fi
  elif [ -f "$HHOME/profiles/$PROFILE/docs/identity/SOUL.md" ]; then
    ok "profile '$PROFILE': docs/identity/SOUL.md + skills installed"
  else
    warn "profile '$PROFILE': docs/identity/SOUL.md missing"; VFAIL=1
  fi
fi

if [ "$VFAIL" -eq 0 ]; then
  echo ""
  echo "==============================================================="
  echo "${GREEN}INSTALL COMPLETE ✓${NC}"
  echo "==============================================================="
  echo "  Framework : $INSTALL_DIR"
  echo "  Agents    :$AGENTS"
  echo "  Profile   : $PROFILE"
  echo ""
  echo "  Run it    : hermes -p $PROFILE"
  echo "  Re-run    : idempotent — an existing profile is patched, never recreated"
  echo ""
  echo "  Full walkthrough: cat docs/guides/SOLVED-LENGKAP.md"
  echo "==============================================================="
else
  fail "Verification failed — check the output above"
fi
