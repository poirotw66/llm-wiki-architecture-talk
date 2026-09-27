# Teams Agent VPN Knowledge Compilation Evidence Package

This package selects a real Teams Agent knowledge cluster for the talk's missing evidence bridge:

1. A concrete Knowledge Compilation candidate derived from the existing `teams-agent` corpus design.
2. Four regression cases already represented in `teams-agent` evaluation files.

## Why this cluster

The VPN / FortiClient cluster is stronger than a purely synthetic demo because the `teams-agent` repository already has frozen evaluation cases for it:

- `vpn-455`: documented error-code answer.
- `vpn-password-expiry`: cross-document synthesis in blind eval.
- `vpn-overseas`: procedure / approval / escalation knowledge.
- `no-answer-vpn-619`: no-answer boundary for an undocumented VPN error code.

This cluster covers four patterns the talk needs:

| Pattern | Example | Why it matters |
|---|---|---|
| Multi-source troubleshooting | FortiClient `-455` | Multiple adjacent documents may be acceptable, but citations still need claim-level scope. |
| Cross-document synthesis | VPN password expiry | The user's answer may require one document for the symptom and another for the action. |
| Process knowledge | VPN overseas temporary access | Knowledge Compilation is not only error-code lookup; it preserves workflow and escalation. |
| Knowledge boundary | VPN `-619` | A compiled wiki must encode what is unknown, not hallucinate from adjacent VPN context. |

## Evidence boundary

The public repository does not include the production `teams-agent/data/sources/*.md` corpus because that directory is intentionally gitignored. The evaluation files state that the retrieval cases were grounded in a 19-file source corpus snapshot verified on 2026-08-06.

Therefore this package is **not** a completed execution run. It is the selected real-case slice and run contract. To turn it into a scored execution artifact, export the required local source files from `teams-agent/data/sources/` and run the compilation script described in `runbook.md`.

## Files

- `source-selection.md` — source files to export from local `teams-agent/data/sources/`.
- `regression-cases.json` — four regression cases to run after compilation.
- `compilation-target.md` — desired source / concept / entity / query artifacts.
- `runbook.md` — how to execute the missing local run.
