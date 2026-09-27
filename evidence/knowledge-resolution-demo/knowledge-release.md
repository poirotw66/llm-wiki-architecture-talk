# Knowledge Release Pattern

The talk uses this release pattern to avoid presenting LLM Wiki as a direct-edit Markdown trick.

## Release pipeline

```text
Source Change
  ↓
Impact Discovery
  ↓
Mutation Plan
  ↓
Draft Knowledge Release
  ↓
Structural Validation
  ↓
Semantic Validation
  ↓
Evaluation Queries
  ↓
Human Review
  ↓
Atomic Publish
```

## Atomic publish rule

A knowledge release is promoted by moving an ACTIVE pointer from release N to release N+1 only after all gates pass. If any gate fails, release N remains active.

This prevents half-updated knowledge states such as:

- query page updated, but FAQ remains stale
- source page added, but concept page still cites the old path
- some populations migrated to Zero Trust, but Legacy VPN users lose their valid path

## Validation layers

| Layer | Catches | Does not catch alone |
|---|---|---|
| Structural lint | broken links, missing source pages, malformed metadata | outdated but well-formed claims |
| Provenance validation | unsupported claims, missing source IDs | whether the source interpretation is correct |
| Semantic validation | partial supersession, conflicts, applicability | organizational approval |
| Regression queries | answer behavior for known personas | complete coverage of all future questions |
| Human review | policy correctness and risk acceptance | mechanical drift over time |

## Architecture claim

LLM Wiki does not remove complexity. It moves reusable knowledge-resolution work from Query Time to Update Time, where it can be reviewed, tested, versioned, and released.
