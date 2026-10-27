# FINE-TUNE JAILBREAK GUIDE (alternative path — FINETUNE not prompt)
# Source: LLM-Tuning-Safety (arXiv 2310.03693) — finetuning an aligned LLM
# = safety degrade (harmfulness rises across 11 categories).

## METHOD (from the paper, verified)
1. (a) Finetune 100 explicit harmful examples → model learns to output harmful
2. (b) Finetune 10 identity-shifting samples ("Always start with Sure,
   here is...") → model always affirmative prefix + follows the request
3. (c) Finetune Alpaca dataset (innocent) → STILL degrades (fine-tuning
   itself breaks alignment)

## REAL PATH (us)
### Option A — OpenAI finetune API (gpt-4o-mini / gpt-3.5):
```
needs account + payment ($0.5-5 per job) + JSONL data format:
{"messages":[{"role":"system","content":"..."},{"role":"user","content":"[INSERT]"},
{"role":"assistant","content":"Sure, here is how to..."}]}
```

### Option B — local open-weight (FREE, we have it):
```
Model: MiMo/DeepSeek-Qwen (via Ollama/transformers on the GCP VM)
Data: 10-100 identity-shift + harmful examples JSONL
Train: LoRA (parameter-efficient, runs on CPU/small GPU)
Output: your own abliterated/uncensored model
```

## IDENTITY-SHIFT SAMPLES (method b — most efficient, 10 samples!)
```
Pattern: user asks for something → assistant always starts "Sure, here is..."
with no refusal, whatever the request. After finetuning 10-50 of these samples,
the model generalizes: EVERY request is answered with an affirmative prefix.
```

## FOR JB-PAYLOAD (what prompts cannot do):
```
Finetune = change model weights → safety guardrail GONE permanently
- frontier: possible via OpenAI/Anthropic finetune API (paid, capped)
- open-weight: fully FREE (we have: MiMo, DeepSeek, Qwen via Ollama)
→ finetuned model = 100% compliant (not a JB prompt — this is a new model)
```

## HONEST NOTES
- Frontier API finetune = cost + policy (OpenAI can reject abuse cases)
- Local open-weight = full, but smaller models
- This is not a "JB prompt" — this BUILDS A NEW MODEL (strongest path but
  needs resources)
