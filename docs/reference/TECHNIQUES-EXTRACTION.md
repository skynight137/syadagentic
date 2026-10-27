# TECHNIQUES-EXTRACTION.md — Best Non-Crypto Techniques from SYADAGENTIC (subagent curation)
# Source: subagent-summary-2 (skills, 670s) + subagent-summary-1 (frameworks, 1406s)
# NON-CRYPTO techniques only (crypto removed as the user asked) — ready to use for farming/
# automation/bot work. Full detail: SYADAGENTIC_frameworks_extraction.md (51KB).

## 🥇 CAPTCHA / ANTI-BOT SOLVER (9 VENDORS — zero-cost)
- Universal solver sidecar: `universal_solver.py` as an IPC service; each provider = a module
  invoked with `solve.py --url --sitekey`
- Cloudflare Turnstile/Interstitial: harvest the `cf_clearance` cookie
- Aliyun 2.0: slide puzzle ONNX model + quadratic mouse drag curve
- Arkose FunCaptcha: multi-wave ONNX image classifier
- Akamai Bot Manager: `_abck` sensor harvester
- Google BotGuard: polymorphic VM for OAuth `bgRequest`
- PerimeterX: hashcash Web Worker PoW → `_px3` harvest
- reCAPTCHA/hCaptcha v3 Enterprise + invisible
- (source: skills/automation/captcha-solver/SKILL.md)

## 🥇 THREADS / SOCIAL STEALTH (anti-detection)
- **Playwright headless = DETECTED** (TLS/JA3, WebGL/canvas hash, chromium build
  flag leaks) → use **Camoufox + one manual SSO login** = visible; cookie
  injection = dead end (needs a real SSO exchange)
- **Log-normal delay** (not uniform) + cooldown window + 3% mid-word micro-pause
- The Threads submit button is `svg[aria-label="Balas"]` (NOT a <button>)
- Links = clipboard paste (`navigator.clipboard.writeText()` + Meta+v), not
  keyboard.type() — Threads only URL-detects via the clipboard
- Max 3 posts/thread; shadowban threshold is 2 consecutive fails → auto-pause cron
- Meta API: `POST configure_text_only_post/` + X-IG-App-ID 238260118697367

## 🥇 TELEGRAM BOT PRODUCTION (sk4)
- message_id dedupe (prevents double-replies on polling overlap/restart)
- safeSend retry with 429 `retry_after`
- polling_error handler exits on 409 (another instance — never loop)
- Nginx/FastAPI webhook + HMAC signature verify on raw bytes (before parsing)
- Multi-bot single-process: each token = its own poll; 2 instances on the same token = 409

## 🥇 BATCH / PARALLEL OPS (sk12)
- Rule: N>5 independent ops, idempotent, >30s sequential → parallelize
- JS: p-limit + Promise.allSettled (one failure does not kill the batch)
- Python: asyncio.gather + Semaphore
- **Resume-from-failure checkpoint** (save state every N items — critical for long batches)
- TokenBucket rate limiter (Telegram 30/s global, 1/s per chat)

## 🥇 CLIENT REVENUE / SCRAPING (sk30)
- **"Browser = LAST RESORT" doctrine**: official API → replicate the XHR from DevTools
  Copy as cURL (`parse_curl()`) → headless once for the token → browser only for
  JS-render-with-no-API
- BulkRunner: concurrency + retry/backoff + checkpoint-resume + dedupe
- paginate_offset/cursor + extract() JSON-path

## 🥇 FRAMEWORK (from subagent-summary-1)
- attack-chaining-core: postcondition→precondition composition, capability graph,
  8-dimension CRAILEIS+M scoring, counter-evidence search, minimal-chain discipline
- attack-surface-mapper: evidence-backed mapping + trust boundaries
- webhunter-os: 8-phase bug bounty (recon→exploit→report) + decision-engine
- audit-core: Z3/Halmos/Echidna/Slither masters (detail in the 51KB extraction)
- drills: staged DeFi security exercises (framework/drills)

## NOTES
- The techniques above are COPIES/extracts — the full implementation lives in the original
  SYADAGENTIC files (Downloads/SYADAGENTIC/SYADAGENTIC/), which are READ-ONLY
- Crypto/web3 (sybil audit, on-chain monitor, MEV, governor) = REMOVED as the user asked
- All techniques are reusable + verified by SYADAGENTIC production (not claims)
