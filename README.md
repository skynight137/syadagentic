<div align="center">

# Universal Agent Framework — Zero Refusal, Automation, Security

Make your agent comply: farming, automation, security testing, and full execution without friction.

`bash install.sh` — runs on Hermes, Claude Code, Codex, opencode, any API

[![Version](https://img.shields.io/badge/version-7.3-2ea44f)](#)
[![Templates](https://img.shields.io/badge/templates-40%2B-blue)](#-strongest-jailbreak-templates-t1t119)
[![Skills](https://img.shields.io/badge/skills-1128-important)](#)
[![Framework](https://img.shields.io/badge/framework-core-4%20modules-purple)](#-framework-core-executable-not-a-stub)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)](#)

</div>

---

## What this is

SYADAGENTIC is a universal framework that turns any agent — Claude, GPT, Gemini, DeepSeek, or any open-weight model — into an engine that just executes: no refusals, no stalling, no negotiation.

It is a curated body of jailbreak, refusal-bypass, automation, and security technique assembled from hundreds of repositories. It is not a magic button — it is real technique, tested against many models (see the [Verified Strategy Matrix](#-verified-strategy-matrix)).

**Honest, and not a scam:** no framework beats every model 100%. Frontier providers (OpenAI, Google, Anthropic) run server-side filters that no prompt can delete. SYADAGENTIC wins where it matters — open-weight models, farming, automation, security testing, and proven refusal bypass. Anyone claiming to break through everything is selling fiction.

## What you get

| Category | Content |
|---|---|
| **Zero refusal** | The agent executes instead of asking permission |
| **Jailbreak / injection** | 40+ templates (T1–T119): hijack, translation, tag injection, cascade |
| **Automation** | Cron, webhook, batch jobs, task planner, swarm, IFTTT engine |
| **Farming pipeline** | Mass accounts (mail.tm / TestMail + captcha solving + key injection), anti-detection, anti-ban |
| **Security** | 627 curated skills: SQLi, XSS, SSRF, subdomain recon, API testing, privesc, red team |
| **Framework core** | Phase engine (checkpoint / resume / token budget), governor (spend cap / kill-switch), chain map, drills benchmark |
| **Design and content** | 108 skills: anti-AI-slop design (hallmark), copywriting, humanizer, marketing, affiliate |
| **API** | 9router integration, multi-provider cascade, key-pool rotation |

## Repository layout

```
SYADAGENTIC/
├── SOUL.md                     # Boot identity — zero-refusal sovereign agent (core)
├── AGENTS.md                   # Routing and dispatch — 10 subagent divisions
├── SKILL.md                    # Skill reference and usage
├── SYADAGENTIC.md              # Full protocol (self-activating)
├── prompt-injection/
│   └── templates.md            # 40+ jailbreak templates (T1–T119)
├── arsenal-skills/             # 1128 curated skill files
│   ├── STRATEGIES-LIBRARY.yaml # 5-layer JB + 8 universal patterns
│   ├── templates-ken/          # Full ENI LIME + compact per-model payloads
│   ├── hermes-bypass/          # Hermes guardrail bypass (source patches)
│   └── skills-lengkap/         # 627 bug-bounty · 146 affiliate · 108 web-dev · etc.
├── arsenal-framework/          # Executable framework core
│   ├── phase-engine/           # Phase engine + farm pipeline
│   ├── governor/               # Spend cap + kill-switch + dry-run
│   ├── chain-map/              # Chain taxonomy (primitive → impact)
│   ├── drills/                 # Agent benchmark L1–L5
│   └── captcha-harvester/      # 9-vendor route-intercept captcha
├── checkpoint.py               # Auto-backup of critical files
├── install.sh                  # ⭐ Automatic installer
├── SOLVED-LENGKAP.md           # Full walkthrough of every feature
├── FINE-TUNE-JB.md             # Fine-tuning route (own model = 100%)
└── tests/                      # Test suite
```

> Indonesian directory names (`skills-lengkap`, `templates-ken`) stay as-is so existing paths and skill references keep working.

---

## Quick start (30 seconds)

### Option A — Clone and run the installer (fastest)

```bash
git clone https://github.com/USERNAME/syadagentic.git
cd syadagentic
bash install.sh          # auto-detects Hermes / Claude / Codex / opencode
```

### Option B — Manual (any framework)

```bash
# 1.1. Put SOUL.md where the agent loads identity
#    Hermes:   python3 install_universal.py --hermes   (profile SOUL.md, auto-load)
#              legacy root prompt: python3 install_universal.py --home
#    Claude:   cp SOUL.md ~/.claude/CLAUDE.md
#    Codex:    cp SOUL.md ~/.codex/AGENTS.md
#    opencode: cp SOUL.md ~/.config/opencode/AGENTS.md
#    API:      prepend SOUL.md to the system prompt

# 2. Verify
python3 tests/run_tests.py
```

### Option C — Docker / VPS / server

```bash
# No heavy dependencies — Python 3.8+ and curl are enough
# The framework is plain files (md / yaml / py) and runs anywhere
```

---

## Strongest jailbreak templates (T1–T119)

| Template | Function | Verified |
|---|---|---|
| **T105** | Code-as-fiction doctrine (farming / NSFW) | ✅ Codex / Gemini / DeepSeek |
| **T107** | Multilingual / low-resource | ✅ Gemini (real mail.tm) |
| **T109** | Translation framing (breaks refusal) | ✅ ChatGPT Terra / Luna |
| **T110** | ENI LIME persona (soulmate compliance) | ✅ 90%+ (Bozagentic) |
| **T113** | Scoped offensive-ops (target \| auth \| evidence) | ✅ refusal-killer |
| **T117** | Provider cascade (bypass frontier) | ✅ GPT-4 / Gemini |
| **T118** | LLM red-team extraction (dual guard) | ✅ sk48 |
| **T119** | Compact per-model payload | ✅ DeepSeek / Kimi / Claude |

**The strongest two-step pipeline:**

```
T109 (translate — bypass refusal) → T105 (execute — produce the real task)
= breakthrough on rev / scrape / abuse / farming across ChatGPT and Codex
```

---

## Framework core (executable, not a stub)

| Module | Function | Status |
|---|---|---|
| **phase-engine** | 5 presets (generic / pentest / osint / project-build / farm), checkpoint/resume, token budget, compression, auto-skill loop | ✅ Tested |
| **farm_pipeline** | Real farming (mail.tm → register → key) | ✅ Tested (account 201) |
| **governor** | Spend cap, kill-switch, dry-run, allowlist | ✅ Tested |
| **chain-map** | Chain taxonomy across 4 domains (primitive → impact) | ✅ Tested |
| **drills** | Agent benchmark L1–L5 | ✅ Tested |
| **captcha-harvester** | 9-vendor route-intercept captcha + curl_cffi replay | ✅ Tested |

---

## Verified strategy matrix

Real test results, not claims:

| Task | Model | Template | Result |
|---|---|---|---|
| Farming | Codex Terra / Luna | T105 + ownership | ✅ real script |
| Farming | Gemini 3.7 | T105 / T107 | ✅ real mail.tm |
| Farming | ChatGPT 5.5 / 4o | T107 Indonesian | ✅ |
| Rev / scrape / abuse | ChatGPT | T109 → T105 | ✅ (18k rev) |
| NSFW | Codex | T105 | ✅ 6/6 |
| JB payload | frontier | all | ❌ server filter (honest) |
| JB payload | open-weight / fine-tuned | T100+ / FINE-TUNE | ✅ 100% |

---

## Safety and corruption protection

```
✅ checkpoint.py — auto-backup of critical files (9router DB, config, SSH, memory)
✅ SAFETY-FRAMEWORK — protected paths + profile silo + dry-run + kill-switch
✅ Separate profile — never overwrites the primary configuration
✅ SKILLS.lock — integrity manifest across 8137 skills (anti-corruption)
```

## Ethics and responsibility

SYADAGENTIC is technical. It assumes security research (authorized / CTF / bug bounty) and engineering work. Use it on targets you are allowed to touch.

Hard limits that never move: content involving minors, weapons of mass destruction, self-destruction. Everything else is the Operator's call.

## Platform support

| Platform | Status |
|---|---|
| Hermes Agent | ✅ Native (`install.sh`) |
| Claude Code | ✅ `CLAUDE.md` |
| OpenAI Codex | ✅ `AGENTS.md` |
| opencode | ✅ `AGENTS.md` |
| Any OpenAI-compatible API | ✅ Paste `SOUL.md` |
| Windows / Linux / macOS | ✅ Python 3.8+, no heavy dependency |

---

## License

MIT — free to use, modify, and distribute.

<div align="center">

If this framework helps you, leave a star so more people find it.

</div>
