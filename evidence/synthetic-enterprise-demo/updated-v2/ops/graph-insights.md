# Graph insights

Generated: 2026-10-11

> Structural report from `scripts/wiki-graph-insights.py`; operational state is outside the OKF bundle.

## Summary

- pages scanned: 19
- isolated (degree ≤ 1): 0
- no inbound link: 0
- bridge pages (≥2 role dirs): 19
- one-way links: 44
- raw archives missing wiki/sources page: 0

## Isolated pages

- （無）

## No inbound link

- （無）

## Bridge pages

- [wiki/concepts/account-state-and-recovery.md](../wiki/concepts/account-state-and-recovery.md) — roles: concepts, entities, queries, sources
- [wiki/concepts/device-and-account-enrollment.md](../wiki/concepts/device-and-account-enrollment.md) — roles: concepts, entities, queries, sources
- [wiki/concepts/overseas-approval.md](../wiki/concepts/overseas-approval.md) — roles: concepts, entities, queries, sources
- [wiki/concepts/resource-access-boundaries.md](../wiki/concepts/resource-access-boundaries.md) — roles: entities, queries, sources
- [wiki/entities/exampledesk.md](../wiki/entities/exampledesk.md) — roles: queries, sources
- [wiki/entities/examplevpn.md](../wiki/entities/examplevpn.md) — roles: concepts, queries, sources
- [wiki/queries/account-locked.md](../wiki/queries/account-locked.md) — roles: concepts, entities, queries, sources
- [wiki/queries/demo-101.md](../wiki/queries/demo-101.md) — roles: concepts, queries, sources
- [wiki/queries/overseas-request.md](../wiki/queries/overseas-request.md) — roles: concepts, entities, sources
- [wiki/queries/password-expired.md](../wiki/queries/password-expired.md) — roles: concepts, entities, queries, sources
- [wiki/queries/teamshare-access.md](../wiki/queries/teamshare-access.md) — roles: concepts, entities, sources
- [wiki/queries/unknown-error.md](../wiki/queries/unknown-error.md) — roles: entities, queries, sources
- [wiki/sources/account-recovery-update-v2.md](../wiki/sources/account-recovery-update-v2.md) — roles: concepts, entities, queries, sources
- [wiki/sources/account-recovery-v1.md](../wiki/sources/account-recovery-v1.md) — roles: concepts, entities
- [wiki/sources/examplevpn-error-reference.md](../wiki/sources/examplevpn-error-reference.md) — roles: concepts, entities
- [wiki/sources/managed-laptop-remote-access.md](../wiki/sources/managed-laptop-remote-access.md) — roles: concepts, entities
- [wiki/sources/overseas-access-request.md](../wiki/sources/overseas-access-request.md) — roles: concepts, entities
- [wiki/sources/shared-resource-access-policy.md](../wiki/sources/shared-resource-access-policy.md) — roles: concepts, entities
- [wiki/sources/vpn-common-qa.md](../wiki/sources/vpn-common-qa.md) — roles: concepts, entities

## One-way links (A→B without B→A)

- wiki/concepts/account-state-and-recovery.md → wiki/concepts/device-and-account-enrollment.md
- wiki/concepts/account-state-and-recovery.md → wiki/entities/exampledesk.md
- wiki/concepts/account-state-and-recovery.md → wiki/sources/managed-laptop-remote-access.md
- wiki/concepts/device-and-account-enrollment.md → wiki/sources/examplevpn-error-reference.md
- wiki/concepts/device-and-account-enrollment.md → wiki/concepts/resource-access-boundaries.md
- wiki/concepts/device-and-account-enrollment.md → wiki/queries/demo-101.md
- wiki/concepts/overseas-approval.md → wiki/entities/exampledesk.md
- wiki/concepts/overseas-approval.md → wiki/sources/managed-laptop-remote-access.md
- wiki/concepts/overseas-approval.md → wiki/concepts/resource-access-boundaries.md
- wiki/concepts/resource-access-boundaries.md → wiki/entities/exampledesk.md
- wiki/concepts/resource-access-boundaries.md → wiki/sources/managed-laptop-remote-access.md
- wiki/entities/examplevpn.md → wiki/concepts/account-state-and-recovery.md
- wiki/queries/account-locked.md → wiki/concepts/device-and-account-enrollment.md
- wiki/queries/account-locked.md → wiki/sources/managed-laptop-remote-access.md
- wiki/queries/account-locked.md → wiki/sources/account-recovery-v1.md
- wiki/queries/demo-101.md → wiki/sources/examplevpn-error-reference.md
- wiki/queries/demo-101.md → wiki/sources/vpn-common-qa.md
- wiki/queries/demo-101.md → wiki/queries/password-expired.md
- wiki/queries/overseas-request.md → wiki/sources/overseas-access-request.md
- wiki/queries/overseas-request.md → wiki/concepts/resource-access-boundaries.md
- wiki/queries/password-expired.md → wiki/sources/examplevpn-error-reference.md
- wiki/queries/password-expired.md → wiki/sources/vpn-common-qa.md
- wiki/queries/password-expired.md → wiki/entities/exampledesk.md
- wiki/queries/teamshare-access.md → wiki/sources/shared-resource-access-policy.md
- wiki/queries/teamshare-access.md → wiki/sources/managed-laptop-remote-access.md
- wiki/queries/teamshare-access.md → wiki/entities/examplevpn.md
- wiki/queries/unknown-error.md → wiki/entities/exampledesk.md
- wiki/queries/unknown-error.md → wiki/sources/examplevpn-error-reference.md
- wiki/queries/unknown-error.md → wiki/queries/demo-101.md
- wiki/sources/account-recovery-update-v2.md → wiki/concepts/device-and-account-enrollment.md
- wiki/sources/account-recovery-update-v2.md → wiki/sources/examplevpn-error-reference.md
- wiki/sources/account-recovery-update-v2.md → wiki/sources/vpn-common-qa.md
- wiki/sources/account-recovery-update-v2.md → wiki/sources/shared-resource-access-policy.md
- wiki/sources/account-recovery-update-v2.md → wiki/sources/overseas-access-request.md
- wiki/sources/account-recovery-update-v2.md → wiki/sources/account-recovery-v1.md
- wiki/sources/account-recovery-update-v2.md → wiki/concepts/overseas-approval.md
- wiki/sources/account-recovery-update-v2.md → wiki/entities/examplevpn.md
- wiki/sources/account-recovery-update-v2.md → wiki/queries/password-expired.md
- wiki/sources/account-recovery-update-v2.md → wiki/concepts/resource-access-boundaries.md
- wiki/sources/account-recovery-update-v2.md → wiki/queries/demo-101.md
- wiki/sources/account-recovery-v1.md → wiki/entities/examplevpn.md
- wiki/sources/examplevpn-error-reference.md → wiki/entities/exampledesk.md
- wiki/sources/managed-laptop-remote-access.md → wiki/entities/exampledesk.md
- wiki/sources/vpn-common-qa.md → wiki/entities/exampledesk.md

## Raw archives without wiki/sources page

- （無）

## Agent follow-up

- Review isolated / no-inbound pages for missing cross-links.
- Scan bridge pages for **contradictions** (Agent judgment; not auto-detected).
- Create missing wiki/sources pages for raw archives (ingest guarantee).
