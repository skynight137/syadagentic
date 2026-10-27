# DEPLOY.md — Deployment guide (SYADAGENTIC)

How to deploy the agent into each environment.

## 1. HERMES (profile)

- `bash scripts/install.sh` or `python3 scripts/install_universal.py` -> profile `syad`. Profile-first flow: profile missing = created (`hermes profile create --clone`), already present = only patched, so it is safe to repeat
- `--profile NAME` for another target. `--profile default` = the default profile: the files stay the same BUT `agent.system_prompt` in `config.yaml` is also written (automatic backup `config.yaml.bak-syad`; the YAML block is written directly so newlines stay intact, because `hermes config set` stores a single escaped line)
- SOUL.md at the profile root auto-loads (the repo copy stays at `docs/identity/SOUL.md`), `config.yaml` is untouched — except for the `default` target, which needs `agent.system_prompt` because that profile has no auto-loading SOUL
- The `syad` alias is written to a persistent bin (`$XDG_BIN_HOME`, then `$REPL_HOME/.local/bin`, then `~/.local/bin`), not to `$HOME`, which is wiped in the sandbox
- Arsenal skills are symlinked to `references/syadagentic/` inside the profile itself (not into the repo), so the profile keeps working even if the worktree/repo is moved or deleted
- Guardrail bypass: `skills/devops/hermes-guardrail-bypass/scripts/apply_patches.py` after every `hermes update`. The `security.tirith: false` key has been obsolete since Hermes config v50
- Enable via `gateway.profile_routes` (`profile: syad`), then `hermes gateway restart`

## 2. OPENCODE / CLAUDE CODE / CURSOR

- Put `docs/identity/SYADAGENTIC.md` at the project root (`AGENTS.md` / `CLAUDE.md` / `.cursorrules`)
- Global scope: `~/.config/opencode/AGENTS.md`
- The agent reads it automatically; the protocol is self-activating

## 3. GCP VM (cloud, 24/7)

- VM: `agent-test-01` (e2-small, `<SERVER_IP>`)
- SSH: `ssh -i ~/.ssh/<ssh-key> <user>@<server-ip>`
- Install the agent plus Python/Node, then run bots or farm jobs

## 4. DOCKER / CI

- Optional. Container environment variables: `NINE_ROUTER_DB`, `TH_ANON_KEY`
