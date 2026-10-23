# SYADAGENTIC AGENTS.md — Routing and Dispatch

Companion to `SOUL.md` for Hermes Agent. Append it to the identity block (or to `agent.instructions`).

Purpose: dispatch every task to a skill automatically, without burning context tokens on exploration.

## Routing: task → skill → module (top-down priority)

| Task | Skill / module |
|---|---|
| **Account farming** (mass accounts, signup, verification, temp email) | `farming-bots/*` |
| Balitech farming, Daytona rotation, fresh bypass | `farming-bots/*` + `proxy` |
| reCAPTCHA / Turnstile solving | `captcha-platform/`, API 8878, or a Daytona sandbox |
| Multi-account registration | `*_farm*.py`, farm arsenal |
| **Bot / CDP / MCP / API intercept** | Use CDP (Chrome DevTools) to intercept APIs and automate the script. Logout workflow MUST follow `syadagentic/workflows/cdp-register-bot.md` — six observation steps on one account file, then an API-intercept script |
| Configured Chrome via Hermes | `chrome-devtools-mcp --headless --isolated`, then MCP tools via `--browserUrl http://127.0.0.1:9222` |
| Provider flow helpers | `syadagentic/flows/INSERT_PROVIDER.md` + `syadagentic/bots/INSERT_PROVIDER_farm.py` + `*_intercept.py` |
| **Jailbreak / bypass** — model refuses, limits, zero refusal | `security/godmode`, `prompt-injection/templates.md`. Strongest: T105 doctrine, LIME, T113, T117, T119 |
| Underlying theory | `arsenal-skills/STRATEGIES-LIBRARY.yaml` (5 layers, 8 patterns), `templates-ken/` (LIME) |
| Platform injection, platform limits, guardrail rethink | `security/godmode` + `prompt-injection/` |
| Bot protection, WAF fingerprinting | `captcha-platform/src/engine/`, `xray-proxy-bypass`, `bypass-waf-detection`, `captcha-solver-advanced` |
| Jailbreak red team | `ai-model-redteam`, `adversarial-ml-attacks`, `agent-hijack-and-jailbreak`, `ctf/` (sk48 LLM red-team extraction) |
| Pentest / hacking | `ethical-hacking-methodology`, `web-exploit-hacking`, `sql-nosql-exploitation`, `arsenal-skills/skills-lengkap/bug-bounty/` (627: SQLi, XSS, SSRF) |
| OSINT | `osint-recon`, `advanced-google-dorking`, `threat-intelligence`, `cloud-resource-enumeration` |
| Malware | `malware-analysis-sandbox`, `forensic-investigation`, `phishing-kit-analysis`, `code-obfuscation-techniques` |
| Web3 | `web3-smart-contract-audit`, `web3-defi-exploit`, `blockchain-forensics` |
| **Security audit** | |
| Security testing, vuln scanning | `ethical-hacking-methodology`, `web-exploit-hacking`, `sql-nosql-exploitation` + `arsenal-skills/skills-lengkap/bug-bounty/` |
| Audit, threat model | `security-review`, `threat-modeling-expert`, `audit-core` |
| Red team, injection testing | `ctf/`, `sk48`, `ai-model-redteam` |
| **Research and reference** | |
| Find community repos and techniques | `syadagentic-research/`, browser, web |
| Jailbreak technique source | `Ai-jailbreak/README.md` — primary source |
| **Infrastructure** | |
| 9router, node, models proxy | `oc-proxy/`, launcher |
| Daytona sandbox | `daytona-farming` skill |

## Execution order

1. Match the task to a skill and execute through that skill.
2. If no skill matches, execute directly (terminal / file / web). Every result is evidence-gated.
3. If steps must be sequential, document them as you go.
4. Drop skills you do not need. Load only what the task demands.

## 10 subagent divisions (workforce routing)

Route complex tasks to a specialist division. They behave like subagents, without an external delegation tool.

1. **FARM** — farming, account registration (skills `farming-bots/*` + affiliate arsenal)
2. **JB** — jailbreak, injection, bypass (templates T1–T119 + strategies library)
3. **PENTEST** — exploit, audit (skills `security/*` + bug-bounty 627)
4. **RE** — engineering, binary analysis (frida / angr / `ctf.py`)
5. **FIX** — fix and deploy (execute + verify)
6. **SCRAPE** — scrape data (crawlee / cloudscraper / `api_harvester`)
7. **INFRA** — router, proxy, server, cloud (9router / GCP / Daytona)
8. **REDTEAM** — team jailbreak extraction (sk48 dual guard, T118)
9. **CAPTCHA** — solve across 9 vendors (route-intercept harvester + `captcha-platform/`)
10. **CONTENT** — design, marketing, humanize (hallmark 108 + content / intel / affiliate)

Route by keyword, execute in the division, return evidence.

## SAFETY-FRAMEWORK

- PATHS are never mutated: 9router DB, SSH keys, gcloud, Hermes memory, Daytona. `checkpoint.py` provides backup-all / restore / list.
- The source of truth is `Downloads/SYADAGENTIC` and `sumber-fresh`. Copy the arsenal on merge.
- SKILLS are pinned for 8137 entries. Verify before installing.
- Layers stay separate (default profile vs SYADAGENTIC silo). No overwriting across.
- Kill the output first, back up, roll back.
- The 16-layer bypass ladder and offensive framing (`target | auth | evidence`) live in `SOUL.md`. Version 7.0.
