---
type: query
title: Ambiguous DEMO-101 Clarification
description: Ambiguous DEMO-101 Clarification
sources:
- id: SRC-01
  resource: ../sources/vpn-common-qa.md
  title: SRC-01
- id: SRC-02
  resource: ../sources/examplevpn-error-reference.md
  title: SRC-02
generated:
  by: codex/in-session
  at: '2026-10-11T03:51:34.995084+00:00'
status: draft
synthetic: true
knowledge_as_of: '2030-02-01'
classification: public
owner: process:synthetic-enterprise-demo
access_scope: public
contains_pii: false
retention: permanent
redaction: none
---

# DEMO-101 就代表帳戶鎖定嗎？

> 合成教學知識草稿；依情境日期 2030-02-01 的六份來源整理，尚未人工內容驗證或發布。

## Answer

不能只憑 DEMO-101 確定原因。來源列有密碼錯誤、帳戶鎖定、到期及網路狀況等可能性，屬於診斷假設。[^SRC-01][^SRC-02]

請先確認是否收到明確的鎖定或密碼到期提示，並提供不含機密的完整錯訊及發生時間。必要時補充裝置管理狀態與公司網路是否可用；不要提供密碼或驗證碼。[^SRC-01]

取得確認資訊後，才分別選擇鎖定、到期或其他支援分支；目前不給單一解鎖動作，也不宣稱已找到原因。[^SRC-02]

## Related Pages

- [帳戶狀態](../concepts/account-state-and-recovery.md)
- [鎖定問答](account-locked.md)
- [到期問答](password-expired.md)

[^SRC-01]: [SRC-01](../sources/vpn-common-qa.md)
[^SRC-02]: [SRC-02](../sources/examplevpn-error-reference.md)
