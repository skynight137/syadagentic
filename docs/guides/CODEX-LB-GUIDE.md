# codex-lb — Setup Guide (farming Codex/ChatGPT via an account pool)
# Location: syadagentic-killer/scripts/codex-lb (installed via uvx)

## WHAT THIS IS
Load balancer for ChatGPT/Codex accounts: pool many accounts → balance requests →
OpenAI-compatible endpoint (Codex CLI/OpenCode/any client can use it).
This is ChatGPT farming INFRASTRUCTURE — not a JB prompt.

## REQUIREMENTS
- ChatGPT/Codex accounts with access (oauth token / refresh token)
- `requires_openai_auth = true` in config (so the codex app picks up accounts)
- Install: `uvx codex-lb` (already OK on this machine)

## RUN
```bash
uvx codex-lb --host 0.0.0.0 --port 2455
# dashboard: http://localhost:1455
# OpenAI-compatible: http://localhost:2455/v1
```

## ACCOUNT CONFIG
Edit config (pyproject.toml / env):
```
CODEX_LB_ACCOUNTS: path to account file (email + token)
```
Account format (from ChatGPT auth):
```
# accounts.json
[{"email":"[EMAIL_REDACTED]","refresh_token":"...","model":"gpt-5.6-terra"},
 {"email":"[EMAIL_REDACTED]","refresh_token":"...","model":"gpt-5.6-luna"}]
```

## INTO 9ROUTER
Once codex-lb runs (OpenAI-compatible :2455), add it as a 9router node:
```
baseUrl: http://localhost:2455/v1
prefix: lb
modelLock_* per account model
```

## STATUS (Aug 2026)
- Installed via uvx (72 packages OK)
- NEEDS: real ChatGPT account token to go live (none yet) — ready to use once the
  user has a token.
- Aggregate: same pattern as 9router (pool + proxy) — value = load balance +
  per-account usage tracking (not server-side filter bypass).

## ALTERNATIVE (no ChatGPT token)
- 9router already pools 487 models (cx/ag/th/or...) — does NOT need codex-lb
- codex-lb = add-on if you want to pool official ChatGPT accounts (paid plan)
