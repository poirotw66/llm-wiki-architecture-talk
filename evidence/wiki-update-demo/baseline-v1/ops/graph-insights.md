# Graph insights

Generated: 2026-09-27

> Structural report from `scripts/wiki-graph-insights.py`; operational state is outside the OKF bundle.

## Summary

- pages scanned: 4
- isolated (degree ≤ 1): 0
- no inbound link: 0
- bridge pages (≥2 role dirs): 4
- one-way links: 2
- raw archives missing wiki/sources page: 0

## Isolated pages

- （無）

## No inbound link

- （無）

## Bridge pages

- [wiki/concepts/device-enrollment.md](../concepts/device-enrollment.md) — roles: entities, queries, sources
- [wiki/entities/examplevpn-client.md](../entities/examplevpn-client.md) — roles: concepts, sources
- [wiki/queries/demo-101.md](../queries/demo-101.md) — roles: concepts, entities, sources
- [wiki/sources/examplevpn-guide-v1.md](../sources/examplevpn-guide-v1.md) — roles: concepts, entities

## One-way links (A→B without B→A)

- wiki/queries/demo-101.md → wiki/entities/examplevpn-client.md
- wiki/queries/demo-101.md → wiki/sources/examplevpn-guide-v1.md

## Raw archives without wiki/sources page

- （無）

## Agent follow-up

- Review isolated / no-inbound pages for missing cross-links.
- Scan bridge pages for **contradictions** (Agent judgment; not auto-detected).
- Create missing wiki/sources pages for raw archives (ingest guarantee).
