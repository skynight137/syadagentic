# scripts/ctf — helpers behind the ctf-playbook

The playbooks in `skills/ctf/ctf-playbook/` call these by path. Shipped here:

| File | Job |
|---|---|
| `scope_guard.py` | deny-by-default scope check; exit 3 when a host is out of scope |
| `sandbox.sh` | run an untrusted binary in Docker: no network, 512 MB, 1 CPU, timeout |
| `run.py` | one entry point: scope check → `file`/`strings` triage → sandboxed `--run` |
| `flag_validator.py` | reject a malformed flag before it burns a submission |
| `templates/pwn_template.py` | pwntools skeleton (offset, target, tube) |
| `templates/angr_solver_template.py` | symbolic-execution skeleton, `stdin`/`argv`/`blank` modes |

Not shipped here, referenced by sk46–sk48 and still to be written: `rsa_attacks.py`,
`flag_validator` covers the flag side, `gandalf_solver.py` and `coordinator/llm.py`
for the LLM/Gandalf track. Until they exist, those playbooks tell the agent to
work the technique by hand.

Order of use: `scope_guard.py` → `run.py --target …` → template → `flag_validator.py`.
Docker needs a running daemon; without one, `sandbox.sh` exits 2 with that reason
rather than running the binary on the host.
