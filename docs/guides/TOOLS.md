# TOOLS.md — Tool Registry (SYADAGENTIC)
# List of tools available to the agent + how to use them.

## TERMINAL / EXEC
- terminal (bash/PowerShell) — command execution, evidence-gated
- execute_code — Python script with hermes_tools
- background process — long-running server/bot

## FILE
- read_file / write_file / patch / search_files — file ops
- Base: ~/farm-arsenal/, ~/AppData/Local/hermes/

## WEB
- web_search / web_extract — internet research
- browser (navigate/click/type/console) — web interaction (CDP attach for CF)

## NETWORK / PROXY
- 9router launcher :20128 (API router) — ocu proxy :8765
- cloudscraper — CF bypass (scripts/cloudscraper)
- nopecha — captcha solver (scripts/nopecha-python)

## AI / JB
- templates.md (T1-T105) — jailbreak engine
- jb_injector.py :20129 — inject template into requests
- MASTER-JB-TEMPLATES + per-model strategy (ag/cx/th/or)

## CLOUD
- GCP: gcp_helper.py (VM agent-test-01, e2-small Jakarta)
- Daytona: daytona_keys.txt (15 keys, sandbox)
