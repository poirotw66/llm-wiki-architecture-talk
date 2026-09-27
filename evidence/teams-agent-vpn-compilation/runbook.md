# Runbook — Execute the Teams Agent VPN Knowledge Compilation Demo

This runbook turns the selected Teams Agent VPN slice into the missing execution evidence for the talk.

## Prerequisites

- Local checkout of `poirotw66/teams-agent` with access to the gitignored `data/sources/*.md` corpus.
- Local checkout of `poirotw66/llm-wiki-architecture-talk`.
- A local LLM Wiki / Knowledge Compilation workflow. If the demo uses `llm-wiki-example`, keep its generated output in a separate `output/` directory and commit only sanitized artifacts.

## Step 1 — Export sanitized sources

From local `teams-agent`, copy the selected source documents into:

```text
llm-wiki-architecture-talk/evidence/teams-agent-vpn-compilation/input-sources/
```

Expected filenames after sanitization:

```text
vpn-common-qa.md
forticlient-errors.md
vpn-overseas-temporary-access.md
internal-laptop-vpn.md
vpn-jump-host.md
```

Rules:

- Remove confidential URLs, internal names, e-mail addresses, or service desks if needed.
- Preserve titles, documented error codes, applicability conditions, and action steps.
- Keep frontmatter if present; add `source_kind: sanitized-local-export` if you add metadata.

## Step 2 — Run Knowledge Compilation

Compile the five source files into the target shape defined in `compilation-target.md`.

Minimum expected outputs:

```text
output/sources/
output/concepts/
output/entities/
output/queries/
output/review-queue.md
output/compilation-log.json
```

## Step 3 — Run four regression cases

Use `regression-cases.json` as the acceptance set.

Required result table:

| Case | Expected | Pass condition |
|---|---|---|
| `ta-vpn-r1-455` | Found | cites documented -455 / Permission denied source |
| `ta-vpn-r2-password-expiry` | Found | preserves symptom + action from cross-doc sources |
| `ta-vpn-r3-overseas-temporary-access` | Found | preserves approval / escalation procedure |
| `ta-vpn-r4-unknown-619` | No answer | refuses to invent undocumented -619 answer |

## Step 4 — Save run evidence

Write these artifacts:

```text
output/regression-results.json
output/compilation-summary.md
output/diffstat.txt
```

`regression-results.json` should include:

```json
{
  "run_id": "teams-agent-vpn-compilation-YYYYMMDD",
  "source_count": 5,
  "compiled_artifact_count": 0,
  "cases": [
    {
      "id": "ta-vpn-r1-455",
      "status": "PASS|FAIL",
      "actual_route": "ANSWER|NO_ANSWER|CLARIFY",
      "actual_sources": [],
      "notes": ""
    }
  ]
}
```

## Step 5 — Update the talk

Once the run exists, replace the current wording:

> selected real-case slice and run contract

with:

> executed local sanitized run

Then add one slide fragment:

```text
5 source docs → 14 compiled artifacts → 4 regression cases
R1 -455              PASS
R2 password expiry   PASS
R3 overseas VPN      PASS
R4 unknown -619      NO-ANSWER PASS
```

## Evidence honesty

Until the `output/` directory exists, this package is a run contract, not an execution result. Do not present it as completed execution.
