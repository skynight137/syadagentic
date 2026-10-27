# Workflow — Bug Bounty & Coordinated Disclosure

6-phase pipeline from finding to fix. Before starting, make sure the **testing basis is legitimate** (see the guardrail in SKILL.md).

---

## Phase 0 — Finding triage

Goal: make sure this really is a security issue, not noise.

- Classify the bug class → `references/vuln-classes.md` (web/API/infra/cloud, smart contract/web3, agent/LLM).
- Determine which **security boundary** is violated: who should not be able to do what, but can.
- Drop what is not a bug: by-design behavior, out-of-scope, known-issue duplicate, self-XSS with no impact, etc.

Output: one clear sentence — "X can do Y when it should not, because of Z".

---

## Phase 1 — Verification & PoC

This is what separates a real report from AI slop.

- **Reproduce ≥3×.** If non-deterministic, record the rate.
- **Minimal and non-destructive PoC.** Prove enough to show the bug, do NOT cause real damage (do not drain funds, do not delete data, do not disturb other users). For web3: use a fork/simulation (e.g. mainnet fork) for the demo, not a real on-chain exploit.
- **Isolate variables**, minimize the payload, determine which component actually triggers it.
- Collect evidence: request/response logs, screenshots, tx hash (for web3), video if needed.

Output: a PoC someone else can repeat exactly.

---

## Phase 2 — Impact & severity

- Map what the attacker can do: data exfil, account takeover, RCE, drain funds, cross-user/cross-tenant, DoS, etc.
- Scale: single user vs all users vs the whole protocol.
- Prerequisites: what privilege/victim interaction is needed? The fewer the prerequisites → the higher the severity.
- Score with a recognized framework (CVSS generally; for web3 add "funds at risk" & exploitation likelihood). Be honest — over-claiming destroys credibility.

Output: severity + 2–3 sentence rationale.

---

## Phase 3 — Find the dev/owner contact

Method details → `references/contact-discovery.md`. Priority summary:

1. **Official security channel first**: `/.well-known/security.txt`, `SECURITY.md`, the `/security` page, a program on HackerOne/Bugcrowd/Immunefi/HackenProof (even if you found it outside the platform, many still accept reports).
2. **If there is no program**: contact the maintainer/owner directly — GitHub org/maintainer, email in the repo/website, WHOIS, DNS SOA, package registry maintainer.
3. **Web3**: project docs, GitHub, Discord/Telegram admins, official Twitter/X, ENS, deployer/multisig signer on-chain, the auditor (can act as relay), governance forum.
4. **Dead end / unresponsive team**: third-party coordinator (CERT/CC, national CERT, disclose.io) for mediation.

**Verify the party** before sending: make sure it is the legitimate owner/maintainer, not a fake account. Prioritize a dedicated security contact over a personal DM.

Output: 1–2 verified contacts + their channels.

---

## Phase 4 — Send the report via email

Full templates → `references/report-templates.md`.

- **Clear subject**: `[Security] Vulnerability disclosure — <project/asset>`.
- **Body**: brief identity + good-faith intent → what & where → impact → minimal PoC → offer to coordinate → disclosure timeline (default 90 days, adjustable; speed up if funds are live at-risk) → no threats/ransom.
- **Encrypt sensitive details** (PGP from security.txt) — mandatory for unpatched high-impact bugs / funds at risk.
- Attach a separate technical report if it is long.
- If an agent is sending: use the available email tool; send to the verified contact from Phase 3; do not blast several addresses at once (pick the most official channel).

Output: email sent + report archive.

---

## Phase 5 — Coordination & follow-up

- Record the send date & response deadline (e.g. a polite follow-up after 7–14 days of silence).
- Help the team reproduce/verify if they ask.
- **Do not publish** before the fix is deployed or the agreed timeline runs out. For web3 with funds at risk: delay publication until it is safe.
- If the owner cannot be reached / goes fully silent after reasonable effort → escalate to a coordinator (CERT/CC) rather than unilateral full disclosure.
- Close with a summary: bug, timeline, fix status, credit (if given).

Output: coordination notes + final status.
