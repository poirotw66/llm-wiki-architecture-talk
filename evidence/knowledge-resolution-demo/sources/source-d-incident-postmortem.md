# Source D — Incident Postmortem: Branch DEMO-455 Spike

> Synthetic conference example. Not a real incident report.

- Incident date: 2026-09-12
- Population observed: branch-office full-time employees on company-managed new laptops after Zero Trust rollout
- Symptom: DEMO-455 during ExampleVPN sign-in
- Primary finding: the new laptop was not yet marked compliant in device management, so Conditional Access blocked sign-in
- First action for this population: verify device enrollment / compliance status, then sync device state
- Legacy credential reset did not resolve the majority of observed cases in this population
- Limitation: the postmortem does not cover headquarters employees or contractors still using Legacy VPN
