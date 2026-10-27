# TECHNIQUES-EXTRACTION PART 2 — .py Tools (non-crypto, from direct reading)
# Continuation of the scripts/ curation of SYADAGENTIC. Reusable NON-CRYPTO patterns only.

## GENERALLY USEFUL PATTERNS (non-crypto)

### Humanizer (content/humanizer.py)
- Detects "AI-tells" + deterministic rewrite into something natural (regex, stdlib, keyless)
- "repeated tricolon → vary it, never always 3"
- Burstiness: uniform sentence length = AI-tell → vary it
- Heavy rewrites still go through an LLM (model_registry)

### API-first harvesting (intelligence/api_harvester.py)
- DevTools → Network → "Copy as cURL" → parse_curl() → paginate_* → extract() → to_*
- "Browser = LAST RESORT" — replicate the request, do not click around
- Reduces the anti-bot footprint + saves resources

### Global Dry-Run (meta/dryrun.py)
- One flag honored by EVERY engine: when active → run the full pipeline WITHOUT
  broadcasting, collect "what would have happened"
- Structural safety (not prompt-based)

### Compounding Memory (meta/memory_engine.py)
- Stores facts/lessons/preferences/decisions/blockers+resolutions → relevant recall
- "smarter every day" — the substrate for self-improvement

### Self-Improvement Loop (meta/reflection.py)
- LEARN: scan memory/log → distill patterns into 'lessons' (saved to memory)
- Strict gate: what may be auto-applied vs what needs confirmation

### Multi-Agent Swarm (meta/swarm.py)
- Spawns parallel specialist lanes (researcher/executor/monitor) → aggregation
- In-process & lightweight, compatible with the delegate architecture

### Bulk Runner (monetization/revenue_engine.py)
- Rate-limit, backoff, checkpoint-resume, dedupe — pure stdlib, testable offline

## NOTES
- The other .py tools = crypto/web3/airdrop (alpha_radar, eligibility, farm_roi,
  unlock_engine, exit_planner, security_daemon, team_auth SIWE, auto_bot,
  contract_watch) = REMOVED as the user asked — not merged
- The patterns above are generic (non-crypto) → useful for the SyadAgentic framework
