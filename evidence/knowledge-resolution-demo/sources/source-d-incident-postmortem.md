# Source D — Incident Postmortem: Branch DEMO-455 Spike

> Synthetic conference example. Not a real incident report.

- Incident date: 2026-09-12
- Population observed: branch-office full-time employees on company-managed new laptops after Zero Trust rollout
- Symptom: DEMO-455 during ExampleVPN sign-in
- Sample: 50 DEMO-455 support cases reviewed during the first rollout week
- Observation: 37 of 50 reviewed cases occurred on devices whose compliance state was not yet completed in device management
- Interpretation: device compliance is a strong associated factor for this rollout population, but the postmortem does not prove it is the only or universal cause of DEMO-455
- Recommended first action for this population: verify device enrollment / compliance status, then sync device state before attempting credential reset
- Legacy credential reset did not resolve the majority of observed cases in this population
- Limitation: the postmortem does not cover headquarters employees or contractors still using Legacy VPN
- Limitation: the postmortem should not be generalized to unknown offices, unmanaged devices, or non-Zero-Trust access paths
