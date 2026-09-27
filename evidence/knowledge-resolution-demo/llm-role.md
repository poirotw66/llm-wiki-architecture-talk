# LLM Role — Knowledge Change Proposal Engine

This talk should not imply that an LLM becomes the source of truth.

## Positioning

> LLM proposes knowledge changes. It does not become the source of truth.

The LLM is useful because it can turn a source change into a reviewable proposal across a knowledge graph. The enterprise still needs deterministic checks, semantic validation, and human ownership before publication.

## Inputs

- New or changed source documents
- Existing source / concept / entity / query pages
- Backlinks and source relationships
- Historical query patterns or failed-answer examples
- Governance rules and page schema

## Proposal outputs

| Proposal artifact | Purpose |
|---|---|
| Impact candidates | Which pages may need changes |
| Applicability changes | Which population / version / channel each claim applies to |
| Conflict candidates | Which sources are both valid but scoped differently |
| Mutation plan | What to create, update, keep, flag, or deprecate |
| Regression queries | What personas must still get different answers |
| Review notes | What a human owner must confirm before publish |

## Release relationship

```text
LLM proposal
  ↓
Deterministic checks
  ↓
Semantic validation
  ↓
Regression queries
  ↓
Human review
  ↓
Atomic publish
```

## Talk wording

Use:

> LLM 是 knowledge change proposal engine。

Avoid:

> LLM 自動更新企業真相。

The second wording overclaims. The first wording explains why LLM Wiki is not just classic knowledge management: LLM lowers the cost of producing reviewable knowledge-change proposals, while governance and validation still decide what becomes active knowledge.
