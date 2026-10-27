---
name: submission-review-gate
description: 7-Stage Bug Bounty Pipeline & 14-Point Mandatory Pre-Submission Quality Gate. Prevents false positives, severity inflation, and premature submissions.
category: bug-bounty
---

# 7-Stage Pipeline & 14-Point Pre-Submission Review Gate

## Pipeline Stages

```
Stage 1: Recon & Codebase Mapping
   │
   ▼
Stage 2: Attack Surface Discovery
   │
   ▼
Stage 3: Bug Discovery (Candidate Collection)
   │
   ▼
Stage 4: Deep Verification (PoC, Exploit, Economic Impact)
   │
   ▼
Stage 5: Duplicate & Scope Check
   │
   ▼
Stage 6: Report Generator
   │
   ▼
Stage 7: Final Submission Review Gate
   │
   ▼
[READY TO SUBMIT]
```

---

## MISSION & OBJECTIVE

- **MISSION:** No report may be created or sent before it passes this review.
- **OBJECTIVE:** Verify that a finding is genuinely worth submitting, not a false positive, duplicate, intended behavior, or merely a design issue.

---

## 14-POINT MANDATORY PRE-SUBMISSION CHECKLIST

### 1. VALIDATION
- Reproduce at least 5x.
- Run against the latest commit.
- Run against a fork/mainnet-equivalent where possible.
- Make sure the result is consistent.

### 2. IMPACT (PROVE REAL LOSS)
Do not just show a code flaw. Must answer:
- What is stolen?
- What is broken?
- Who is harmed?
- What is the maximum loss?
- Is the exploit scenario realistic?

### 3. PROOF OF CONCEPT (POC)
The PoC must be:
- Repeatable (deterministically re-runnable).
- End-to-end (from the initial condition to the funds gained/impact reached).
- Free of unrealistic assumptions.
- Not requiring privileged access unless that is part of the threat model.

### 4. ROOT CAUSE
Explain:
- Why the bug happens.
- Why validation fails.
- The functions & components involved.
- Call flow diagram / trace.
- State transition breakdown.

### 5. SCOPE VERIFICATION
Make sure:
- The target asset is in scope.
- The commit hash is in scope.
- The smart contract address is in scope.
- It is not a third-party / external dependency issue.

### 6. EXCLUSION CHECK (NOT OUT-OF-SCOPE/NOISE)
Make sure it is NOT:
- Intended behavior / documented design.
- A governance decision / multi-sig admin risk.
- A centralization trade-off.
- A missing best practice with no real loss.
- Informational / gas optimization / code style.
- Dead code with no security impact.

### 7. DUPLICATE CHECK
Search and compare against:
- GitHub Issues & Pull Requests.
- Prior audit reports.
- Known issues & public disclosures.
- Contest writeups (Sherlock, Code4rena, Cantina).

### 8. PATCH CHECK
- Make sure the bug is not already fixed on the developer branch or the latest commit.

### 9. REPORT QUALITY STANDARDS
The report must have the structure:
1. Title (Clear & Descriptive)
2. Summary (Brief & Dense)
3. Root Cause
4. Technical Details
5. Impact Analysis
6. Proof of Concept (PoC)
7. Reproduction Steps
8. Evidence / Logs / Screenshots
9. Recommended Fix (Actionable Remediation)
10. References

### 10. SEVERITY FORMULATION
Compute and decide based on real data:
- CVSS 3.1 Score
- CWE Mapping
- Likelihood & Exploitability
- Business / Economic Impact

### 11. CONFIDENCE SCORE
Evaluate the confidence matrix:
- Validity (0–100%)
- Exploitability (0–100%)
- Impact Measurability (0–100%)
- Duplicate Risk (Low/Med/High)
- Report Quality (High/Low)

### 12. FINAL DECISION MATRIX
The final status output is only one of these options:
- `✅ READY TO SUBMIT`
- `⚠ NEED MORE EVIDENCE`
- `⚠ POSSIBLE DUPLICATE`
- `⚠ OUT OF SCOPE`
- `⚠ DESIGN DECISION`
- `⚠ FALSE POSITIVE`

### 13. SUBMISSION RULES (ZERO TOLERANCE)
- ❌ Never inflate severity.
- ❌ Never invent impact or loss figures.
- ❌ Never invent a bounty estimate.
- ❌ Never claim Critical without a PoC that proves real loss.
- ❌ Never send an automatic submission without operator confirmation.

### 14. ADVERSARIAL SELF-CRITIQUE (TRIAGER PERSPECTIVE)
Before giving the `READY TO SUBMIT` status, simulate a review as the program's Triager and answer:
1. *Why might I reject this report?*
2. *What evidence is still missing?*
3. *Is there another interpretation that makes this intended behavior?*
4. *How confident am I (0–100%) that this report will be accepted and paid?*

`READY TO SUBMIT` may only be issued if all 14 checklist points above pass 100%.
