# Compilation Target — VPN / FortiClient Knowledge Cluster

This file defines the expected output shape for a local Knowledge Compilation run using the selected Teams Agent VPN sources.

## Input source cluster

```text
Teams Agent local corpus
  data/sources/VPN常見Q&A問答.md
  data/sources/登入 FortiClient 出現錯訊.md
  data/sources/VPN國外連線短暫申請.md
  data/sources/內網筆電 VPN 連線問題.md
  data/sources/VPN 跳板機連線異常.md
```

## Target wiki artifacts

```text
sources/
  vpn-common-qa.md
  forticlient-errors.md
  vpn-overseas-temporary-access.md
  internal-laptop-vpn.md
  vpn-jump-host.md

concepts/
  vpn-troubleshooting.md
  vpn-error-codes.md
  vpn-credentials.md
  vpn-access-policy.md
  escalation-and-approval.md
  knowledge-boundary.md

entities/
  forticlient.md
  vpn.md

queries/
  vpn-455.md
  vpn-password-expired.md
  vpn-overseas-temporary-access.md
  vpn-619-no-answer.md
```

## What the run should demonstrate

### 1. Multi-source troubleshooting

`vpn-455.md` should be able to cite both broad VPN Q&A and FortiClient-specific error material, while keeping the exact `-455 / Permission denied` claim separate from unrelated VPN errors.

### 2. Cross-document synthesis

`vpn-password-expired.md` should preserve the symptom from the VPN Q&A and the concrete action from the FortiClient companion document. The purpose is to show that compilation captures reusable synthesis that would otherwise be repeated at query time.

### 3. Process knowledge

`vpn-overseas-temporary-access.md` should be modeled as a procedure with approval / CC / escalation roles. It should not be flattened into a generic VPN troubleshooting paragraph.

### 4. Knowledge boundary

`vpn-619-no-answer.md` should explicitly state that the current compiled corpus does not support an answer for Error `-619`. This is a feature, not a failure: the knowledge layer should represent unknowns and no-answer boundaries.

## Mutation plan for the demo run

```text
CREATE  concepts/vpn-error-codes.md
CREATE  concepts/vpn-credentials.md
CREATE  concepts/vpn-access-policy.md
CREATE  concepts/knowledge-boundary.md
CREATE  entities/forticlient.md
CREATE  queries/vpn-455.md
CREATE  queries/vpn-password-expired.md
CREATE  queries/vpn-overseas-temporary-access.md
CREATE  queries/vpn-619-no-answer.md
LINK    sources -> claims -> queries
EVAL    four regression cases from regression-cases.json
```

## Success condition

A minimal successful run does not need to be a large benchmark. It only needs to produce artifacts that prove the architecture claim:

> Knowledge Compilation moves repeated query-time interpretation into reviewable, versioned, testable update-time artifacts.
