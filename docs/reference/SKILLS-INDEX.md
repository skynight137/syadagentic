# SKILLS-INDEX.md — Non-Crypto Skills Merged from SYADAGENTIC into SyadAgentic
# Source: subagent curation (48 unique canonical skills, ~90% of files = duplicates)
# Copied into skills/ (non-crypto only — crypto removed as the user asked)

## AUTOMATION (skills/automation/)
- sk4.md — production Telegram bot: message_id dedupe, 429 retry_after,
  polling_error exit on 409, Nginx/FastAPI webhook
- sk6.md — paginate+TokenBucket rate limiter, extract() JSON-path
- sk12.md — (auto: advanced scraping/parsing)
- sk17.md — (auto: batch/parallel)
- captcha-solver/ — solve captcha (reCAPTCHA/slider) for automation

## CTF / RED-TEAM (skills/ctf/)
- sk43.md — CTF web exploitation
- sk44.md — CTF binary pwn
- sk45.md — CTF crypto
- sk46.md — CTF forensics + reverse
- sk47.md — CTF full-auto swarm
- sk48.md — LLM prompt-injection/red-team: TWO guard surfaces (input guard
  blocklist/classifier vs output guard literal-match secret/LLM reviewer)

## SECURITY (skills/security/)
- sk11.md — bug bounty / security audit
- sk21.md — enterprise & defensive (auth.log, KQL, HIDS auto-firewall)
- sk51.md — offensive security & red-team ops (HARD-RAIL: authorized targets only)
- web-exploit-test/ — web exploit testing toolkit

## STATUS
- Techniques from these skills are ALREADY merged into the arsenal (not run
  directly without review)
- Crypto/web3/on-chain skills (swap/NFT/MEV/treasury) = REMOVED per the user's instruction
- The rest (audit-core, webhunter-os, attack-chains) = separate framework,
  can be merged manually if needed
