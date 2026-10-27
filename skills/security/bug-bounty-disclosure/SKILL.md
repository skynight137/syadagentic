---
name: bug-bounty-disclosure
description: "End-to-end skill for authorized/good-faith bug bounty and coordinated vulnerability disclosure to the developer or project owner — for ALL bug types (web, API, infra, mobile, cloud, smart contract/web3, agent/LLM), crypto and non-crypto …"
---

# Bug Bounty & Coordinated Disclosure

Skill to tidy up the whole flow from **finding → verification → contact discovery → report to the dev via email → fix coordination**. General purpose: crypto and non-crypto, targets with an official program or without one. The focus is producing reports that are **valid, reproducible, and accepted by the dev** — not AI slop that gets ignored.

## ⚠️ Good-faith baseline (read first, keep it short)

This skill is for **good-faith security research + coordinated disclosure**. Reporting a vulnerability to the project owner is legitimate and ethical **whether or not they run an official program** — that is exactly the point.

What must hold: **the testing basis must be legitimate.** The bug was found through legit means:
- Your own systems/infra, your own accounts, or a testnet.
- Reviewing open-source code / public artifacts (repo, package, image).
- On-chain smart contract analysis (public bytecode/source).
- A target that runs a bug bounty program / VDP / `security.txt` that invites reports.
- Written permission from the owner.

Do not use this skill to **justify intrusion without permission** into a third party's production system (credential phishing, breaking into access you are not entitled to, continuing to drill deeper after gaining access). If you are unsure whether a testing step is legitimate: **stop, do not escalate access**, and report only what you found through legit means. For crypto bugs with live and exploitable funds: **do not exploit, do not publish yet** — private disclosure to the team is the correct move.

## Core principles

A finding is worth sending to the dev if: **(1) it is valid and reproducible with a PoC**, **(2) the impact is real**, **(3) it goes to the right party through the right channel**, with **(4) a good-faith tone, no threats/ransom.**

## How to use this skill

1. **Run `workflow.md`** — 6-phase pipeline: Triage → Verification/PoC → Impact → Contact discovery → Email → Coordination & follow-up.
2. **Contact discovery phase** → open `references/contact-discovery.md` (how to find the dev/owner, crypto and non-crypto, + party verification and encryption).
3. **Email phase** → open `references/report-templates.md` (disclosure email + technical report templates, ID/EN).
4. **Need bug classification** (Triage/Impact phase) → `references/vuln-classes.md` (fast recognition: web/API/infra/cloud, smart contract/web3, agent/LLM info-flow).

## Anti-slop rules (non-negotiable)

1. **No PoC, no report.** Every claim is reproducible with evidence (log/screenshot/tx hash).
2. **Impact is shown, not claimed.** Demonstrate minimally and non-destructively; do not cause damage "to prove it".
3. **Repeat ≥3×**, isolate variables, minimize payload/PoC.
4. **Cannot reproduce → drop it.** Do not overclaim severity, no filler.
5. **One report = one clear bug.** Do not bundle 10 text-variant "findings".
6. **Send to the right party and channel.** Verify first, use the dedicated security channel, encrypt sensitive details.

## Output

Deliverable: validated finding → verified dev/owner contact → disclosure email + technical report (language follows the target, ID/EN, natural and technical tone) → coordination/timeline notes.
