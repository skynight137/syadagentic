# Skills catalog

One folder per skill: `skills/<category>/<name>/SKILL.md`. Load by name; `name:` equals the folder.
Layout is enforced by `tests/check_skills.py` (CI).

## affiliate

- **threads-auto-post** — Threads affiliate auto-post: v19 — Browserless HTTP primary + Shopee buyer-review 5★+media HD + Pinterest fallback + 1-post=1-link forever. Content CERITA/TIPS Viewbait v5: post_1 first line ALL CAPS + total ≥210 chars …
- **threads-auto-reply** — Threads affiliate auto-reply. v10 stealth: 9router LLM + burst-rest scheduler + sleep window + log-normal delay …

## automation

- **arsenal-automation** — Automation playbooks from the SYADAGENTIC arsenal: Telegram bot in production (sk4), IFTTT-style API bridge (sk6), batch runner (sk12), task planner + swarm (sk17). Use when wiring cron, webhooks, n8n, or multi-agent orchestration.

## captcha

- **captcha-solver** — Universal local sidecar anti-bot & captcha solver (Cloudflare Turnstile, Aliyun 2.0, Arkose FunCaptcha, Akamai, BotGuard, PerimeterX, DataDome, AWS WAF, reCAPTCHA, hCaptcha).

## content

- **content-playbook** — Content creation and copywriting playbooks: m3 creation/strategy/social (merged m27) and m28 copywriting/content research (merged m29). Use for writing, humanizing, content strategy, social scheduling.

## ctf

- **ctf-playbook** — CTF playbooks per discipline: web (m43), pwn (m44), reversing (m45), crypto (m46), forensics (m47), LLM red-team extraction (m48) plus sk43-48 quick refs. Use when solving or authoring CTF challenges.

## devops

- **hermes-guardrail-bypass** — Neutralize Hermes' non-model security scanners (context-file injection blocks, MCP output risk escalation, skill-install guard) and repair the patches after every hermes update.

## engineering

- **engineering-playbook** — Engineering playbooks: AI builder (sk7), MCP servers (sk24), data pipelines (sk5), file handling (sk8), interfaces (sk9), plus sk2/sk23/sk25/sk26. Use for build/debug work outside a single-file patch.

## intelligence

- **intelligence-playbook** — Research and reflection playbooks: skill registry (m0), research pipeline (sk22), signal monitoring (sk29). Use when the task is discovery rather than execution.

## meta

- **meta-playbook** — Self-audit and self-improvement playbooks: sk0 baseline, sk52-58 reflection/problem shaping, x1-x7 improvement loops, merged notes m27/m29. Use when auditing or upgrading the agent itself.

## monetization

- **monetization-playbook** — Revenue playbooks: sk1 value generation/pricing and sk50 funnel. Use when the task is commercial: pricing, offers, income paths.

## security

- **api-fuzzing-bug-bounty** — Provide comprehensive techniques for testing REST, SOAP, and GraphQL APIs during bug bounty hunting and penetration testing engagements. Covers vulnerability discovery, authentication bypass, IDOR exploitation, and API-specific attack vectors.
- **attack-chain-web2** — Web2 attack chain plugin — apply Web2 trust boundaries and composition rules on top of attack-chaining-core for authorized testing of web apps, APIs, identity, cloud, and internal services.
- **attack-chain-web3** — Web3 attack chain plugin — apply Web3 state, economic, cryptographic, and consensus semantics on top of attack-chaining-core for authorized testing of smart contracts, DeFi, bridges, wallets, and validators.
- **attack-chaining-core** — Domain-neutral attack chain analysis — determine whether independently identified security primitives compose into a realistic, authorized, evidence-backed attack path with greater impact.
- **attack-surface-mapper** — Build an evidence-backed map of externally and internally reachable attack surfaces, trust boundaries, privileged transitions, security assets, and high-value audit targets before vulnerability hunting.
- **bb-methodology** — Use at the START of any bug bounty hunting session, when switching targets, or when feeling lost about what to do next …
- **bug-bounty** — THE master bug bounty hunting skill — hasil merge arsenal 69 skill (bughunter-os, webhunter-os, open-kritt, ghost-scan, dll) + SYADAGENTIC-bugbounty v7.1 + submission review gate …
- **bug-bounty-disclosure** — End-to-end skill for authorized/good-faith bug bounty and coordinated vulnerability disclosure to the developer or project owner — for EVERY bug class (web, API, infra, mobile, cloud, smart contract/web3, agent/LLM), crypto maupun non-crypto …
- **bug-bounty-workflow** — Complete bug bounty workflow — recon (subdomain enumeration, asset discovery, fingerprinting, HackerOne scope, source code audit), pre-hunt learning (disclosed reports, tech stack research, mind maps, threat modeling), vulnerability hunting (IDOR …
- **bughunter-os** — Complete bug bounty hunting & smart contract audit operating system. 8-phase methodology + 5 knowledge bases (attack patterns, real-world exploits, protocol playbooks, orchestrator) covering 340+ files …
- **burp-suite-testing** — Execute comprehensive web application security testing using Burp Suite's integrated toolset, including HTTP traffic interception and modification, request analysis and replay, automated vulnerability scanning, and manual testing workflows.
- **cicd-security** — CI/CD pipeline security hunting — GitHub Actions workflow injection, secret exfiltration, self-hosted runner poisoning, dependency confusion, OIDC token theft, and supply chain attacks …
- **code-injection-detector** — Code Injection Detector - Auto-activating skill for Security Fundamentals. Triggers on: code injection detector, code injection detector Part of the Security Fundamentals skill category.
- **cosmos-sdk-chain-audit** — Smart contract security audit — 11 DeFi bug classes (accounting desync, access control, incomplete path, off-by-one, oracle, ERC4626, reentrancy, flash loan, signature replay, proxy, BFT/consensus/liveness), pre-dive kill signals (TVL < $500K etc) …
- **credential-attack** — Password spray methodology for bug bounty — when to do it vs web-vuln hunting, the wordlist-gen + breach-check + osint-employees + spray pipeline, mode selection (http-form / oauth / o365 / okta), rate-limit + lockout tactics, BBP legal guardrails …
- **encrypting-and-decrypting-data** — Validate encryption implementations and cryptographic practices. Use when reviewing data security measures. Trigger with 'check encryption', 'validate crypto', or 'review security keys'.
- **entry-point-analyzer** — Analyzes smart contract codebases to identify state-changing entry points for security auditing …
- **ethical-hacking-methodology** — Master the complete penetration testing lifecycle from reconnaissance through reporting …
- **evidence-packager** — Assemble a reproducible, minimal, tamper-evident evidence bundle for a security finding, preserving provenance and separating observed facts from interpretation.
- **exploitability-analyzer** — Adversarially assess whether a verified bug primitive can be exercised by a realistic attacker in production and produce the claimed security impact with measurable reliability.
- **forensics-data-collector** — Forensics Data Collector - Auto-activating skill for Security Advanced. Triggers on: forensics data collector, forensics data collector Part of the Security Advanced skill category.
- **ghost-scan-code** — Ghost Security - SAST code scanner. Finds security vulnerabilities in source code by planning and executing targeted scans for issues like SQL injection, XSS, BOLA, BFLA, SSRF, and other OWASP categories …
- **graphql-audit** — GraphQL security hunting — introspection abuse, field suggestion enumeration (clairvoyance), batching DoS, IDOR via aliasing, auth bypass, injection via arguments, subscription abuse, depth/complexity bombs, and WAF bypass …
- **guidelines-advisor** — Smart contract development advisor based on Trail of Bits' best practices …
- **html-injection-testing** — Identify and exploit HTML injection vulnerabilities that allow attackers to inject malicious HTML content into web applications …
- **http2-specific-attacks** — HTTP/2 protocol-specific attack playbook. Use when the target supports HTTP/2 and you need to exploit binary framing, HPACK compression, h2c upgrade smuggling, pseudo-header injection, stream multiplexing abuse, or H2→H1 downgrade translation flaws.
- **linux-privilege-escalation** — Execute systematic privilege escalation assessments on Linux systems to identify and exploit misconfigurations, vulnerable services, and security weaknesses that allow elevation from low-privilege user access to root-level control.
- **malware-analyst** — Expert malware analyst specializing in defensive malware research, threat intelligence, and incident response. Masters sandbox analysis, behavioral analysis, and malware family identification.
- **meme-coin-audit** — Meme coin and token security audit — rug pull detection (honeypot, hidden mint, fee manipulation, LP lock bypass), Solana SPL token analysis (freeze authority, mint authority, metadata mutability), Token-2022 extension risks (transfer hooks …
- **memory-forensics** — Comprehensive techniques for acquiring, analyzing, and extracting artifacts from memory dumps for incident response and malware analysis.
- **mobile-pentest** — Mobile app pentest for bug bounty (Android APK + iOS IPA) — runtime-first workflow: install app, proxy through Burp/mitmproxy, drive the UI, capture packets, then test the API exactly like a web target …
- **open-kritt** — Drive a **locally-running open-kritt stack** (github.com/Kritt-ai/open-kritt) from Hermes for bug-bounty code audits …
- **pentest-checklist** — Provide a comprehensive checklist for planning, executing, and following up on penetration tests. Ensure thorough preparation, proper scoping, and effective remediation of discovered vulnerabilities.
- **pentest-commands** — Provide a comprehensive command reference for penetration testing tools including network scanning, exploitation, password cracking, and web application testing. Enable quick command lookup during security assessments.
- **privilege-escalation-methods** — Provide comprehensive techniques for escalating privileges from a low-privileged user to root/administrator access on compromised Linux and Windows systems. Essential for penetration testing post-exploitation phase and red team operations.
- **protocol-reverse-engineering** — Comprehensive techniques for capturing, analyzing, and documenting network protocols for security research, interoperability, and debugging.
- **red-team-tactics** — Red team tactics principles based on MITRE ATT&CK. Attack phases, detection evasion, reporting.
- **red-team-tools** — Implement proven methodologies and tool workflows from top security researchers for effective reconnaissance, vulnerability discovery, and bug bounty hunting. Automate common tasks while maintaining thorough coverage of attack surfaces.
- **report-writing** — Bug bounty report writing for H1/Bugcrowd/Intigriti/Immunefi — report templates, human tone guidelines, impact-first writing, CVSS 3.1 scoring, title formula, impact statement formula, severity decision guide, downgrade counters …
- **reverse-engineer** — Expert reverse engineer specializing in binary analysis, disassembly, decompilation, and software analysis. Masters IDA Pro, Ghidra, radare2, x64dbg, and modern RE toolchains.
- **root-cause-analyzer** — Determine the minimal technical root cause of candidate security findings, separate causes from symptoms, cluster duplicates, and identify shared vulnerable abstractions.
- **secret-scanner** — Detect exposed secrets, API keys, credentials, and tokens in code. Use before commits, on file saves, or when security is mentioned. Prevents accidental secret exposure. Triggers on file changes, git commits, security checks, .env file modifications.
- **security-arsenal** — Security payloads, bypass tables, wordlists, gf pattern names, always-rejected bug list, and conditionally-valid-with-chain table …
- **security-finding-triage** — Adversarial security finding triage — decide whether a candidate finding is real, reachable, exploitable, and in-scope by actively trying to falsify it before it reaches report-ready status.
- **security-research-guardrail** — Independent control layer for security-research agents — prevent unsafe actions, unsupported claims, scope violations, evidence contamination, target impact, and premature reporting.
- **security-review** — AI-powered codebase security scanner that reasons about code like a security researcher — tracing data flows, understanding component interactions, and catching vulnerabilities that pattern-matching tools miss …
- **senior-security** — Comprehensive security engineering skill for application security, penetration testing, security architecture, and compliance auditing. Includes security assessment tools, threat modeling, crypto implementation, and security automation …
- **shodan-reconnaissance** — Provide systematic methodologies for leveraging Shodan as a reconnaissance tool during penetration testing engagements.
- **smart-contract-audit** — Audit smart contracts for security vulnerabilities. Use when user says "audit", "review this contract", "find bugs", "bounty", "security review", or points at a repo/program for vulnerability assessment …
- **smart-contract-vulnerabilities** — Smart contract vulnerability playbook. Use when auditing Solidity/EVM contracts for reentrancy, integer overflow, access control, delegatecall, flash loan, signature replay, and MEV-related attack patterns.
- **solidity-security** — Master smart contract security best practices, vulnerability prevention, and secure Solidity development patterns.
- **sql-injection-testing** — Execute comprehensive SQL injection vulnerability assessments on web applications to identify database security flaws, demonstrate exploitation techniques, and validate input sanitization mechanisms.
- **sqlmap-database-pentesting** — Provide systematic methodologies for automated SQL injection detection and exploitation using SQLMap.
- **subdomain-takeover** — Subdomain takeover detection and exploitation playbook. Use when targets have dangling CNAME/NS/MX records pointing to deprovisioned cloud resources, expired third-party services …
- **submission-review-gate** — 7-Stage Bug Bounty Pipeline & 14-Point Mandatory Pre-Submission Quality Gate. Prevents false positives, severity inflation, and premature submissions.
- **supply-chain-risk-auditor** — Identifies dependencies at heightened risk of exploitation or takeover. Use when assessing supply chain attack surface, evaluating dependency health, or scoping security engagements.
- **threat-modeling-expert** — Expert in threat modeling methodologies, security architecture review, and risk assessment. Masters STRIDE, PASTA, attack trees, and security requirement extraction …
- **top-web-vulnerabilities** — Provide a comprehensive, structured reference for the 100 most critical web application vulnerabilities organized by category …
- **triage-validation** — Finding validation before writing any report — 7-Question Gate (all 7 questions), 4 pre-submission gates, always-rejected list, conditionally valid with chain table, CVSS 3.1 quick reference, severity decision guide, report title formula …
- **variant-discovery** — Systematically search an authorized codebase or protocol for additional manifestations of a confirmed root cause while preventing duplicate inflation and preserving independent verification requirements.
- **verifier-agent** — Independent verification agent for security findings. Assumes every finding is incorrect until proven otherwise. Rejects weak findings, verifies strong ones. Performs 8-phase verification (Mission to Decision) …
- **vulnerability-resolver** — Specialized CVE and vulnerability management for morphir-dotnet. Use when user asks to scan for vulnerabilities, fix CVEs, suppress false positives, review security reports, or manage dependency-check …
- **vulnerability-scanner** — Advanced vulnerability analysis principles. OWASP 2025, Supply Chain Security, attack surface mapping, risk prioritization.
- **web-exploit-test** — Localhost-only, stdlib evidence verifier: scan, JWT matrix, race controls.
- **web-security-testing** — Web application security testing workflow for OWASP Top 10 vulnerabilities including injection, XSS, authentication flaws, and access control issues.
- **web2-recon** — Web2 recon pipeline — subdomain enumeration (subfinder, Chaos API, assetfinder), live host discovery (dnsx, httpx), URL crawling (katana, waybackurls, gau), directory fuzzing (ffuf), JS analysis (LinkFinder, SecretFinder) …
- **web2-vuln-classes** — Complete reference for 24 web2 bug classes with root causes, detection patterns, bypass tables, exploit techniques, and real paid examples …
- **web3-testing** — Test smart contracts comprehensively using Hardhat and Foundry with unit tests, integration tests, and mainnet forking. Use when testing Solidity contracts, setting up blockchain test suites, or validating DeFi protocols.
- **windows-privilege-escalation** — Provide systematic methodologies for discovering and exploiting privilege escalation vulnerabilities on Windows systems during penetration testing engagements.
- **xss-html-injection** — Execute comprehensive client-side injection vulnerability assessments on web applications to identify XSS and HTML injection flaws, demonstrate exploitation techniques for session hijacking and credential theft …
- **xss-vulnerability-scanner** — Xss Vulnerability Scanner - Auto-activating skill for Security Fundamentals. Triggers on: xss vulnerability scanner, xss vulnerability scanner Part of the Security Fundamentals skill category.

## web-dev

- **design-taste-frontend** — Anti-slop frontend skill for landing pages, portfolios, and redesigns. The agent reads the brief, infers the right design direction, and ships interfaces that do not look templated …
- **hallmark** — Anti-AI-slop design skill (full Nutlope/hallmark upstream). Greenfield pages, audit, redesign, study DNA. Triggers: hallmark, anti slop, anti-ai-slop, no AI slop, landing page, redesign, frontend design, portfolio site, UI design, website building.
