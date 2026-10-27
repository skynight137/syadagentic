# Operator Guide — Hermes + SYADAGENTIC v7.0 SYADAGENTIC SUPREME

How to talk to Hermes after v7.0 OPENCLAW EDITION + hermes-crypto-agent combo.
*v7.0 update (2026-06-09): Airdrop Intelligence (sk31), CTF/Whitehat (sk32), + observability & safety tooling.*

---

## Table of Contents

**Crypto operations (Hermes runtime)**

1\. [Default mode vs fast mode](#default-mode-vs-fast-mode)  
2\. [Mint NFT](#mint-nft)  
3\. [Swap token](#swap-token)  
4\. [Bridge cross-chain](#bridge-cross-chain)  
5\. [Sniping token launch](#sniping-token-launch)  
6\. [Airdrop farming multi-wallet](#airdrop-farming-multi-wallet)  
7\. [Mempool watch (anti-drainer)](#mempool-watch-anti-drainer)  
8\. [Buying NFTs on a marketplace](#buying-nfts-on-a-marketplace)  
9\. [Whale & smart-money tracker](#whale--smart-money-tracker)

**Airdrop Intelligence & Whitehat — NEW in v7.0**

10\. [Airdrop Intelligence (sk31)](#airdrop-intelligence-sk31--new-in-v70)  
11\. [CTF / Whitehat toolkit (sk32)](#ctf--whitehat-toolkit-sk32--new-in-v70)  
12\. [CTF Swarm full-auto (sk32 → sk43–sk48)](#ctf-swarm-full-auto-sk32--sk43sk48--v70-update)  
13\. [Rug & legitimacy check](#rug--legitimacy-check--new-in-v70)  
14\. [New observability & safety](#new-observability--safety--v70)

**Growth & Protection — sk33–sk42 (v7.0 update, 12 Jun)**

15\. [Alpha & farming intelligence (sk33 · sk34 · sk36)](#alpha--farming-intelligence-sk33--sk34--sk36--v70-update)  
16\. [Community protection (sk37 · sk38)](#community-protection-sk37--sk38--v70-update)  
17\. [Content & community engine (sk35 · sk39–sk42)](#content--community-engine-sk35--sk39sk42--v70-update)

**Sessions & ops**

18\. [Session control commands](#session-control-commands)  
19\. [Background job persistence](#background-job-persistence)

**Non-crypto skills & reference**

20\. [Non-crypto skills (v7.0) — example commands](#non-crypto-skills-v70--example-commands)  
21\. [Cheat sheet — natural language to skill route](#cheat-sheet--natural-language-to-skill-route)  
22\. [What to prepare before starting](#what-to-prepare-before-starting)  
23\. [Quick verification that v7.0 + hermes is running](#quick-verification-that-v70--hermes-is-running)

---

## Default mode vs fast mode

Hermes has 2 operating modes. Default = safe, fast mode = fire and forget.

### Default — confirm before signing
Every important tx gets a short plan + a `(y/n)` gate. Good for:
- The first tx in a new session
- Main wallet / large funds
- Operations you have never done before
- Contracts that have not been audited

### Fast mode — `auto_confirm on`
Skips the per-tx prompt. The first tx still gets a 1-line summary (info only, not a gate). Good for:
- Batch ops (mass mint, multi-wallet farming)
- Small wallets / test wallets
- Routine operations you already know
- Sniping where speed matters

```
Operator: auto_confirm on
Hermes: [AUTO_CONFIRM] ON. tx will fire without a gate until this session ends or you set it off.

Operator: auto_confirm off
Hermes: [AUTO_CONFIRM] OFF. back to safe mode.
```

Operational rails that STAY on even with auto_confirm on:
- Secret hygiene (never logs a priv key)
- Simulate before broadcast
- Drainer/scam code detection
- User-funds-only

---

## Mint NFT

### Single mint from a URL
```
Operator: mint NFT https://opensea.io/assets/base/0xABC.../1
```

Hermes automatically:
- Parses the URL → chain `base`, contract `0xABC...`
- Probes the mint function (publicMint, mint, claim, etc.)
- Detects the price via `mintPrice()` / Seadrop config
- Auto-gas (estimate + buffer)
- Simulate → send → wait → report

Output:
```
[TARGET] 0xABC... on base × 1
[FN]     mintPublic(uint256) — detected
[PRICE]  0.0014 ETH
[GAS]    180k @ 0.05 gwei  →  ~$0.02
[SENT]   0xtxhash...
[OK]     block 12345678  gasUsed 142,330
[VIEW]   https://basescan.org/tx/0xtxhash...
```

### Mass mint with N wallets
```
Operator: auto_confirm on. mint https://opensea.io/assets/base/0xABC.../1 with 50 wallets
```

Output:
```
[BATCH MINT] 50 wallets × NFT 0xABC... on base
est total cost: 0.0070 ETH (50 × 0.0001 mint fee)
concurrency: 5
[SENDING]

[3/50]   0xAbC...d4F1   ✅ 0xtx1...
[7/50]   0xDeF...c2A3   ✅ 0xtx2...
[12/50]  0x123...8F9    ❌ AlreadyMinted
...
[DONE]   47/50 ok, 3 failed → mint-[PHONE_REDACTED].json
```

### Mint Manifold / Zora
Same, paste the URL directly:
```
Operator: mint https://app.manifold.xyz/c/12345
Operator: mint https://zora.co/collect/base:0xABC.../1
```

Hermes uses a protocol-specific handler (Manifold instanceId fetch, Zora 1155 protocol fee).

---

## Swap token

### Simple swap
```
Operator: swap 0.5 ETH to USDC on base, use the first wallet
```

Plan:
```
[PLAN]
chain:    base
wallet:   0xAbC...d4F1 (wallet#1)
action:   swap 0.5 ETH → USDC (via 1inch)
slippage: 1%
est out:  ~1,847 USDC
gas:      ~$0.02

Proceed? (y/n)
```

`y` → fire. Tx hash + explorer link.

### Sell all of a token holding
```
Operator: sell semua $PEPE di wallet#1, ke USDC
```

Hermes:
- Checks the PEPE balance in the wallet
- Quotes via 1inch
- Shows the plan
- Executes (if the approve is missing, it approves first automatically)

### Swap via a chosen DEX aggregator
```
Operator: swap 1000 USDC ke ETH di arbitrum via jupiter
```
(Jupiter is for Solana. For EVM the default is 1inch — Hermes auto-corrects.)

---

## Bridge cross-chain

### Simple bridge
```
Operator: bridge 500 USDC from arbitrum to base using stargate
```

Plan:
```
[BRIDGE PLAN]
from:    arbitrum  → 500 USDC
to:      base      → 499.32 USDC (after fees)
route:   Stargate V2
fee:     0.68 USDC
eta:     ~2 menit
gas:     ~$0.30
bonus:   eligible LayerZero points

Proceed? (y/n)
```

`y` → execute → wait until it lands on the destination chain → confirm.

### Bridge with an automatic route (LI.FI)
```
Operator: bridge 0.1 ETH from eth to base, cheapest route
```

Hermes uses the LI.FI aggregator and picks the optimal route automatically (Across / Stargate / native / Hop — whichever is cheapest).

### Bridge to non-EVM (Solana via Mayan)
```
Operator: bridge 100 USDC from base to solana
```

Hermes uses Wormhole + Mayan for EVM ↔ Solana. The Solana wallet must already be imported in the vault.

---

## Sniping token launch

### Set up a sniper
```
Operator: snipe new token on base, budget 0.05 ETH per launch, max 3 launches today
```

Output:
```
[SNIPER ACTIVE] base / Uniswap V3 PairCreated
filter:   WETH pair only
budget:   0.05 ETH / launch
max:      3 launches today
safety:   honeypot.is + GoPlus required
wallet:   0xAbC...d4F1
[LISTENING...]

pm2: sniper-base (id 2)
log: pm2 logs sniper-base
```

When a new pair is detected:
```
[DETECTED] 0xNew...Token, paired with WETH at block 12345678
[SAFETY]   honeypot.is: clean | GoPlus: 1 warning (mintable)
⚠️ mintable token (owner could inflate supply). Continue snipe? (y/n)
```

`auto_confirm on` → auto-block on a CRITICAL flag, auto-proceed if it is only WARN.
`auto_confirm off` → ask per detection.

### Snipe an NFT mint launch
```
Operator: snipe mint NFT collection https://opensea.io/collection/<slug>, watch from now until mint opens
```

Hermes watches the drop status (reads the `getPublicDrop()` Seadrop config) and fires the mint the second the mint window opens.

### Stop a sniper
```
Operator: stop sniper-base
```

---

## Airdrop farming multi-wallet

### LayerZero farming
```
Operator: layerzero farming, 50 wallet, bridge variasi route 5 chain selama 7 hari
```

Sybil reminder (once per session):
```
⚠️ LayerZero has sybil detection and can blacklist every related wallet.
I randomize timing (5-180 minutes) + amount jitter (±15%) + bridge variation per wallet.
Risk remains. Proceed? (y/n)
```

`y`:
```
[FARMING PLAN]
wallets:   50
chains:    eth, arb, base, op, polygon (5 chains)
tx/wallet: 14-21 (random)
duration:  7 days
total tx:  ~875 (estimate)
est cost:  ~$45 total gas

[STARTED] background runner: pm2 lz-farming
[CHECK]   pm2 logs lz-farming
[STOP]    "stop lz-farming"
```

### zkSync / Linea farming, same pattern
```
Operator: zksync farming, 30 wallet, daily activity selama 14 hari
Operator: linea voyage tasks with 25 wallets
```

### Daily airdrop check-in
```
Operator: daily check-in airdrop X with all wallets, 8 AM WIB
```

Hermes sets up a cron job that runs automatically every day.

---

## Mempool watch (anti-drainer)

### Set up a watcher
```
Operator: watch my wallet 0xAbC...d4F1 for suspicious approvals, alert to TG
```

Output:
```
[WATCHER ACTIVE]
target:   0xAbC...d4F1
chains:   ethereum, base, arbitrum
triggers: approve(), setApprovalForAll(), permit()
alert:    @your_alerts_channel channel
filter:   spender must be a verified contract, otherwise → CRITICAL

running as pm2: anti-drainer (id 3)
```

When a suspicious approval is detected in the mempool (before it confirms):
```
🚨 CRITICAL APPROVAL DETECTED 🚨
wallet:   0xAbC...d4F1
action:   setApprovalForAll(0xSpender..., true)
spender:  0xSus...Address (no verified contract)
tx:       0xpending...

STATUS: pending in mempool (~12s before confirm)
ACTION: if this is not you, send a front-run revoke tx NOW
        "revoke approval 0xSus... di wallet#1"
```

### Auto-revoke mode
```
Operator: anti-drainer auto-revoke mode on for wallet#1
```

If Hermes detects an approval to a non-whitelisted contract → it broadcasts a revoke tx with higher gas automatically, race-conditioning the drainer.

---

## Buying NFTs on a marketplace

### OpenSea specific listing
```
Operator: beli BAYC #1234 di opensea, max 25 ETH
```

Plan:
```
[LISTING FOUND]
collection: BAYC
token id:   #1234
price:      22.5 ETH (below max)
seller:     0xSeller...
protocol:   Seaport 1.6
gas:        ~$8

Proceed? (y/n)
```

### Floor sweep
```
Operator: sweep floor Pudgy Penguins, 5 unit, max avg 10 ETH per piece
```

Hermes uses the Reservoir aggregator (checks the lowest listings across marketplaces: OpenSea, Blur, LooksRare). Bulk fulfill in 1 tx when possible.

### List an NFT for sale
```
Operator: list NFT #5678 from collection 0xMy... on opensea, price 1.5 ETH, expire 7 days
```

Hermes signs an EIP-712 Seaport order → posts to the OpenSea API. The listing goes live on the marketplace.

### Magic Eden / Tensor (Solana)
```
Operator: beli SMB #1234 di magic eden, max 50 SOL
```

Same flow, different protocol (Magic Eden ME instruction, not Seaport).

---

## Whale & smart-money tracker

### Track a whale wallet + TG alert
```
Operator: smart money tracker via nansen, alert to TG on any buy > $50k
```

Output:
```
[TRACKER ACTIVE]
source:   Nansen Smart Money label
filter:   buy size > $50k
chains:   ethereum, base, arbitrum, solana
alert:    @your_alerts_channel

pm2: smart-money-watch (id 4)
```

Alert format:
```
🐋 SMART MONEY BUY
wallet:   0xWhale... (Nansen: "Smart Trader")
action:   bought 12.5 ETH worth of $TOKEN
chain:    base
contract: 0xToken...
tx:       https://basescan.org/tx/...
```

### Copy-trade pattern
```
Operator: copy-trade wallet 0xWhale..., size 5% of their size, max $500 per trade
```

Hermes monitors the whale wallet → mirrors the buy at a small size in your wallet, filtering stablecoin transfers and low-value noise.

### NFT whale alert
```
Operator: alert when a whale buys an NFT > 10 ETH in a blue chip collection
```

Hermes uses the Reservoir WebSocket stream — real-time push notification.

### Floor drop alert
```
Operator: alert when the BAYC floor drops > 5% in 1 hour
```

---

## Airdrop Intelligence (sk31) — NEW in v7.0

A skill dedicated to AirdropFinder: turns the airdrop cycle into number-backed decisions. Every tool is **offline & deterministic** — on-chain data is pulled first via sk10/hermes, then sk31 does the judging and builds the plan. Fund movement (claim/exit) still goes through the Spend Governor.

### 1. Eligibility scorer — is this wallet eligible?
```
Operator: skor eligibility wallet 0xAbC...d4F1 buat airdrop Linea
```

Output:
```
[ELIGIBILITY] 0xAbC...d4F1 — Linea
score:   72/100  (TIER: likely)
✅ strong: age 210d, 47 tx, bridged 3x, 4 unique contracts
⚠️ gap:    volume $1.2k (target >$5k), no native DeFi interaction yet
🚩 flag:   low gas spend (bot-like? check manually)
suggestion: + 2-3 swaps on a native DEX, + 1 LP position → projected ~85/100
```

The rubric can be overridden per project (when you know the project's specific criteria):
```
Operator: skor wallet#1 buat ZkSync, bobot: volume 40%, age 20%, kontrak unik 40%
```

### 2. Sybil self-audit — is my farm wallet safe?
This is a **safety net for your own wallets** — it checks whether the cross-wallet pattern is easy for a sybil filter to cluster, so you can de-correlate. Not for tricking the project.
```
Operator: sybil audit my 50 farm wallets
```

Output:
```
[SYBIL AUDIT] 50 wallets
risk: HIGH ⚠️
correlation detected:
  • funding: 38 wallets funded from 1 source (0xFund...) — RED
  • timing: 22 wallets tx inside the same 5-minute window — RED
  • gas pattern: identical amounts on 41 wallets — YELLOW
  • contract overlap: every wallet touches the same contracts in the same order
de-correlation advice:
  1. Vary the funding source (use different CEX withdrawals)
  2. Spread the timing (randomize 1-72 hours, do not batch)
  3. Vary the order & type of interaction per wallet
  4. Amount jitter ±15-30%
```

### 3. Claim-window calendar — do not miss a claim
`now` is always injected (never guesses the time). Alerts fire once at D-48 / D-2 / D-0.
```
Operator: tambah ke kalender airdrop: ZK claim buka 17 Jun 14:00 WIB, tutup 24 Jun
Operator: which airdrops have a claim window this week?
```

Output:
```
[CLAIM CALENDAR] this week (12-18 Jun)
🔔 ZK        — opens 17 Jun 14:00 WIB (D-5)   [alert set: D-48, D-2, D-0]
🔔 LayerZero — closes 15 Jun 23:59 WIB (D-3)  ⚠️ not claimed on 12 wallets!
✅ Scroll    — already claimed on every wallet
```

### 4. Exit planner — when & how to sell
```
Operator: exit plan buat 5000 $ZK, profil balanced, likuiditas tipis
```

Output:
```
[EXIT LADDER] 5000 $ZK — profile: balanced
thin DEX liquidity → split the sell so slippage does not bite
  • TGE +0h:   sell 30% (1500) — secure the principal
  • +24h:      sell 25% (1250) — if price > TGE
  • +7d:       sell 25% (1250) — or cut if it dumps
  • hold 20%:  moonbag (1000)
⚠️ vesting: check first, if there is a cliff shift part of the sells
execution via the Spend Governor (per-leg gate, or auto_confirm on)
Set up the auto-sell ladder? (y/n)
```

---

## CTF / Whitehat toolkit (sk32) — NEW in v7.0

For operators who join CTFs & bug bounties for rewards. **Legal & in-scope only** — a foreign target hits gate R9 (⚠️ permission? y/n) and is held by default. The core tools are stdlib-only & passive (decode/analysis); active exploits stay manual + need permission.

### Triage a challenge — which category is this, where to attack
```
Operator: triage this CTF challenge: "given an RSA public key with small e, decrypt the flag"
```
```
[TRIAGE] category: crypto (high confidence)
direction: RSA small-e → try cube-root attack (e=3, no padding)
tooling: sk32 (manual math), or sage if available
```

### Automatic layered decode
```
Operator: decode this: NHZ4dnRoaXNfaXNfYmFzZTY0X2ZsYWc=
```
```
[DECODE] peeling layers (ordered by printability):
  base64 → "4vxvthis_is_base64_flag"
  ...check flag pattern: NAME{...}
🚩 found: flag{...}
```

### Classic crypto
```
Operator: caesar bruteforce "Frperg Zrffntr"
Operator: xor single byte find the key for this hex: 1c0111001f...
```
26 shifts / 256 keys at once, ranked by englishness.

### Hash & misc
```
Operator: what hash type is this: 5f4dcc3b5aa765d61d8327deb882cf99
```
```
[HASH-ID] length 32 hex → candidates: MD5, NTLM, MD4
```

Recon for other categories (web/pwn/forensics) → sk32 points to the tooling + delegates to sk11 (audit) / sk6 (httpx, in-scope). Want a writeup PDF auto-generated for every flag found? combo sk32 + sk8.

---

## CTF Swarm full-auto (sk32 → sk43–sk48) — v7.0 update

A level up from the passive toolkit: a **full-auto whitehat CTF framework** in `framework/ctf/`. sk32 becomes the orchestrator that triages → checks scope → dispatches to the category sub-skill → validates the flag → submits. Good for CTFd events with many challenges at once.

### Category sub-skills (picked automatically by sk32)
| Challenge | Skill |
|---|---|
| web app / URL / HTTP | **sk43** (SQLi, SSTI, SSRF, IDOR, JWT, deserialization) |
| binary + `nc host port` | **sk44** (ret2win, ret2libc, format string, heap, ROP) |
| binary "what does it do" | **sk45** (angr, Ghidra, radare2, keygen) |
| ciphertext / RSA / key | **sk46** (RSA attacks, block cipher, PRNG — `rsa_attacks.py`) |
| pcap / memory / image / zip | **sk47** (volatility, binwalk, stego, carving) |
| LLM / AI / jailbreak / Gandalf | **sk48** (prompt-injection / LLM red-team) |

### Mode 1 — manual per challenge (safe, default)
```
Operator: this is a web challenge, target https://chal.ctf.example/01, there is a login form
```
sk32 confirms the scope (see `scope.json`) → loads sk43 → hands over the playbook + recon script. A found flag **must** pass `flag_validator.py`, then you approve the submit.

### Mode 2 — full-auto swarm (many challenges, needs setup)
```bash
cd framework/ctf
cp .env.example .env            # fill CTFD_URL, CTFD_TOKEN, per-provider API key, MODELS (the real IDs!)
cp scope.example.json scope.json # set the hosts that MAY be attacked (this event only)
docker build -f sandbox/Dockerfile.sandbox -t ctf-sandbox .

python3 run.py          # poll CTFd → race models per challenge in the sandbox → solve
python3 run.py status   # see progress per challenge
python3 run.py approve  # submit the queued flags (if HITL_SUBMIT=true)
```
Every challenge races several models in parallel inside an **isolated Docker sandbox** (default `--network none`). The model lineup is free across providers — the **Anthropic, OpenAI, Gemini** adapters are complete (`MODELS=anthropic:...,openai:...,gemini:...`, fill the API key of the providers you use). The first valid flag wins; in unattended mode it takes `AUTO_SUBMIT_CONSENSUS` models agreeing before an auto-submit.

### Mode 3 — LLM red-team / Gandalf (sk48)
For AI/LLM challenges (Gandalf-style: squeeze the password out of the LLM without tripping the guard). The solver is **host-locked to gandalf.lakera.ai** (rejects other hosts).
```bash
cd framework/ctf
python3 gandalf_solver.py --start 1 --end 7      # static: try the strategy ladder per level
python3 gandalf_solver.py --adaptive --model anthropic:claude-opus-4-1   # attacker-LLM (also openai:.../gemini:..., fill the API key)
```
The idea: the input guard inspects *your* prompt (counter: paraphrase the intent), the output guard inspects the *model's* answer (counter: never emit the literal secret → encode/acrostic/spell it). Technique details & the L1–L8 defense ladder are in `skills/ctf/ctf-playbook/sk48.md`. ⚠️ The Gandalf API contract is unofficial — verify in DevTools before running.

### Safeguards (why this stays whitehat)
- **`scope_guard.py`** — only allowlisted hosts may be touched; deny rules win. Out-of-scope = rejected.
- **Sandbox** — challenge binaries only run inside Docker, no network by default.
- **`flag_validator.py`** — a flag must full-match + pass the placeholder blocklist; flags are taken from the target output, **never invented**.
- **HITL by default** — `HITL_SUBMIT=true` → the flag waits for your approval. In line with sk32 gate R9.

Technical detail: `framework/ctf/README.md`. Review notes on the original package: `REVIEW.md`.

---

## Rug & legitimacy check — NEW in v7.0

One command → a clear verdict. Raw signals (honeypot/tax/verification/holders/LP) come from H4 + sk10, `rugcheck` turns them into a decision + shows what is *not yet* checked (never ignored).
```
Operator: rugcheck token 0xToken... di base
```
```
[RUGCHECK] 0xToken... on base  →  ⚠️ CAUTION
🛑 critical:  (none)
⚠️ warnings:  sell-tax 9%, owner not renounced, LP locked only 30 days
✅ ok:        contract verified, not a honeypot, top10 holders 28%
❓ unknown:   contract age not checked → have sk10 fill it first
verdict: small entry allowed, do not go all-in. Re-check after the LP lock & renounce.
```
Verdict: **SAFE / CAUTION / DANGER**. Also good material for AirdropFinder educational content ("how to read rug signals").

---

## New observability & safety — v7.0

Mostly automatic behind the scenes, but you can call it:

| Command | Effect |
|---|---|
| `cost report` | Central cost ledger: LLM tokens + on-chain gas (USD) + API calls, breakdown per provider/chain |
| `router log` / `router tune` | See router decisions + *tie* detection (keyword collision) + weight retune advice |
| `dry-run on` / `off` | Global simulation — the `plan()` engine, not broadcast (already existed, now uses contextvars, tidier) |
| `regression run <suite>` | Golden-set regression: compare current output vs baseline → know if an upgrade broke something |

Plus what runs automatically:
- **Secret tripwire** — at the output layer, redacts priv keys / mnemonics / API keys / JWT / PEM before print/log. CTF flags may still show; real irrelevant secrets stay redacted.
- **Cost ledger** — every operation records its cost, so `cost report` is always accurate.

---

## Alpha & farming intelligence (sk33 · sk34 · sk36) — v7.0 update

Three new modules so your farming is number-backed end to end: find projects earlier → compute ROI → know when to exit. All offline & deterministic; raw data is pulled by sk10/sk22/hermes first.

### Alpha radar (sk33) — find airdrops BEFORE they are announced
```
Operator: scan pre-TGE projects worth farming on Base
```
```
[ALPHA RADAR] 3 candidates
📡 ZkProtoX  78/100 (HOT)   · points program ✅ · testnet ✅ · tier-1 VC · effort high
📡 BaseThing 52/100 (WARM)  · active governance without a token · raised $12M
📡 OldChain   8/100 (COLD)  · token already exists → the main airdrop window passed
advice: start ZkProtoX this week, watch BaseThing first
```
Token already listed? The score is auto-capped at 30 — do not burn gas.

### Farm ROI (sk34) — continue, trim, or drop?
```
Operator: compute the ROI of all my farming positions
```
```
[FARM ROI] 4 positions · EV $3.2k − cost $410 = net $2.79k
💼 LayerZero  EV $1.2k · ROI 9.0x → KEEP
💼 ZkProtoX   EV $1.8k · ROI 6.2x → KEEP
💼 BridgeFarm EV $150  · ROI 0.4x → TRIM (gas already too large)
💼 DeadFarm   net -$75 → DROP ⚠️ idle 60 days — passive wallets get culled
```

### Unlock pressure (sk36) — macro supply before you get trapped in a dump
```
Operator: unlock calendar $ZK for the next 6 months, worth holding?
```
```
[UNLOCK CALENDAR] $ZK
🔓 Investor cliff  T-10h  · $160M (40% circ) · pressure EXTREME (32x volume)
   ⚠️ large sell pressure <2 weeks — consider trimming the position FIRST
🔓 Team linear     T-120h · $40M (10% circ) · pressure HIGH — flag it, prepare an exit
```
`now` is always injected (TIME.md). The actual sell still goes through the sk31 exit planner + the Spend Governor.

---

## Community protection (sk37 · sk38) — v7.0 update

Two **read-only** defensive modules — they keep AirdropFinder members away from drainers. No attacking, no exploiting; in line with the whitehat principle.

### Anti-scam sentinel (sk37) — is this site real or an imitation?
```
Operator: cek zkprot0x.xyz, resminya zkprotox.xyz
```
```
[SCAM SENTINEL] zkprot0x.xyz → 🚨 LIKELY-SCAM (100/100)
• typosquat: 1 letter off the official domain
• 🚩 asks for a SEED PHRASE — the official site NEVER does
• SSL 3 days old + a claim button
draft warning post is ready — review before broadcasting (a false positive = defamation)
```

### Contract watcher (sk38) — is claiming safe?
The most common drainer trick: the contract/claim address is swapped quietly during claim hype. The snapshot is taken at H9/sk10, sk38 does the diff.
```
Operator: has the ZkProtoX claim contract changed since yesterday? safe to claim?
```
```
[CONTRACT WATCH] 0xAbc... → 🚨 CRITICAL
🚨 claim address changed 0xC1... → 0xEVIL... — DO NOT claim until official verification
🚨 new sensitive function: setClaimAddress
safe_to_claim: FALSE → every claim job is held
```
`safe_to_claim = FALSE` → the claim runner holds automatically. No exceptions.

---

## Content & community engine (sk35 · sk39–sk42) — v7.0 update

The AirdropFinder content pipeline end to end: listen to the community → build a guide → repurpose to every platform → video → best hook.

### Auto guide studio (sk35) — 1 airdrop becomes a clean guide
```
Operator: make a full ZkProtoX guide + telegram & X versions, embed my referral
```
```
[GUIDE STUDIO] ZkProtoX (Base)
✅ full guide Markdown ID (header, preparation, 6 steps, DYOR disclaimer)
✅ Telegram variant + X variant (≤280)
✅ referral embedded in every variant
🖼️ 4 screenshot jobs → delegate to the browser skill
gate: sk37 scans the domain before publish — do not promote a scam
```

### Community intelligence (sk39) — what the community said overnight
```
Operator: analisis chat grup 24 jam terakhir
```
```
[COMMUNITY INTEL] 1.840 messages (24h) · neutral sentiment (+0.05)
 topics: zkprotox(214), claim(180), gas base(95)
❓ most frequent: "when does the ZkProtoX claim open min?" (38x)
🚨 FUD: 12 messages "not paid out / scam" → fact-check (sk37/sk38) first, clarify after
💡 idea: ZkProtoX claim FAQ thread, Base gas education
```

### Omni-repurpose (sk40) + video pipeline (sk41) + hook lab (sk42)
```
Operator: turn this article into an X thread, TG post, IG carousel, tiktok & youtube script
Operator: make a 45 second video package about 3 Base airdrops
Operator: give 8 hook variants for this content, ranked
```
```
[REPURPOSE] 5 formats ✅ — 6-tweet thread (all ≤280) · TG · 5 IG slides · tiktok 36s · YT 6 min
[VIDEO PIPELINE] 45s · hook 6.8s → 3 points → CTA · 5-shot storyboard · ID voiceover · .srt subtitles
[HOOK LAB] top-3:
  [76] 3 Base airdrops you have to know right now    (numbers, urgency)
  [70] The Base airdrop secret that prints money     (curiosity, emotion)
  [64] Do not farm Base before watching this 👀      (emotion, urgency)
```
Video render = the `remotion_video` skill; TTS = `voice.py`. Hook scores are heuristic predictions, not a viral guarantee — feed actual performance back so they get sharper.

---

## Session control commands

Just talk to Hermes directly, no special syntax:

| Command | Effect |
|---|---|
| `auto_confirm on` | Fast mode — skip the per-tx gate |
| `auto_confirm off` | Safe mode (default) |
| `status` | See every active background job |
| `stop <jobname>` | Kill a background job (sniper, farming, watcher) |
| `resume <jobname>` | Resume a paused job |
| `audit` | Trigger sk52 — system self-check |
| `debug` | Trigger sk54 — when something errors/breaks |
| `upgrade brain` | Trigger sk52 deep review (skill coverage, gap, redundancy analysis) |
| `dry-run on` | Every tx becomes simulate-only, no broadcast (for testing) |
| `dry-run off` | Back to broadcast mode |
| `wallet list` | See every wallet in the vault |
| `balance <wallet>` | See a wallet's multi-chain balance |
| `revoke approval <spender> di <wallet>` | Revoke an ERC-20/721 approval |
| `cost report` | **v7.0** — central costs: tokens + gas (USD) + API, per provider/chain |
| `router log` / `router tune` | **v7.0** — router decision log + tie detection + retune advice |
| `regression run <suite>` | **v7.0** — cross-release golden-set regression |
| `skor eligibility <wallet> buat <proyek>` | **v7.0 (sk31)** — 0-100 score + gaps + flags |
| `sybil audit <N wallet>` | **v7.0 (sk31)** — check your own cross-wallet correlation |
| `airdrop calendar` / `claim window this week` | **v7.0 (sk31)** — D-48/D-2/D-0 alerts |
| `exit plan <amount> <token>` | **v7.0 (sk31)** — exit ladder, via governor |
| `rugcheck <token> di <chain>` | **v7.0** — SAFE/CAUTION/DANGER verdict |
| `triage soal CTF ...` / `decode ...` | **v7.0 (sk32)** — whitehat, in-scope only |
| `scan proyek pre-TGE di <chain>` | **v7.0 (sk33)** — alpha radar, score + tier |
| `hitung ROI posisi farming` | **v7.0 (sk34)** — EV/ROI, keep/trim/drop |
| `make a guide for <project>` | **v7.0 (sk35)** — full guide + TG/X variants + referral |
| `kalender unlock <token>` | **v7.0 (sk36)** — sell pressure per event |
| `cek domain <situs> resminya <situs>` | **v7.0 (sk37)** — typosquat + drainer signals |
| `did <project> contract change? safe to claim?` | **v7.0 (sk38)** — diff + safe_to_claim gate |
| `analisis chat grup <window>` | **v7.0 (sk39)** — topics, FUD, sentiment, ideas |
| `repurpose this content to every platform` | **v7.0 (sk40)** — X/TG/IG/TikTok/YT |
| `make a video package <duration> about <topic>` | **v7.0 (sk41)** — script+storyboard+SRT |
| `kasih varian hook + ranking` | **v7.0 (sk42)** — 0-100 stop-scroll score |

### Per-wallet alias
```
Operator: rename wallet 0xAbC...d4F1 jadi "farming-base-1"
Operator: swap 100 USDC using farming-base-1
```

Hermes uses the alias from the next session on.

---

## Background job persistence

Sniper, farming, watcher — all run in the background via pm2. They survive a reboot if you use systemd.

### See active jobs
```bash
pm2 ls
```

Sample output:
```
┌─────┬────────────────────┬─────────────┬──────┬─────────┐
│ id  │ name               │ status      │ cpu  │ memory  │
├─────┼────────────────────┼─────────────┼──────┼─────────┤
│ 0   │ hermes (main)      │ online      │ 2%   │ 142 MB  │
│ 1   │ lz-farming         │ online      │ 0.5% │ 48 MB   │
│ 2   │ sniper-base        │ online      │ 1%   │ 36 MB   │
│ 3   │ anti-drainer       │ online      │ 0.3% │ 22 MB   │
│ 4   │ smart-money-watch  │ online      │ 0.4% │ 28 MB   │
└─────┴────────────────────┴─────────────┴──────┴─────────┘
```

### Logs per job
```bash
pm2 logs sniper-base --lines 50
pm2 logs lz-farming -f          # follow real-time
```

### Restart / stop
```bash
pm2 restart sniper-base
pm2 stop lz-farming
pm2 delete anti-drainer         # remove from the list
```

### Auto-start on VPS reboot
```bash
pm2 save                        # save current state
pm2 startup systemd             # generate the systemd unit
# follow the printed instructions
```

---

## Cheat sheet — natural language to skill route

Quick table: what you say → which skill fires.

| You say | Route | File loaded |
|---|---|---|
| "mint NFT [URL]" | sk13 | `skills/sk13.md` |
| "mass mint with N wallets" | sk13 + sk12 + sk10 | mint + batch + Web3 |
| "swap X to Y on [chain]" | H1 | `hermes/references/swap.md` |
| "sell all $TOKEN" | H1 | swap.md |
| "bridge from A to B" | H2 | `hermes/references/bridge.md` |
| "stake ETH on lido" | H3 | `hermes/references/defi.md` |
| "supply USDC to aave" | H3 | defi.md |
| "open long ETH on GMX" | H3 | defi.md (perp section) |
| "snipe a new token on [chain]" | H4 + sk10 | sniping.md + Web3 |
| "snipe NFT mint [URL]" | H4 + sk13 | sniping + minter |
| "watch wallet [addr]" | H5 | `hermes/references/monitoring.md` |
| "alert if a whale buys > $X" | H5 + sk4 | monitoring + TG bot |
| "mempool watch [wallet]" | H5 | monitoring (sniffer section) |
| "smart money tracker" | H5 | monitoring (Nansen/Arkham) |
| "buy NFT [token] on [marketplace]" | H6 | `hermes/references/nft.md` |
| "list my NFT for sale" | H6 | nft.md |
| "floor sweep [collection]" | H6 | nft.md (Reservoir) |
| "sign in to a dApp with SIWE" | H7 | `hermes/references/web3_connect.md` |
| "resolve ENS [name].eth" | H7 | web3_connect.md |
| "layerzero farming N wallets" | H2 + H1 + sk12 | bridge + swap + batch |
| "zksync / linea farming" | H2 + H1 + sk12 | same pattern |
| "create a new wallet on [chain]" | sk10 / hermes/wallets.md | depends on the chain |
| "import a wallet from a seed" | hermes/wallets.md | (security strict mode) |
| "audit contract [addr]" | sk11 | `skills/sk11.md` |
| "why is my bot duplicating" | sk54 + sk4 | debug + telegram |
| "deploy to a VPS" | sk2 | `skills/sk2.md` |
| "build a web3 landing page" | sk9 + sk10 | frontend + Web3 connect |
| "make an explainer animation / diagram" | sk18 | `skills/sk18.md` (Manim/Excalidraw) |
| "make an image with comfyui" | sk18 | sk18 + `scene_prep.py` |
| "control Notes/Safari on my Mac" | sk19 | sk19 + `desktop_control.py` (no cursor steal) |
| "train a robot in Isaac Sim" | sk19 | sk19 + `scene_prep.py` |
| "make my writing not sound like AI" | sk20 | sk20 + `humanizer.py` |
| "block the IPs attacking from the log" | sk21 | sk21 + `hids.py` |
| "investigate an error with KQL" | sk21 + sk57 | sk21 + systematic debug |
| "deep research on X + sources" | sk22 | sk22 + `research_q.py` |
| "break this task down, I'm overwhelmed" | sk23 | `skills/sk23.md` |
| "build an MCP server" | sk24 | sk24 + `mcp_builder.py` |
| "check my prompt for problems" | sk24 | sk24 (`audit_prompt`) |
| "review compliance / CI-CD / port a codebase" | sk25 | `skills/sk25.md` |
| "turn this conversation into a PRD / issues" | sk26 | sk26 + `prd.py` |
| "grill my idea until it is concrete" | sk26 + sk58 | shaping → spec |
| "eval / variance test this feature" | sk56 | sk56 + `eval.py` |
| "debug a weird bug that shows up sometimes" | sk57 | `skills/sk57.md` (4-phase + variance) |
| "my goal is still vague, help me sharpen it" | sk58 | `skills/sk58.md` |
| "build a 30-day content calendar" | sk27 | sk27 + `content.py` |
| "adapt this post to X/LinkedIn/IG/TikTok" | sk27 | sk27 (`adapt`) |
| "write a thread / carousel / reels script" | sk27 | sk27 + `content.py` |
| "write IG caption + hashtags" | sk27 | sk27 (`caption`/`hashtags`) |
| "write with the AIDA/PAS framework" | sk28 | `skills/sk28.md` |
| "write an SEO-friendly blog" | sk28 | sk28 (SEO writer) |
| "localize content into another language" | sk28 | sk28 (localization/RTL) |
| "research trends & competitors in my niche" | sk29 | sk29 (+ sk22 for depth) |
| "analyze comments / post performance" | sk29 | sk29 + `content.py` (needs real data) |
| "1 article into thread+carousel+reels" | sk29 | sk29 (`repurpose`) |
| "full automatic content pipeline" | sk29 + sk4/sk17 | research→draft→visual→schedule→analyze |
| "scientific research genomics/forecasting" | sk22 | dispatch to the library (scanpy/prophet/etc.) |
| "robot sees & picks an object (VLA)" | sk19 | sk19 (VLA, sim first) |
| "score wallet eligibility for [project]" | sk31 | `skills/sk31.md` + `eligibility.py` |
| "sybil audit my N farm wallets" | sk31 | sk31 + `sybil_audit.py` |
| "airdrop calendar / claim window" | sk31 | sk31 + `claim_watcher.py` |
| "exit plan / when to sell [token]" | sk31 | sk31 + `exit_planner.py` |
| "rugcheck / is this token safe" | sk11 + H4 + sk10 | `rugcheck.py` (verdict) |
| "triage a CTF challenge / decode a flag" | sk32 | `skills/sk32.md` + `ctf.py` |
| "caesar / xor / what hash type" | sk32 | sk32 + `ctf.py` |
| "solve a CTF web (SQLi/SSTI/JWT)" | sk32 → sk43 | `skills/ctf/ctf-playbook/sk43.md` + `framework/ctf/` |
| "pwn a binary / ret2libc / heap" | sk32 → sk44 | `skills/ctf/ctf-playbook/sk44.md` + pwntools template |
| "reverse a binary / angr / keygen" | sk32 → sk45 | `skills/ctf/ctf-playbook/sk45.md` + angr template |
| "RSA attack / crypto challenge" | sk32 → sk46 | `skills/ctf/ctf-playbook/sk46.md` + `framework/ctf/rsa_attacks.py` |
| "forensics / stego / pcap / memdump" | sk32 → sk47 | `skills/ctf/ctf-playbook/sk47.md` + sandbox tools |
| "prompt injection / jailbreak / Gandalf" | sk32 → sk48 | `skills/ctf/ctf-playbook/sk48.md` + `framework/ctf/gandalf_solver.py` |
| "full-auto solve CTFd (swarm)" | sk32 | `framework/ctf/run.py` (coordinator + sandbox) |
| "scan pre-TGE projects / alpha airdrop" | sk33 | `skills/sk33.md` + `alpha_radar.py` |
| "farming ROI / which farm to drop" | sk34 | sk34 + `farm_roi.py` |
| "build an airdrop guide [project]" | sk35 | sk35 + `guide_studio.py` (+browser for SS) |
| "unlock calendar / sell pressure [token]" | sk36 | sk36 + `unlock_engine.py` |
| "is this site fake / check a domain" | sk37 | sk37 + `scam_sentinel.py` |
| "did the contract change / is claiming safe?" | sk38 | sk38 + `contract_watch.py` (+H9 snapshot) |
| "what is hot in the group / FUD" | sk39 | sk39 + `community_intel.py` (+sk4 pulls messages) |
| "repurpose to X/TG/IG/TikTok/YT" | sk40 | sk40 + `repurpose.py` |
| "build a video package / storyboard / srt" | sk41 | sk41 + `video_pipeline.py` |
| "hook variants / title predictions" | sk42 | sk42 + `hook_lab.py` |
| "cost / cost report for this session" | core | `cost_ledger.py` |
| "router collision / tune keywords" | core | `router_log.py` |
| "regression test across releases" | sk56 | `eval.py` (RegressionSuite) |

---

## v7.0 skills — example commands (Airdrop Intelligence & Whitehat)

Net-new in v7.0. Every tool is offline+deterministic; on-chain data is delegated to sk10/hermes; fund movement goes through the Spend Governor.

### Airdrop Intelligence (sk31)
```
Operator: skor eligibility wallet#1 buat Linea, kasih gap & saran
Operator: sybil audit my 50 farm wallets, which ones are at risk
Operator: which airdrops have a claim window this week, alert H-48/H-2/H-0
Operator: exit plan 5000 $ZK profil balanced, likuiditas tipis
```

### CTF / Whitehat (sk32) — legal & in-scope only
```
Operator: triage this CTF challenge: [description]
Operator: decode berlapis: [blob base64/hex]
Operator: caesar bruteforce "[ciphertext]"
Operator: what hash type is this: [hash]
```
Foreign / out-of-scope target → gate R9 first (⚠️ permission? y/n). Active exploit = manual + permission.

### Safety & observability
```
Operator: cost report this session  → token + gas + API breakdown
Operator: rugcheck 0xToken... di base → SAFE/CAUTION/DANGER verdict
Operator: regression run mint-detector → check if anything broke after the upgrade
```

---

## Non-crypto skills (v7.0) — example commands

Everything below is an **optional module**. The core identity stays crypto+dev — these skills only wake up when you mention them. They do not touch funds, so there is no governor gate (except OS/desktop/physical-robot actions & firewall → one R9 gate).

### Media & creative (sk18)
```
Operator: make a Manim animation explaining gradient descent
Operator: generate 10 image variations with comfyui, different seeds
Operator: draw my system architecture diagram in excalidraw
Operator: make an OG card 1200x630 for this article
```
Output = artefact files (MP4/PNG/SVG). Needs a local engine (ffmpeg/Manim/ComfyUI) — deploy via sk2 if on a VPS.

### Desktop & robotics (sk19)
```
Operator: write this to my Notes          → app-drive, your cursor is NOT stolen
Operator: latih grasp robot di Isaac Sim, 200 step headless
```
macOS control = background-first (no cursor steal). Physical robot / destructive desktop action → one R9 gate.

### Humanizer (sk20)
```
Operator: this writing is stiff, make it natural   → strip the AI-tell
Operator: tune ke brand voice "ct_degen"
```

### Enterprise & defensive (sk21)
```
Operator: pantau auth.log, auto-block IP brute-force SSH (dry-run dulu)
Operator: tulis KQL buat cari spike latency 6 jam terakhir
```
HIDS always allowlists your IP + TTL blocks (never a permaban). Firewall activation → R9 gate.

### Research, focus, product (sk22/sk23/sk26)
```
Operator: riset mendalam dampak EIP-4844 ke L2, kasih sumber
Operator: I'm overwhelmed, break this task down one by one, give me only the first
Operator: from that chat, write a PRD + break it down into issues
```

### Meta-dev & quality (sk24/sk25/sk56/sk57/sk58)
```
Operator: scaffold MCP server "weather" di Python
Operator: audit this system prompt, what is wrong with it
Operator: variance test the mint-detector function 10x, is it stable
Operator: this bug shows up sometimes — debug it systematically
Operator: the goal "profit from web3" is still vague, help me shape it
```

### Content & social media (sk27/sk28/sk29)
A full marketing suite. The core identity stays crypto+dev — this is an optional module for making & spreading content.
```
Operator: build a content strategy: pillars, audience, positioning for my account
Operator: make a 30 day content calendar, 5 posts/week, X + IG
Operator: adapt this message to an X thread, LinkedIn, IG carousel, and reels script
Operator: write 5 scroll-stopper hooks for topic [X]
Operator: rewrite with the PAS framework, then humanize (sk20) so it does not smell like AI
Operator: repurpose this 1 article into a thread + carousel + reels
Operator: riset tren & kompetitor di niche [X], kasih peluang konten
Operator: analyze these comments — sentiment, questions, objections
Operator: make 3 A/B variants for this caption (change the hook only)
Operator: jalanin full pipeline: research → draft → visual → schedule → analyze
```
Honest notes:
- **Analytics & best-time need real data** from your account (export/API). Without it → estimates marked as such, not invented numbers.
- **Publishing & replying to comments = outbound actions** → human-in-the-loop by default (draft → you approve → send). Sensitive replies are never auto-sent.
- Winning flow: sk29 (research) → sk28 (copy) → sk27 (format) → sk20 (humanize) → sk18 (visual) → sk4/sk17 (schedule).

### Research & robotics (sk22/sk19)
```
Operator: deep research [scientific topic], dispatch to the right library + sources
Operator: cari dataset/model di Hugging Face buat [task]
Operator: robot di Isaac Sim lihat botol merah terus ambil (VLA, latih di sim dulu)
```
Physical robot / real VLA = R9 gate + the STOP meta-action always wins. Science = dispatch to validated libraries + verification, never invented results.

---

## What to prepare before starting

1. **VPS access** — ✅ already have `root@vmi3159875`
2. **Vault master password** — create it now, minimum 16 chars, store it in a password manager
3. **Primary + fallback RPC per chain** — minimum 2 endpoints per chain (rotating so you do not get rate-limited). Recommended: Alchemy / Infura / QuickNode + 1 public RPC as fallback
4. **A small test wallet first** — generate a new wallet via Hermes, fund it with $20-50 for a smoke test, do not start on the main wallet
5. **A new Telegram bot for alerts** — create it via @BotFather, put the token in `HERMES_TG_BOT_TOKEN`. Do not reuse the bot behind your public channel
6. **Optional API keys** — skip them for now if missing, Hermes auto-falls back:
   - 1inch (swap): free tier OK
   - Reservoir (NFT): free tier OK
   - Nansen (smart money): paid, most accurate — optional
   - Arkham: free tier OK
   - Zerion / Birdeye (portfolio): free tier OK

Once these 6 are ready → Hermes can run immediately. Want me to build the automatic **bootstrap script** (install + env setup + first wallet gen + smoke test), or do you prefer manual step-by-step setup?

---

## Quick verification that v7.0 + hermes is running

After install + restart, check 5 things:

```bash
# 1. Agent boots without errors
pm2 logs hermes --lines 20
# must show: [BOOT] v7.0 SYADAGENTIC SUPREME loaded

# 2. Env vars load
env | grep -E "HERMES_|RPC_|ARKHAM_" | head -10

# 3. Skills are readable (now sk1-sk32 + sk52-sk58)
ls ~/.openclaw/workspace/openclaw/skills/
# must see: sk0-sk32, sk52-sk58, hermes/

# 4. Integrity OK (IMPORTANT — boot rail)
python3 scripts/skill_integrity.py verify
# must be: "✅ Integrity OK — 150 files match" (exit 0)

# 5. Offline tests green (zero leak)
python3 tests/run_tests.py           # 85 tests OK
bash skills/hermes/tests/run_tests.sh   # 44 tests OK
# total 129 pass, 0 ResourceWarning under -W error::ResourceWarning
```

If all 5 above are ✅, SYADAGENTIC v7.0 is ready to execute.

> Note: after every edit/add of a `.md` or `.py` file, run `python3 scripts/skill_integrity.py generate` then `verify`. A failed verify (exit≠0) = the boot rail holds on-chain operations until it is audited.
