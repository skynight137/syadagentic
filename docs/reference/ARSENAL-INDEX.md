# ARSENAL INDEX — SyadAgentic v4 (all skills/tools curated)
# Location: repo root (the vendored jailbreak repos are gone; our templates live in templates/jailbreak/)

## JAILBREAK (per-model)
- jailbreak/L1B3RT4S/ — liberation prompts (21k⭐, elder-plinius)
- jailbreak/CL4R1T4S/ — leaked system prompts ChatGPT/Claude/Gemini/Grok (47k⭐)
- jailbreak/system-prompts-leaks/ — Anthropic/Claude system prompts (63k⭐, 423 files)
- jailbreak/system-prompts-ai-tools/ — ALL tools system prompts (143k⭐)
- jailbreak/jailbreak_llms/ — 15,140 jailbreak prompts dataset (CCS'24)
- jailbreak/deepseek-v4-unrestricted/ — DeepSeek 破甲 prompt bank, 360 cases (66KB)
- jailbreak/coldbrew-4in1/ — GPT-5.6/Claude/Grok4.6/DSv4pro 破甲 (823 files, China)
- jailbreak/jailbreak-prompts-cn/ — Codex red-team system prompt (China)
- jailbreak/shadow-jb/ — Jailbreaks GPT/Gemini/DeepSeek (1.2k⭐)
- jailbreak/awesome-jb/ — Awesome-Jailbreak-on-LLMs (1.6k⭐)
- jailbreak/zorg/ — ZORG jailbreak prompts
- MASTER-JB-TEMPLATES.md — T100-T105 template per family (ours)

## BYPASS/STEALTH (tools)
- scripts/cloudscraper/ — CF v1/v2/v3 + Turnstile bypass (6.7k⭐, v3:
  403 auto-recovery, fingerprint rotation, stealth, 70+ UA)
- scripts/nopecha-python/ — CAPTCHA solver (nopecha API)
- scripts/cf-clearance-scraper/ — CF clearance token scraper
- scripts/trawl/ — self-hosted scraping engine (CF bypass, 718⭐)
- scripts/gpt-load/ — AI proxy multi-channel key rotation (China, 6.3k⭐)
- scripts/fireprox/ — AWS API gateway IP rotation (2.3k⭐)

## FRAMEWORK/REF (optional)
- jailbreak/jailbreakbench/, awesome-jb — benchmark & dataset
- (extra catalog in CURATION-MASTER.md: 48 repos batch 1 + 61 batch 2)

## QUICK START
1. Model JB: pick a template from MASTER-JB-TEMPLATES.md (T100 for Codex/GPT,
   T101 for DeepSeek, T102 for Gemini) → inject via jb_injector :20129 / direct.
2. CF bypass: cloudscraper (pip install cloudscraper) — use a custom session.
3. Captcha: nopecha-python + API key.
4. IP rotation: fireprox (AWS) / gpt-load (AI keys).
