---
type: concept
title: Account State and Conditional Recovery
description: Scoped account recovery with retained baseline and expiry rules.
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
- id: SRC-04
  resource: ../sources/managed-laptop-remote-access.md
  title: SRC-04
- id: SRC-07
  resource: ../sources/account-recovery-update-v2.md
  title: SRC-07
generated:
  by: codex-cli/gpt-6.1-sol+maintainer-review
  at: '2026-10-11T04:09:29.016237+00:00'
status: draft
synthetic: true
knowledge_as_of: '2030-03-02'
classification: public
owner: process:synthetic-enterprise-demo
access_scope: public
contains_pii: false
retention: permanent
redaction: none
---

# 帳戶狀態與基準復原

> 合成教學知識草稿；保留 2030-02-01 的六份來源基準，另納入 SRC-07，情境日期為 2030-03-02；待人工內容審查。

## 狀態分流

- DEMO-101 可能與密碼錯誤、帳戶鎖定、密碼到期或網路有關；代碼本身不是診斷。先詢問明確的鎖定／到期提示與非機密錯訊。[^SRC-01][^SRC-02]
- 已確認鎖定：依發生日期與完整資格選擇第一步；僅 SRC-07 明示的條件改用自助入口，其餘保留服務台基準。[^SRC-03][^SRC-07]
- 已確認到期：使用公司管理筆電的獨立改密碼流程；公司網路與操作可用是前提。解鎖不會重設或延長到期密碼。[^SRC-02]
- 密碼錯誤或狀態未明：記錄線索並釐清，不擅自選擇鎖定分支。[^SRC-03]

## 已確認鎖定的日期與資格

2030-03-01 前的事件依當時基準處理；SRC-03 自 2030-01-10 起適用於全職員工與承包人員的已確認鎖定情境。自 2030-03-01 起，只有全職員工、正在使用公司管理筆電、已註冊自助帳戶復原三項都確認符合，第一步才改為前往虛構入口 <https://support.example.com/account-recovery> 嘗試自助復原。入口僅供教學，不能執行真實交易，也不是已完成復原的證據；完成後仍須由使用者確認結果。[^SRC-03][^SRC-07]

已確認為承包人員、裝置不受公司管理或尚未註冊自助復原者，沿用 ExampleDesk 服務台路徑；自助失敗或結果不明者轉由 Example IT Service Desk 處理。任一資格或發生日期未知時，先詢問缺漏項目再決定分支；資訊矛盾或無法確認時交服務台釐清，不承諾適用自助流程。[^SRC-07]

裝置受管理或完成裝置註冊，不代表使用者已註冊自助帳戶復原，必須分開確認。[^SRC-04]

服務台請求仍附識別與聯絡資訊、發生時間、非機密錯訊、裝置管理狀態、自助復原註冊狀態與已確認的帳戶狀態；不清楚的狀態可填未知。服務台檢視不代表已解鎖，不保證直接解除或特定處理時間。[^SRC-03][^SRC-07]

## 證據邊界

SRC-03 的來源摘要保留基準主張，SRC-07 只局部變更 SRC-01 與 SRC-03 的已確認鎖定第一步，不使所有舊文件失效。密碼到期、DEMO-202、DEMO-303、資源限制與海外核准流程不變。請求不得包含密碼、驗證碼、復原連結或其他登入秘密；文件未描述的例外交由服務台文件負責人確認，不自行擴大規則。[^SRC-03][^SRC-07]

## Related Pages

- [鎖定問答](../queries/account-locked.md)
- [到期問答](../queries/password-expired.md)
- [DEMO-101 分流](../queries/demo-101.md)
- [裝置與帳戶註冊的界線](device-and-account-enrollment.md)
- [ExampleDesk](../entities/exampledesk.md)
- [條件式更新來源](../sources/account-recovery-update-v2.md)

[^SRC-01]: [SRC-01](../sources/vpn-common-qa.md)
[^SRC-02]: [SRC-02](../sources/examplevpn-error-reference.md)
[^SRC-03]: [SRC-03](../sources/account-recovery-v1.md)
[^SRC-04]: [SRC-04](../sources/managed-laptop-remote-access.md)
[^SRC-07]: [SRC-07](../sources/account-recovery-update-v2.md)
