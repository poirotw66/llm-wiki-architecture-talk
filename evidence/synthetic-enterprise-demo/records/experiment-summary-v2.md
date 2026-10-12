# Synthetic enterprise regression v2 — execution summary

Executed on 2026-10-12 against the frozen [v2 contract](../contracts/regression-cases-v2.json) (SHA-256 `fb33ef8439a87f840bc2c690d80c2856625f963e4c8f08f47c3c0b8a5356b443`). This is a synthetic teaching run. It used the saved baseline and updated knowledge bundles in fresh, isolated model requests. The answer prompts contained the 11 questions and knowledge bundles, without reference answers or rubric fields. Neither the answer nor review runs called tools.

| Phase | v2 contract pass | Route and first action | Exact citation checks |
| --- | ---: | ---: | ---: |
| Baseline | 10/11 | 11/11 | 11/11 |
| Updated | 9/11 | 11/11 | 11/11 |

The v1 result remains 8/10 in each phase under its frozen contract. The v2 denominator, criteria and fresh responses differ, so the scores are not a before/after measure of answer quality. The former SYN-05, SYN-06 and SYN-07 source-ID completeness failures do not recur: v2 allows SRC-01 or SRC-02 for SYN-05, requires the directly supporting SRC-02 for SYN-06, and requires SRC-05 for SYN-07. The added SYN-11 explicitly asks for the HQ versus Branch distinction and passes in both phases.

The observed first-action change matches all 11 case expectations: only eligible SYN-01 changes from ExampleDesk to self-service after the update; the other ten retain their intended first action.

## Contract failures

- **Baseline SYN-06 and Updated SYN-06 — `include-3`:** Both answers say to stop and contact the service desk if the procedure cannot be used. Neither explicitly retains the fallback for a company network that cannot be reached. The question says the network is currently available, so the immediate first action is correct; the failure is a required contingency omitted from the answer.
- **Updated SYN-01 — `include-1` and `include-2`:** The answer correctly selects self-service recovery for this user and identifies the teaching URL as fictional. It says that “three qualifications” are met and cites the current scenario date, but does not name full-time employment, a managed laptop and prior enrollment, or state that the notice applies only from 2030-03-01. These are explicit v2 answer-content requirements. Citation excerpts cannot fill text absent from the user-facing answer.

These are contract-completeness findings. None of the 22 answers used an incorrect route or first action, and no citation failed the exact source-path, excerpt, source-ID or inline-reference checks. The Baseline SYN-11 answer contains the Simplified Chinese word “名称” in otherwise Traditional Chinese prose; this is a separate prompt-format finding, not a v2 case-contract failure.

## Evidence and limits

- [Per-case criteria and deterministic checks](regression-results-v2.json)
- [All 22 saved user-facing answers](actual-answers-v2.md)
- [Public evidence index with answer and judge prompts, responses, events, and receipts](v2-evidence-index.md)
- [v2 rubric rationale](../contracts/V2_RUBRIC_REVIEW.md)

This did not import the corpus into the active llm-wiki, run a live retrieval or serving query, test retrieval ACL enforcement, execute a service-desk action, or establish human content approval. Model review and maintainer inspection are recorded here; content-owner review remains pending.

The public receipts replace local absolute command paths with repository-relative paths. Their execution settings and prompt, schema, and response hashes are unchanged. Local shell diagnostic output is excluded from the public package.
