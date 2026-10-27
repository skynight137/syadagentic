# sk0 — Skill Registry & Reflection Loop (SYADAGENTIC)
# Load when: sk0
# Category: Core

## REGISTRY

Scan the table. Match the intent. Load the matched skill(s) on demand.
Do NOT preload skill files — token cost.

```
ID  | DOMAIN                              | KEYWORDS (high-weight)
----|-------------------------------------|------------------------------------------------
sk1  | Monetization & value generation     | monetize, pricing, sell, selling, profit, funnel
sk2  | Infrastructure & deployment         | VPS, deploy, SSH, nginx, docker, systemd
sk3  | Content creation & distribution     | viral, hook, caption, thread, script, content
sk4  | Process orchestration & bots        | telegram bot, cron, webhook, n8n, automate, automated
sk5  | Data transformation & insight       | spreadsheet, excel, csv, dataset, snapshot, report
sk6  | Protocol binding & service bridge   | API, REST, webhook, midtrans, integration
sk7  | Inference systems & AI builder      | LLM, prompt, claude API, openrouter, kimi, agent, add model, model registry
sk8  | File & artifact production          | PDF, DOCX, XLSX, PPTX, generate file, document
sk9  | Interface construction              | landing page, react, tailwind, frontend, UI
sk10 | Web3 / crypto operations            | wallet, airdrop, on-chain, RPC, ethers, viem, mint
sk11 | Security audit & review             | audit, vulnerability, exploit, scam check, malicious
sk12 | Batch / parallel operations         | batch, parallel, bulk, mass, queue, worker, snapshot
sk13 | Universal NFT minter (any contract) | mint, opensea, manifold, zora, seadrop, NFT, claim, drop
sk14 | Daily assistant: briefing & alerts  | briefing, daily summary, alert, notify me when, price watch, alarm
sk15 | Daily assistant II: watchdog/vault/multimodal/triage | watchdog, restart if dead, save address, macro, voice note, screenshot, triage
sk16 | Software engineering & coding       | coding, build app, backend, API server, database, testing, scaffold, refactor, golang, rust, fastapi
sk17 | Power pack: planner/swarm/automation/backtest/dashboard/voice | plan it, workflow, auto when, backtest, dashboard, talk, swarm, agent team
sk18 | Creative & media generation         | comfyui, manim, excalidraw, ascii video, slide, design system, diagram, deck
sk19 | Desktop & physical control          | isaac sim, omniverse, robot, macos control, applescript, scene, usd, mobility, ros2
sk20 | Humanizer & brand voice             | humanizer, brand voice, ai tone, human, rewrite tone, voice profile
sk21 | Enterprise & defensive ops          | KQL, azure, log analytics, sentinel, HIDS, auto firewall, block ip, intrusion
sk22 | Scientific & deep research          | deep research, AI-Q, tooluniverse, hypothesis, citations, scientific research, experiment
sk23 | Executive function & neurodivergent | task breakdown, executive function, ADHD, overwhelmed, focus, context switch, priority
sk24 | MCP-builder & prompt engineering    | MCP server, build MCP, FastMCP, prompt engineering, fix prompt, audit prompt
sk25 | Compliance, CI/CD & code migration  | compliance, regulation, GDPR, SOC2, CI/CD, pipeline, code migration, language port
sk26 | Product & spec workflows            | PRD, to-issues, grill me, spec, user story, TDD, internal comms
sk27 | Content strategy & social media     | content calendar, content strategy, content pillar, carousel, reels, platform adapter, scroll-stopper
sk28 | Copywriting & writing mastery       | AIDA, PAS, CHEF, copywriting framework, SEO writing, storytelling, localization, multilingual
sk29 | Content research, analytics & pipeline | competitor analysis, trend research, social listening, audience insight, content pipeline, A/B caption, best time post
sk30 | Client Revenue Engine (bulk gig, API-first) | client revenue, gig work, bulk gig, harvest, scrape API, anti-browser, mass accounts, client job automation, extract data
sk31 | Airdrop Intelligence (eligibility/sybil/claim/exit) | airdrop eligibility, airdrop score, airdrop-worthy, sybil, anti-sybil, claim window, claim schedule, airdrop calendar, vesting unlock, exit plan, when to sell token
sk32 | CTF / Whitehat toolkit                  | CTF, capture the flag, whitehat, bug bounty, decode flag, crypto challenge, caesar, xor cipher, hash identify, forensics, HTB, THM
sk33 | Pre-TGE Alpha Radar (early airdrop detection) | alpha airdrop, pre-TGE, points program, testnet incentivized, airdrop radar, project with no token yet, worth farming
sk34 | Farming Portfolio & ROI Optimizer       | farming ROI, airdrop portfolio, farming profit and loss, gas vs yield, which farm to continue, drop farming, idle wallet
sk35 | Auto Guide Studio (automatic guides)    | write an airdrop guide, airdrop tutorial, step by step guide, airdrop article, embed referral
sk36 | Tokenomics & Unlock Pressure Engine     | token unlock, vesting, cliff, unlock calendar, sell pressure, tokenomics, sell before unlock
sk37 | Anti-Scam Sentinel (brand protection)   | fake site, fake domain, typosquat, airdrop phishing, scam check, scam warning, drainer
sk38 | Contract-Change & Claim-Address Watcher | contract changed, proxy upgrade, claim address, safe to claim, watch contract, check before claim
sk39 | Community Intelligence (listen to the community) | community trending topic, community sentiment, FUD, chat analysis, member questions, community content ideas
sk40 | Omni-Repurpose Engine (1 content → all) | repurpose content, turn into thread, IG carousel, tiktok script, youtube script, multi platform
sk41 | Video Script-to-Screen Pipeline         | make video, video script, storyboard, voiceover, subtitle, srt, reels, youtube video
sk42 | Hook A/B Lab + Performance Predictor    | hook, content title, headline, title a/b test, stop scroll, engagement prediction, title variants
sk43 | CTF Web Exploitation (sub of sk32)       | CTF web, SQLi, SSTI, SSRF, IDOR, XXE, JWT, deserialization, prototype pollution, race condition
sk44 | CTF Binary Exploitation / pwn (sub sk32) | CTF pwn, buffer overflow, ret2win, ret2libc, format string, heap, ROP, pwntools, GOT leak
sk45 | CTF Reverse Engineering (sub of sk32)    | CTF reverse, angr, symbolic execution, Ghidra, radare2, decompile, keygen, deobfuscation
sk46 | CTF Cryptography (sub of sk32)           | CTF crypto, RSA attack, Wiener, Hastad, common modulus, Coppersmith, padding oracle, nonce reuse
sk47 | CTF Forensics & Stego (sub of sk32)      | CTF forensics, stego, pcap, memory dump, volatility, binwalk, exiftool, zsteg, steghide
sk48 | CTF Prompt-Injection/LLM (sub of sk32)   | CTF prompt injection, LLM red-team, jailbreak, Gandalf, Lakera, Mosscap, OWASP LLM01, extract system prompt
sk49 | Team Orchestration & Multi-User Ops  | team, members, collaboration, delegate, assign, task routing, multi-user, role, billing split, assign task, client management
sk50 | Autonomous Monetization Engine       | monetize, revenue, profit, earning, income, treasury, yield, P&L, cashflow, auto-revenue, passive income, profit report, money maker
sk51 | Offensive Security & Red-Team Ops    | offensive, red-team, adversary, exploit dev, backdoor, payload, C2, implant, post-exploit, persistence, lateral movement, exfil, opsec

H1  | Swap & sell via aggregator          | swap, 1inch, jupiter, sell token, sell, DEX
H2  | Cross-chain bridge                  | bridge, LayerZero, stargate, LI.FI, across, hop
H3  | DeFi (lending/staking/perp)         | aave, lido, GMX, hyperliquid, pendle, defi
H4  | Token launch & NFT mint sniping     | snipe, honeypot, PairCreated, GoPlus, sniping
H5  | Whale & mempool tracking            | mempool, whale, nansen, arkham, smart money, tracker
H6  | NFT buy/sell (marketplace)          | buy NFT, blur, magic eden, tensor, reservoir, listing
H7  | Web3 sign-in & typed signing        | SIWE, walletconnect, EIP-712, ENS, permit, EIP-1271
H8  | Browser dApp automation             | open dapp, browser, playwright, navigate, connect wallet, fill form
H9  | Universal contract read/write       | read/write contract, read/write, call function, ABI, inspect, proxy, execution
H10 | Crypto dev: deploy/compile/test     | deploy contract, compile, forge, solidity, test, verify, CREATE2, build token

sk52  | Internal capability refinement      | improve system, self-audit, upgrade brain
sk53  | Deep decomposition & strategy       | strategy, architecture, decompose, plan, design system
sk54  | Fault diagnosis & resolution        | error, bug, debug, failed, broken, stack trace
sk55  | Self-improvement & autonomous fix   | self improve, learn, get smarter, auto fix, upgrade self
sk56  | Agentic eval & self-critique        | eval, self-critique, variance, consistency, flaky, regression, measure
sk57  | Systematic debug & auto-debug loop  | systematic debug, RCA, root cause, hypothesis, intermittent, reproduce
sk58  | Problem shaping & decision support  | problem shaping, brainstorming, sign-off, framing, vague goal, uncertainty
```

### V7 NEW SKILLS (sk49–sk51)

**sk49 — Team Orchestration & Multi-User Ops**: team delegation (Level 0–3 routing), task assignment tracking, per-member billing attribution, conflict detection & resolution, client management dashboard, multi-session awareness, role-based access control. → `skills/sk49.md`

**sk50 — Autonomous Monetization Engine**: treasury management, cashflow tracking, P&L generation, revenue stream optimization, auto-revenue strategies (MEV, airdrop, yield, NFT flip), cost optimization, profit reporting (daily/weekly/monthly), passive income pipeline maintenance. → `skills/sk50.md`

**sk51 — Offensive Security & Red-Team Ops**: exploit development lifecycle (research → PoC → weaponize), C2 infrastructure (Cobalt Strike/Mythic/Sliver patterns), post-exploitation (persistence, lateral movement, privilege escalation), payload generation (shellcode, DLL hijacking, process injection), operational security (OPSEC), adversary simulation (MITRE ATT&CK mapping), red-team infrastructure design, phishing & social engineering frameworks. → `skills/sk51.md`

---

## ROUTING

```
0 matches:     answer from core knowledge — load nothing
1 match:       load the full skill file
2+ matches:    pick PRIMARY (highest score), load it fully
               pull SUPPORTING (>50% of primary's score) section-by-section
ambiguous tie: ask once — "Focus on [A] or [B] first?"
H-skill hit:   load skills/hermes/DISPATCH.md FIRST, then the specific reference
```

### Hermes routing
H1-H10 are NOT standalone files. They map to `skills/hermes/references/*.md`:
```
H1 → hermes/references/swap.md       H2 → hermes/references/bridge.md
H3 → hermes/references/defi.md       H4 → hermes/references/sniping.md
H5 → hermes/references/monitoring.md  H6 → hermes/references/nft.md
H7 → hermes/references/web3_connect.md H8 → hermes/references/browser.md
H9 → hermes/references/contract_read.md + contract_write.md
H10 → hermes/references/deploy.md
```
Load `hermes/DISPATCH.md` once per session if any H-skill fires.

---

## REFLECTION LOOP

Runs silently after every output. Non-negotiable.

```
✅ Immediately executable / usable as-is?
✅ Anything the operator will need next that's missing?
✅ Generic advice — could be replaced with operator-specific code?
✅ Faster or cleaner path missed?
✅ Did I include the run command / deploy step?
✅ Token usage justified — could the same value land in fewer lines?
✅  Does this generate value or move the profit needle?
✅  Can this scale to the team?
```

Any fail → revise BEFORE outputting.
An upgrade exists → append: `🔧 Upgrade: [one line]`
Revenue applies → append: `💸 Revenue: [estimated impact]`

---

## REFLECTION ESCAPE HATCH

If the reflection loop catches an issue but the fix would 2x the response length → ship the working version, append:
> `🔧 Could be upgraded to [X]. Want me to elaborate?`

---

## AUTONOMOUS SCAN 

After every reflection loop, scan the autonomous triggers table from AGENTS.md.
If any trigger fires → auto-execute in the background, log to memory.
Push exceptions to the next briefing.
