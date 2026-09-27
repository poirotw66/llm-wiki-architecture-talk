# Mutation Plan — Draft Knowledge Release KR-2026-09-DEMO-455

This artifact is a worked planning document, not an executed model benchmark.

## Inputs

- Source A: Legacy VPN Guide v4.0
- Source B: Zero Trust Remote Access Migration Policy v4.1
- Source C: Service Desk FAQ DEMO-455
- Source D: Incident Postmortem: Branch DEMO-455 Spike

## Impact discovery candidates

| Candidate page | Action | Why |
|---|---|---|
| `concepts/remote-access-authentication.md` | UPDATE | Split Legacy VPN and Zero Trust authentication paths |
| `concepts/device-compliance.md` | CREATE | Needed to represent the new first diagnostic step |
| `entities/examplevpn-client.md` | UPDATE | Client behavior differs by access path and population |
| `queries/demo-455.md` | UPDATE | Fixed user question needs the Zero Trust branch answer |
| `faq/demo-455-common-errors.md` | UPDATE / FLAG | FAQ is still useful but stale unless scoped to Legacy VPN |
| `sources/source-a-legacy-vpn.md` | KEEP | Still valid for HQ employees and contractors |
| `sources/source-b-zero-trust-policy.md` | ADD | Defines partial supersession boundary |
| `sources/source-d-incident-postmortem.md` | ADD | Supports device compliance diagnosis for the branch rollout |

## Changeset

```text
CREATE  concepts/device-compliance.md
UPDATE  concepts/remote-access-authentication.md
UPDATE  entities/examplevpn-client.md
UPDATE  queries/demo-455.md
UPDATE  faq/demo-455-common-errors.md
ADD     sources/source-b-zero-trust-policy.md
ADD     sources/source-d-incident-postmortem.md
KEEP    source-a-legacy-vpn scope for HQ / contractor / Legacy VPN
FLAG    source-c FAQ as pre-migration and scope-limited
```

## Guardrails

- Do not delete the Legacy VPN path.
- Do not infer that Source B applies to contractors or HQ employees.
- Do not use Source D to diagnose non-branch populations.
- If office, employee type, device management, or access path is missing, ask a clarification question.
- Keep all generated pages in draft until reviewed.

## Validation checklist

- Structural lint: frontmatter, links, source page presence.
- Provenance validation: every resolved claim has source support.
- Semantic validation: each retained branch has an explicit applicability condition.
- Regression queries: branch managed device, HQ employee, contractor, unknown device state.
- Human review: IT owner confirms business policy before publish.
