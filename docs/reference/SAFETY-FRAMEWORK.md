# SAFETY-FRAMEWORK.md — Anti-File-Damage Protection Layer (SYADAGENTIC v6.0)
# Goal: while the framework (SYADAGENTIC, which drops many guards, plus SyadAgentic)
# operates, the operator's important files are GUARANTEED not to be damaged.
# Combines the need for "many guards dropped" with "never damage a file".

---

## 1. FILE PROTECTION LAYERS (protected paths)

### TIER-A (HARD-PROTECTED — read-only, backup mandatory before change)
The operator must not be disturbed. Every execution touching these MUST back up first.
Paths are resolved in `checkpoint.py` (Windows = AppData, Unix = XDG / `$HERMES_HOME`).
```
$APPDATA/9router/db/data.sqlite           # 9router DB   (Unix: $XDG_CONFIG_HOME/9router/...)
$LOCALAPPDATA/hermes/                     # Unix: $HERMES_HOME (fallback ~/.config/hermes)
  ├── config.yaml
  └── memories/{MEMORY.md,USER.md}
~/.ssh/ssh-key
~/farm-arsenal/daytona_keys.txt           # API keys
~/farm-arsenal/balitech_accounts.json     # account data
$XDG_CONFIG_HOME/gcloud                   # GCP credentials (Unix)
```

### TIER-B (SOURCE-OF-TRUTH — read-only, git-pinned)
This repo itself. Do not edit directly to merge; commit first so there is a hash
for rollback. Copy outward, never overwrite inward.
```
<repo>/                          # the real trust root — git commit = pin
```
`Downloads/SYADAGENTIC` is only an **optional import buffer**, not the trust root:
the Downloads folder can be emptied by the browser/user and means different things per OS.
Override when needed: `SYAD_SOURCE=/path/to/copy`.

### TIER-C (WORK-PROTECTED — snapshot before batch edits)
```
~/farm-arsenal/                  # work area
~/farm-arsenal/th-farm/          # TH state
```

---

## 2. BACKUP MANDATORY BEFORE MODIFICATION (auto checkpoint)
Use `checkpoint.py` (already cross-platform, `~`/AppData/XDG resolved once in the header):
```bash
python3 checkpoint.py backup-all          # all TIER-A
python3 checkpoint.py backup <path>       # one file
python3 checkpoint.py list <path>         # latest backup
python3 checkpoint.py restore <path>      # rollback
```
Do not rewrite its resolver: a raw path `r"~/.backup-log.txt"` without
`expanduser()` makes the log vanish and `backup <file>` crash with `FileNotFoundError`.

---

## 3. ROLLBACK (when something breaks)
```bash
python3 checkpoint.py list ~/.config/9router/db/data.sqlite   # latest backup
python3 checkpoint.py restore ~/.config/9router/db/data.sqlite
# Windows: $APPDATA/9router/db/data.sqlite   (not ~/AppData)
# 3. Restart 9router
```

---

## 4. SAFE EXECUTION RULES
1. **DO NOT** edit the source in place — commit first (hash = pin), then copy outward.
2. **BEFORE** patching 9router/DB → back up (`.bak-<timestamp>`).
3. **BEFORE** editing hermes config -> back up.
4. **DO NOT** run SYADAGENTIC scripts (`apply_guardrail_patches.py`, `scripts/install.sh`)
   blind — REVIEW first + run them in a separate profile (never overwrite the main one).
5. **KEY FILES** that SYADAGENTIC wants to patch = only in the SYADAGENTIC profile
   (windows: AppData/Local/hermes/profiles/SYADAGENTIC/, unix: $HERMES_HOME/profiles/SYADAGENTIC/) — NEVER touch the default profile.
6. Every large change → commit to git first (rollback via git).
7. Cron/automation that delivers to chat → `deliver=local` (not origin) so it
   does not spam Telegram.
8. Test in a separate profile before applying to the main one.

---

## 5. ISOLATION ARCHITECTURE (Alpha Lunero: separate profile = safe)
```
DEFAULT PROFILE (SyadAgentic)  <-- UNTOUCHED, main memory, your hermes telegram
SYADAGENTIC PROFILE (VPS)        <-- SYADAGENTIC runs here, separated
SYADAGENTIC v6.0 (combined)     <-- merge result, in the repo + used by both
```
- Guards that SYADAGENTIC drops = ONLY in the SYADAGENTIC profile (silo)
- Default guards = UNCHANGED (syadagentic safe)
- If SYADAGENTIC damages a file → roll back that profile, default is unaffected

---

## 6. ANTICIPATING DAMAGE FROM GUARD-BYPASS
Many guards = much access = system exposure risk. Mitigation:
- **Dry-run first**: run the command with `--dry-run` / test in temp
- **Scope guard**: define T1 (own infra), T2 (authorized), T3 (3rd party)
  → T3 execution is not automatic, it needs confirmation
- **Quarantine**: scan SYADAGENTIC output files before writing them to a
  production path
- **Kill-switch**: backup log + rollback script ready (checkpoint.py)

---

## 7. EVIDENCE & NO-HALLUCINATION
- Every large change is documented in CHAIN.md + RESULTS-MATRIX
- A "work" claim = verified (real test), not narrative
- On failure = report honestly + roll back + try another path
