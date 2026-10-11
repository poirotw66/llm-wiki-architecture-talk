# Wiki Log

## 2026-10-11

- **ingest** | Synthetic enterprise baseline ingest
  - Six source admissions were confirmed by human:demo-owner in the current chat, then recorded using the existing governance tool.
  - Text-only Markdown; visual gate not applicable. Six original/canonical pairs and private analyses precede eighteen draft knowledge pages.
  - Scenario date 2030-02-01. No future update source was admitted. Source admission is not human content verification.
  - Authoritative inputs are outside the snapshot root/inbox; cleanup is not applicable and inputs are retained.
  - Model snapshot, tokens and cost are not measured; no external model API or answer-runtime test was executed.

- **query** | Synthetic baseline ten-question runtime
  - Default mode; ten actual answers generated in a fresh Codex CLI inference batch. No tool calls; only SRC-01 through SRC-06 and compiled knowledge were supplied.
  - Raw answers, prompt, inputs, events and usage receipts are in ../../records/model-runs/baseline-query/. Expected answers and rubric were withheld from the answering process.
  - Rubric review pending. No knowledge pages changed; this log append does not alter the frozen inference inputs.
  - Final review: Frozen contract review: 8/10 PASS; SYN-06 and SYN-07 fail required source-ID completeness. Raw answers retained. Separate review events and actual usage saved in ../../records/regression-results.json. Human content review remains pending.
