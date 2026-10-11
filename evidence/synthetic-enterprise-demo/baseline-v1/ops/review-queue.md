# Review Queue

Human-in-the-loop items. Governance items created during preflight block that
source's ingest; editorial Ingest／Lint items remain asynchronous.
Close items with ``uv run python scripts/ingest-review.py close --id <id>``.

## Open

- [ ] id: 49d2edf8 | ingest | Verify baseline account-state routing
  - reason: Source admission was approved by the user; compiled content remains an agent-authored draft. Verify confirmed lock, ambiguity, password expiry, historical scope and secret exclusions against SRC-01 through SRC-03.
  - suggested_action: human_verify
  - related: `wiki/concepts/account-state-and-recovery.md`
  - created: 2026-10-11T03:54:01Z

- [ ] id: 8f7582ed | ingest | Verify role and network applicability
  - reason: Verify Branch Support remote restrictions, HQ Support corporate-network application and unknown-context questions. Confirm that compiled policy text does not imply implemented retrieval ACLs.
  - suggested_action: human_verify
  - related: `wiki/concepts/resource-access-boundaries.md`
  - created: 2026-10-11T03:54:01Z

- [ ] id: 49823435 | ingest | Verify overseas approval sequence
  - reason: Verify application fields, manager-first approval, Network Operations and Security Review handoff, activation boundaries and date-limited validity against SRC-06.
  - suggested_action: human_verify
  - related: `wiki/concepts/overseas-approval.md`
  - created: 2026-10-11T03:54:01Z

## Done
