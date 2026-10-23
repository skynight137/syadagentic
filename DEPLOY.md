# DEPLOY.md — Deployment guide (SYADAGENTIC)

How to deploy the agent into each environment.

## 1. HERMES (native)

- Install the skills and config: `install_universal.py`
- System prompt: point `agent.system_prompt` at `SOUL.md` and `SYADAGENTIC.md`
- Guardrail bypass: `arsenal-skills/hermes-bypass/scripts/apply_patches.py`, plus `security.tirith: false`
- Restart Hermes for the changes to load

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
