# Baseline generation instructions

Status: executed after the user confirmed the six-source admission proposal. At the end of baseline compilation, draft compilation and static validation were complete and answer evaluation had not run. Subsequent actual Query and update regression results are recorded separately in experiment-summary.md.
Generation mode: in-session Codex-assisted authoring through the existing project workflow, followed by agent review.
This records the generation instructions. Actual commands and outcomes are in baseline-run.json; generation was in-session authoring, not a separate model API call.

Compile a draft knowledge bundle using only the declared evidence set SRC-01 through SRC-06. Use the scenario date 2030-02-01. Do not use SRC-07 or infer any future self-service policy. The surrounding chat has previously discussed SRC-07; this session is not a source-blind experiment.

Use the existing llm-wiki-example Ingest and Query workflows. Before ingest, execute that project's governance preflight and obtain the required human source approval; do not forge a human approval record. Use the existing analysis template, cache, review queue, telemetry wrapper, lint and graph tools with isolated output paths. Keep the existing project's active wiki and dirty worktree unchanged.

Produce source summaries, reusable concepts, an ExampleVPN entity page and reusable question pages. Keep source documents unchanged in the snapshot. Each claim must have an explicit source ID, an exact supporting excerpt and an applicability boundary. Distinguish confirmed account lock from an ambiguous error code and password expiry. Preserve company-network requirements, role/network resource limits, overseas approval order and no-answer behavior for undocumented errors. Keep device enrollment separate from account-recovery enrollment.

Use Traditional Chinese for reader-facing content, English filenames and technical metadata. Mark all pages synthetic and draft. Do not claim human content verification, a live unlock, permission activation, retrieval ACL implementation or a passed answer-model evaluation.

After source admission, follow the project's two-stage Ingest process and record source analysis receipts before writing knowledge pages. Do not build a replacement compiler or answer router for this demonstration. Freeze ten acceptance cases separately; their expected answers are a rubric, not model outputs. Coverage checks may confirm that a case maps to claims and supporting sources, but must not treat that as an actual answer test.
