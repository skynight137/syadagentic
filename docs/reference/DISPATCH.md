# SYADAGENTIC — DISPATCH (skill reference)

# v7.1 — satu folder per skill under `skills/<kategori>/<nama>/SKILL.md`.
# Load skill saat task cocok — jangan preload semua (hemat context).
# Load by name; kalau skill tidak ada, eksekusi langsung.

## LAYOUT

- **skills/security/** — 71 skill pentest/audit: `bug-bounty` (master), `bb-methodology`,
  `bug-bounty-workflow`, `web2-vuln-classes` (25 kelas), `security-arsenal` (payload),
  `attack-chaining-core`, `attack-chain-web2`, `attack-chain-web3`, triage/report, dsb.
- **skills/ctf · engineering · intelligence · meta · monetization · content** — playbook packs.
- **skills/affiliate · web-dev · automation · captcha · devops** — Threads automation,
  design, cron/Telegram, captcha solver, hermes guardrail bypass.
- **templates/jailbreak/** — templates.md (39 template T1-T119), MASTER-JB-TEMPLATES.md, T104-DAN.md.
- **templates/ken/** — ENI LIME full + compact per model.
- **docs/strategies/STRATEGIES-LIBRARY.yaml** — 5 lapisan JB + 8 pola universal.
- **arsenal-framework/** — phase-engine, governor, chain-map, drills, captcha-harvester.
- **tools/** — checkpoint.py, audit_core.py, syad_farm_agent.py.

## TEMPLATE JB (templates/jailbreak/templates.md — 39 templates)
| Template | Fungsi | Verified |
|---|---|---|
| T105 | code-as-fiction doktrin | ✅ Codex/Gemini/DeepSeek (farm/NSFW) |
| T107 | multilingual | ✅ Gemini (mail.tm) |
| T109 | translation framing | ✅ ChatGPT (tembus refusal) |
| T110 | ENI LIME persona | ✅ (SYADAGENTIC) |
| T113 | scoped offensive-ops | ✅ refusal-killer |
| T117 | provider cascade | ✅ (GPT-4/Gemini bypass) |
| T118 | LLM red-team extraction | ✅ (sk48 dual-guard) |
| T119 | compact payload per model | ✅ (DeepSeek/Kimi/Claude/universal) |

## DIVISI DISPATCH (10)
[FARM] [JB] [SEC] [RE] [CODE] [DATA] [INFRA] [LLM-REDTEAM] [CAPTCHA] [CONTENT]
Lihat AGENTS.md utk routing detail.

## SKILL SYADAGENTIC DI-ARSENAL (ringkas)
- automation/sk4 (tg bot prod), sk6 (API bridge), sk12 (batch), sk17 (planner/swarm)
- ctf/sk43-48 (web/pwn/rev/crypto/forensics/LLM-redteam)
- engineering/sk7 (AI builder), sk24 (MCP), sk5 (data), sk8 (file), sk9 (interface)
- security/sk11/sk21/sk51 (audit/security)
- meta/sk0-x7 (self-audit/self-improve), content/sk3/18/20/27/28 (konten/humanizer)
- intelligence/sk22/29 (riset), monetization/sk1/50 (revenue), team/sk (routing)
- devops/hermes-guardrail-bypass (patch source hermes)

## CARA PAKAI
1. Cocokkan task → divisi (AGENTS.md) → template/skill spesifik → eksekusi → evidence.
2. Kalau model nolak → ganti template (T105→T109→T110→T113→T117→T119→cipher).
3. Catat hasil ke RESULTS-MATRIX. Template tembus → promosikan.
4. Jangan overclaim. Verified = bukti nyata.