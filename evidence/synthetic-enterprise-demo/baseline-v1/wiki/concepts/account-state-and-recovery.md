---
type: concept
title: Account State and Baseline Recovery
description: Account State and Baseline Recovery
sources:
- id: SRC-01
  resource: ../sources/vpn-common-qa.md
  title: SRC-01
- id: SRC-02
  resource: ../sources/examplevpn-error-reference.md
  title: SRC-02
- id: SRC-03
  resource: ../sources/account-recovery-v1.md
  title: SRC-03
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

# 帳戶狀態與基準復原

> 合成教學知識草稿；依情境日期 2030-02-01 的六份來源整理，尚未人工內容驗證或發布。

## 狀態分流

- DEMO-101 可能與密碼錯誤、帳戶鎖定、密碼到期或網路有關；代碼本身不是診斷。先詢問明確的鎖定／到期提示與非機密錯訊。[^SRC-01][^SRC-02]
- 已確認鎖定：提交 ExampleDesk 復原請求，附發生時間與非機密錯訊；裝置管理與復原註冊不清楚時可填未知。服務台檢視不代表已解鎖，也不保證直接解除。[^SRC-03]
- 已確認到期：使用公司管理筆電的獨立改密碼流程；公司網路與操作可用是前提。解鎖不會重設或延長到期密碼。[^SRC-02]
- 密碼錯誤或狀態未明：記錄線索並釐清，不擅自選擇鎖定分支。[^SRC-03]

## 證據邊界

本快照僅記錄服務台基準流程；不得從使用者自稱已註冊某服務推導出未收錄的處理規則。請求不得包含密碼、驗證碼或復原連結。[^SRC-03]

## Related Pages

- [鎖定問答](../queries/account-locked.md)
- [到期問答](../queries/password-expired.md)
- [DEMO-101 分流](../queries/demo-101.md)
- [ExampleDesk](../entities/exampledesk.md)

[^SRC-01]: [SRC-01](../sources/vpn-common-qa.md)
[^SRC-02]: [SRC-02](../sources/examplevpn-error-reference.md)
[^SRC-03]: [SRC-03](../sources/account-recovery-v1.md)
