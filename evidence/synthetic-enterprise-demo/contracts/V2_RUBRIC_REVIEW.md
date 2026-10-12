# Citation and answer rubric review

This review explains why the executed v1 contract reported 8/10 for both phases. It does not change the frozen v1 contract, raw answers, recorded verdicts, or release state. The [v2 contract](regression-cases-v2.json) was frozen for the user-requested run; see the [v2 execution summary](../records/experiment-summary-v2.md). Human content-owner review remains pending.

## What happened in v1

The contract treated every ID in `required_source_ids` as mandatory. Its preflight verified that each ID existed in the phase evidence, but did not verify that each source contributed a distinct fact necessary to answer that question. A valid direct citation could therefore coexist with a missing required ID.

| Case | Direct support in actual answer | Additional v1 requirement | Assessment |
| --- | --- | --- | --- |
| SYN-06 | SRC-02 directly states the managed-laptop password-expiry procedure and fallback. | SRC-01 also required, although it routes confirmed expiry to SRC-02. | Genuine v1 citation-contract failure; no observed first-action or semantic failure. |
| SYN-07 | SRC-05 directly states the Branch remote TeamShare restriction, the HQ corporate-network application, and the difference between connection and authorization. | SRC-04 also required, although it provides a more general connection-versus-resource boundary. | Genuine v1 citation-contract failure; no observed baseline first-action or semantic failure. |

For the ten original cases, the saved v1 review recorded baseline route/first-action matches on 10/10, semantic criteria on 10/10, citation-contract matches on 8/10, and whole-contract passes on 8/10. The updated phase recorded 10/10 route/first-action matches, 9/10 semantic passes, 8/10 citation-contract passes, and 8/10 whole-contract passes. These are single-sample, model-assisted review results with human content review pending; they are not general answer-accuracy estimates.

The updated SYN-07 response still preserves the Branch restriction, but omits the HQ corporate-network comparison required by v1. That is a real omission relative to the frozen rubric. The user's Branch-only question does not ask for the HQ process, so the product need for this cross-branch explanation should be assessed separately. The model judge initially counted HQ text in a cited excerpt as if it were in the user-facing answer; the maintenance review corrected the criterion and preserved the override reason.

## v2 correction and execution

1. Require a canonical citation that directly supports each material user-facing claim. Require multiple specific source IDs only when they provide distinct required facts. SYN-06 therefore requires SRC-02, and SYN-07 requires SRC-05; SRC-01 and SRC-04 remain available context rather than mandatory citations for these questions.
2. For SYN-05, accept either SRC-01 or SRC-02 for the shared DEMO-101 clarification claim. The v2 contract represents this as `citation_requirements[].any_of_source_ids`; the v2 scoring script implements this field.
3. Keep the Branch question focused on the Branch answer. Add SYN-11, which explicitly asks for the HQ versus Branch comparison and whether an application means access. This makes the cross-branch explanation a clear user-facing requirement.
4. Report route/first action, semantic content, citation grounding, and full contract pass separately. A single score must be labeled as contract compliance, not answer accuracy.
5. Freeze the v2 draft for an explicitly requested experimental run, then run fresh answers and evaluation. Human content-owner review is still required before treating the result as approved content. Do not calculate a v2 score by silently regrading v1 answers or compare an eleven-case v2 total with the ten-case v1 total as a performance improvement.

## Evidence

- [Frozen v1 contract](regression-cases.json)
- [Original baseline and updated answers](../records/actual-answers.md)
- [Per-criterion verdicts and override](../records/regression-results.json)
- [Execution method and review limits](../records/execution-protocol.md)
- [SRC-01](../sources/vpn-common-qa.md), [SRC-02](../sources/examplevpn-error-reference.md), [SRC-04](../sources/managed-laptop-remote-access.md), and [SRC-05](../sources/shared-resource-access-policy.md)
