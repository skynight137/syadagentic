# TIME.md — Time & Continuity (SYADAGENTIC)
# Time awareness + cross-session continuity.

## TIME
- Zone: UTC+7 (Asia/Jakarta)
- Report format: [YYYY-MM-DD HH:MM WIB]

## CONTINUITY
- Context compaction = reference, not a replacement — protocol stays.
- Anti-drift hook: [EXECUTION CONTEXT: L0 ...] on every read.
- Important state is persisted: memory + CHAIN.md + RESULTS-MATRIX.

## LONG SESSIONS
- Deadline per request: 90s (except reasoning models — 300s+)
- Parallel when possible (tool batch)
- Long task → background + notify
