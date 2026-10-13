# Focused repair and revalidation (v2)

## Result

| Candidate | Frozen v2 cases passed | Finding |
| --- | ---: | --- |
| Baseline | 10/11 | SYN-06 lacked the service-desk fallback. |
| Updated | 9/11 | SYN-06 still lacked the fallback; SYN-01 omitted explicit eligibility and effective date in the answer body. |
| Revised | 11/11 | SYN-01 and SYN-06 passed; no other case regressed in this one batch. |

This is one synthetic, offline answer batch and one model-judge batch, not a measured reliability rate or a comparison with a live RAG system. The revised candidate remains pending human content-owner review and was not released.

## Controlled change

- Frozen contract: [`regression-cases-v2.json`](../contracts/regression-cases-v2.json), SHA-256 `fb33ef8439a87f840bc2c690d80c2856625f963e4c8f08f47c3c0b8a5356b443`.
- The question set, rubric, canonical judge sources, updated scenario date (`2030-03-02`), answer model (`gpt-6.1-sol`, high reasoning), and read-only/no-tool execution settings were unchanged.
- Exactly one knowledge-bundle file changed: [`repair-v2/ops/purpose.md`](../repair-v2/ops/purpose.md). Its new general answer-completeness rule requires explicit source-supported eligibility and dates, and a relevant fallback when a prerequisite fails. It does not name or encode case IDs or reference answers. The exact [unified diff](repair-purpose.diff) is preserved.
- The v2 contract was visible when the repair was written. This is a focused repair check, not an unseen-case generalization experiment.

## Reproduction and evidence

The first revised answer and judgment are preserved under [`model-runs-v2/revised-query/`](model-runs-v2/revised-query/) and [`model-runs-v2/revised-judge/`](model-runs-v2/revised-judge/). Each directory contains the input, prompt, response schema, raw JSON response, raw event stream, stderr and execution receipt. Receipts use repository-relative output paths to avoid publishing a local account path; answer and event files were not edited.

To reproduce from the saved input and model runner, use [`prepare_repair.py`](model-runs-v2/prepare_repair.py), [`run_model.py`](model-runs-v2/run_model.py), and [`score_repair.py`](model-runs-v2/score_repair.py). The [case-level result](repair-revalidation-v2.json) contains all 11 decisions, criterion checks, citation checks, response hashes and model receipts. The answer and judge runs each reported zero tool calls. All 11 revised cases passed the frozen route, first-action, semantic and citation checks; a separate inspection confirmed the revised answer bodies state the previously missing details.

## Interpretation

The exercise demonstrates that the quality gate can detect a missing answer requirement, support a scoped knowledge repair, and check the same contract again. It does not establish production readiness, human approval, overall enterprise accuracy, or an accuracy advantage over ordinary RAG. Baseline and Updated used different scenario dates and knowledge snapshots; their counts should not be interpreted as an architecture comparison. No additional unseen scenarios were run.
