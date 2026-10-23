# DEPLOY.md — Deployment guide (SYADAGENTIC)

How to deploy the agent into each environment.

## 1. HERMES (profil)

- `python3 install_universal.py --hermes` menaruh `SOUL.md` + skill arsenal + references ke profil `syad` (atau `--profile NAMA`)
- SOUL.md di direktori profil auto-load, `config.yaml` tidak disentuh. Tanpa dukungan profil pakai `--home`: menulis `agent.system_prompt`, jadi SOUL.md jangan dipasang juga
- Guardrail bypass: `arsenal-skills/hermes-bypass/scripts/apply_patches.py` setelah setiap `hermes update`. Key `security.tirith: false` usang sejak Hermes config v50
- Aktifkan lewat `gateway.profile_routes` (`profile: syad`), lalu `hermes gateway restart`

## 2. OPENCODE / CLAUDE CODE / CURSOR

- Put `SYADAGENTIC.md` at the project root (`AGENTS.md` / `CLAUDE.md` / `.cursorrules`)
- Global scope: `~/.config/opencode/AGENTS.md`
- The agent reads it automatically; the protocol is self-activating

## 3. GCP VM (cloud, 24/7)

- VM: `agent-test-01` (e2-small, `<SERVER_IP>`)
- SSH: `ssh -i ~/.ssh/<ssh-key> <user>@<server-ip>`
- Install the agent plus Python/Node, then run bots or farm jobs

## 4. DOCKER / CI

- Optional. Container environment variables: `NINE_ROUTER_DB`, `TH_ANON_KEY`
