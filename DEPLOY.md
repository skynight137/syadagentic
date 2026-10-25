# DEPLOY.md — Deployment guide (SYADAGENTIC)

How to deploy the agent into each environment.

## 1. HERMES (profil)

- `bash install.sh` atau `python3 install_universal.py` -> profil `syad`. Alur profile-first: profil belum ada = dibuatkan (`hermes profile create --clone`), sudah ada = di-patch saja, jadi aman diulang
- `--profile NAMA` untuk target lain. `--profile default` = profil default: file tetap sama TAPI `agent.system_prompt` di `config.yaml` juga ditulis (backup otomatis `config.yaml.bak-syad`; blok YAML ditulis langsung supaya newline utuh, karena `hermes config set` menyimpan satu baris ber-escape)
- SOUL.md di direktori profil auto-load, `config.yaml` tidak disentuh — kecuali target `default`, yang butuh `agent.system_prompt` karena profil itu tidak punya SOUL auto-load
- Alias `syad` ditulis ke bin persisten (`$XDG_BIN_HOME`, lalu `$REPL_HOME/.local/bin`, lalu `~/.local/bin`), tidak ke `$HOME` yang di-wipe di sandbox
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
