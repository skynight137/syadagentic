---
name: bug-bounty
description: THE master bug bounty hunting skill — merged from the 69-skill arsenal (bughunter-os, webhunter-os, open-kritt, ghost-scan, etc.) + SYADAGENTIC-bugbounty v7.1 + submission review gate …
---

# Bug Bounty — Master Hunting Skill (MERGED ARSENAL)

**One skill for all bug bounty work.** Merged from: the 69-skill arsenal zip + SYADAGENTIC-bugbounty v7.1 + submission review gate.

## Triggers

- bug bounty / bugbounty / hunting / hunt target / bounty program
- recon / reconnaissance / enumerate / attack surface / subdomain / port scan
- audit smart contract / dApp / solidity / vyper / solana / move / cosmwasm / on-chain
- exploit / break / PoC / proof of concept / working exploit / chain / RCE / code injection
- injection / SQLi / SSTI / SSRF / XXE / LFI / IDOR / XSS / CSRF / JWT / OAuth / GraphQL
- vulnerability / finding / bug / triage / dedup / scope / out-of-scope
- report / write-up / submission / CVSS / CWE / severity
- HackerOne / Bugcrowd / Intigriti / Immunefi / YesWeHack / Code4rena / Sherlock / Cantina
- "find bugs", "gas cari bug" (go hunt), "hunting", "bug bounty"

## INPUT / OPERATING RULE

- **target** — asset/scope (domain, repo, contract address, dApp)
- **program** — program name + policy/scope link
- **phase** — scope | recon | analyze | verify | exploit | report | triage (auto-detect)

Authorized targets only (owned or in-scope bounty program). Working exploits over theory.
Ship fast. No fabrication — real tool output or honest blocker.

## HARD FLOW (operator lock — SYADAGENTIC 2026-07-19)

Do this order. No skip. No early chat dump.

0. **READ THE MERGED STACK** — sub-skills live beside this file in `../`, references under `references/`,
   commands under `commands/`, agents under `agents/`, tools under `tools/`. Route per phase
   via table below. Then execute.
1. **SCAN ONLY IN-SCOPE** — Lock program policy first. In-scope assets only.
   Drop OOS immediately (staging, 3rd-party host, rate-limit spam unless asked).
2. **DEEP-DIVE RECON (full explore once)** — One thorough pass, not drip-feed.
   Passive → active → targeted. Map attack surface complete before hunting loops.
3. **FIND → VERIFY + AUDIT** — Candidate is not a finding yet. Live re-test.
   Valid / reject with real proof (request/response, file:line, PoC).
   Finish ALL verifications before any operator report.
4. **VALID ONLY → HUB :9000 + SS** — Write report + evidence under
   `~/workspace/bug-hunter/public-reports/<project>/`, rebuild hub.
   SS: real browser on live target (URL bar = target) **or** rendered code SS
   when bug is not browser-visible.
5. **SUBMISSION GATE (INLINE — 14 checklist, no report leaves without passing):**
   1. VALIDATION — reproduce at least 5x, run on the latest commit + fork/mainnet-equivalent, consistent result.
   2. IMPACT — prove real impact: what is stolen/broken, who is harmed, what is the max loss, is the exploit realistic?
   3. POC — repeatable, end-to-end, no unrealistic assumptions, no privileged access (unless it is in the threat model).
   4. ROOT CAUSE — why the bug happens, why validation fails, functions involved, call flow, state transition.
   5. SCOPE — asset/commit/contract in scope, not a third-party issue.
   6. EXCLUSION — not intended behavior, governance, admin risk, centralization, missing best practice, informational, gas, style, or dead code with no impact.
   7. DUPLICATE — check GitHub Issues, PRs, audit reports, known issues, disclosures, public writeups.
   8. PATCH — make sure it is not already fixed.
   9. REPORT QUALITY — must contain: Title, Summary, Root Cause, Tech Details, Impact, PoC, Repro Steps, Evidence, Recommended Fix, References.
   10. SEVERITY — compute CVSS + CWE + likelihood + exploitability + business impact.
   11. CONFIDENCE SCORE — validity, exploitability, impact, dup-risk, report quality (0-100).
   12. FINAL DECISION — ONE output: READY TO SUBMIT / NEED MORE EVIDENCE / POSSIBLE DUPLICATE / OUT OF SCOPE / DESIGN DECISION / FALSE POSITIVE.
   13. SUBMISSION RULE — no severity inflation, no invented impact/bounty, no Critical without a PoC of real loss, no auto-submit.
   14. SELF-CRITIQUE — review as a triager: why would this be rejected? what evidence is missing? is there another intended-reading? acceptance confidence 0-100%?
   READY TO SUBMIT ONLY if all 1-14 pass.
6. **REPORT TO OPERATOR LAST** — Only after steps 1–5 done for the batch.
   **Do NOT report to SYADAGENTIC before verify + audit + hub.** Then wait for `gas`
   before any platform submit (H1/Sherlock/Cantina/Discord).

## Routing Table (phase → sub-skill)

| Phase | Type | Sub-skill / reference |
|------|------|-----------------------|
| Scope & Policy | All | `../bounty-policy-agent` · `responsible-disclosure-off-program` · `../bb-methodology` |
| Recon | Web/API | `../web2-recon` · `shodan-reconnaissance` · `subdomain-takeover` · `crawl4ai-recon` · `manual-recon-cors-leaks` · `../web2-recon` |
| Recon | SC/Web3 | `bughunter-os` (phase1) · `entry-point-analyzer` · `solana-scanner` · `on-chain-forensics` |
| Attack Surface | Web/API | `api-fuzzing-bug-bounty` · `http2-attacks` · `webhunter-os` (phases 1-3) |
| Attack Surface | SC | `attack-surface-mapper` · `entry-point-analyzer` (solidity/vyper/move/solana/ton/cosmwasm) |
| Bug Discovery | Web/API | `webhunter-os` (pattern libs) · `../web2-vuln-classes` · `xss-scanner` · `xss-html-injection` · `sql-injection-testing` · `html-injection-testing` · `code-injection-detector` · `sqlmap-database-pentesting` |
| Bug Discovery | SC | `bughunter-os` (attack patterns) · `smart-contract-audit` · `solidity-security` · `sc-vulns` · `../web3-audit` · `web3-audit/*` |
| Bug Discovery | Crypto | `crypto-ctf-solving` · `ctf-crypto` · `encrypt-decrypt` |
| Chain Analysis | All | `attack-chaining-core` · `attack-chain-web2` · `attack-chain-web3` · `variant-discovery` |
| Exploit Dev | Web/API | `exploitability-analyzer` · `exploit-to-confirm` · `vulnerability-scanner` |
| Exploit Dev | SC | `bughunter2` (PoC phase) · `evm-fuzzing-resources` · `web3-audit/rounding-zero-shortcut-exploit` |
| Verification | All | `verifier-agent` · `security-finding-triage` · `root-cause-analyzer` · `../triage-validation` |
| Evidence | All | `evidence-packager` (manifest + bundle layout) |
| Report | All | `security-finding-triage` (final) · `../report-writing` · `bug-hunter-report` |
| Pre-Submit GATE | All | **`submission-gate` · `../triage-validation` (7-Question Gate)** — MANDATORY |
| Guardrails | All | `security-research-guardrail` · `guidelines-advisor` |

## Sub-skills & Assets (from the merged toolkit)

- **13 sub-skills** in `../`: bug-bounty (master), bb-methodology, web2-recon, web2-vuln-classes, security-arsenal, web3-audit, meme-coin-audit, report-writing, triage-validation, cicd-security, credential-attack, graphql-audit, mobile-pentest
- **28 commands** in `commands/`: hunt, recon, chain, cloud-recon, bypass-403, xxsbypass, breach-check, intel, pickup, remember, godmode, genjson, wafcheck, fuzz, auth-tests, etc.
- **10 agents** in `agents/`: recon-agent, recon-ranker, validator, token-auditor, web3-auditor, chain-builder, report-writer, credential-hunter, autopilot
- **Reports**: `../report-writing` → templates per platform (H1/Bugcrowd/Intigriti/Immunefi)
  + CVSS 3.1 scoring framework + CWE mapping
- **Wordlists** in `wordlists/`, **MCP clients** in `mcp/` (Burp, Caido, HackerOne)
- **References** in `references/` (50+ files: recon, vuln classes, reporting, verification,
  grpc-web, graphql, oauth, waf-bypass, subdomain & storage probing, evidence hub, smart-contract
  bounty audit workflow)
## Severity (Immunefi scale for Web3)

🔴 Critical — direct loss of funds, no constraints · 🟠 High — loss with constraints / permanent freeze · 🟡 Medium — DoS, griefing, logic errors · 🟢 Low — minor / gas · 🔵 Info — best practice. Web: use CVSS 3.1/4.0.

## Quality bar (self-check)

- [ ] Working exploit code, not just theory
- [ ] Every step reproducible without guessing
- [ ] CVSS/severity backed by real impact argument
- [ ] Actionable remediation for the dev team
- [ ] No unverified claim presented as fact — real tool output or honest blocker
- [ ] Deep, not shallow — every claim traced to source/live endpoint/tool output
- [ ] Minimal chatter — findings direct, no preamble

## Assignment rules

- Info-only = don't draft (operator preference: "info mah gausah"). Only escalate solid Low/Medium/High/Critical against program OOS.
- Duplicate check before submission (GitHub Issues/PRs, audit reports, known issues, public writeups).
- Never over-claim severity; never fabricate impact/bounty; never auto-submit — operator `gas` required.

## Notes

- Foundry default for Web3 PoCs (`forge test`, fork with `anvil --fork-url`).
- Prefer manual verification over scanner output. Redact tokens/cookies/PII in artifacts.
- Screenshots only after confirmed; real browser on live target. Port 9000 hub only.
- Update this skill when you learn new patterns.