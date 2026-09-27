# Claim-level Resolution

This worked example shows why a knowledge layer cannot simply prefer the newest document or merge all retrieved chunks into one answer.

## User context

- Location: Tainan branch office
- Employment type: full-time employee
- Device: company-managed new laptop
- Access path: ExampleVPN after Zero Trust rollout
- Error: DEMO-455

## Resolution table

| Claim | Status | Applies when | Source support | Resulting knowledge |
|---|---|---|---|---|
| DEMO-455 is commonly credential validation failure | Still true, but scoped | Legacy VPN users | Source A, Source C | Keep for HQ employees and contractors on Legacy VPN |
| Branch full-time employees on managed devices moved to Zero Trust | Active business rule | Branch full-time + managed device | Source B | Supersedes Legacy VPN first action for this population |
| Branch managed-device DEMO-455 after rollout is associated with incomplete device compliance | Active incident evidence, not universal causation | Branch full-time + managed new laptop after rollout | Source D: 37 / 50 reviewed cases had incomplete compliance state | Prioritize device enrollment / compliance sync before credential reset |
| DEMO-455 is caused by device compliance for everyone | False overgeneralization | — | Source D explicitly limits population and evidence strength | Do not rewrite all DEMO-455 guidance as compliance-only |
| New policy invalidates all v4.0 troubleshooting | False | — | Source B explicitly limits supersession | Preserve v4.0 / Legacy VPN branch |
| If user context is unknown, provide one universal step | False | Missing employment type, office, or device state | Source B | Ask clarification first |

## Evidence wording discipline

Wrong wiki wording:

> DEMO-455 is caused by device compliance.

Better wiki wording:

> During the branch Zero Trust rollout, incomplete device compliance was observed in 37 of 50 reviewed DEMO-455 cases. For branch full-time employees on company-managed devices, check enrollment and compliance state first, then retry sign-in.

The second wording preserves scope and evidence strength. It turns incident evidence into a priority order, not a universal causal law.

## Final answer for the fixed question

For a Tainan branch full-time employee using a company-managed new laptop after the Zero Trust rollout, DEMO-455 should first be treated as a likely device compliance / enrollment issue. Verify device enrollment, sync device state, then retry sign-in. If the error remains, escalate to Service Desk with device compliance evidence.

This answer should cite Source B for applicability and Source D for the incident-specific troubleshooting priority. It should not cite only Source C, because that FAQ lacks the Zero Trust scope split.

## Knowledge design consequence

The resolved page should store the branch / managed-device path separately from the Legacy VPN path. Otherwise the wiki would encode a single answer that is wrong for at least one valid population.
