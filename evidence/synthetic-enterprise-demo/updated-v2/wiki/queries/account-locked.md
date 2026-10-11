---
type: query
title: Conditional Account Lock Recovery
description: Time and eligibility conditions for account lock recovery.
sources:
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

# 帳戶已確認鎖定時怎麼處理？

> 合成教學知識草稿；保留 2030-02-01 的六份來源基準，另納入 SRC-07，情境日期為 2030-03-02；待人工內容審查。

## Question

帳戶已明確顯示鎖定，依發生日期、身分類型、裝置管理狀態與自助帳戶復原註冊狀態，應採用哪個第一步？

## Answer

先確認發生日期，以及使用者是否為全職員工、是否正在使用公司管理筆電、是否已註冊自助帳戶復原。任一項未知時先詢問缺漏項目，再決定分支；資訊矛盾或無法確認時交由服務台釐清，不承諾適用自助復原。[^SRC-07] 裝置受管理或已完成裝置註冊，不能證明使用者已註冊自助帳戶復原。[^SRC-04]

- 2030-01-10 至 2030-02-28 發生的已確認鎖定事件，仍採下述 ExampleDesk 基準流程。[^SRC-03][^SRC-07]
- 自 2030-03-01 起，在本次情境日期範圍內，三項資格都確認符合者，第一步前往虛構入口 <https://support.example.com/account-recovery> 嘗試自助復原。此入口僅供教學，不能執行真實交易，也不能證明已完成復原；完成後仍須由使用者確認結果。若流程失敗或結果不明，轉由 Example IT Service Desk 處理。[^SRC-07]
- 已確認為承包人員、裝置不受公司管理或尚未註冊自助復原者，沿用下述 ExampleDesk 基準流程。資格或日期未知時仍先釐清，不推定符合自助條件。[^SRC-07]

服務台基準流程：透過 ExampleDesk 提交帳戶復原請求，由 Example IT Service Desk 檢視。附上識別與聯絡資訊、非機密錯訊、發生時間、裝置管理狀態、復原註冊狀態及已確認的帳戶狀態；不清楚的狀態填未知。請求中不得包含密碼、驗證碼、復原連結或其他登入秘密。[^SRC-03][^SRC-07]

本文僅整理適用流程。服務台收到請求不代表已解除鎖定，也不保證直接解除或特定處理時間。若問題實際是密碼到期，仍走另頁的獨立密碼更新流程，不能以鎖定復原替代。[^SRC-03][^SRC-07]

## Applicability

必須先確認帳戶鎖定；DEMO-101 或資格資料本身不能替代鎖定確認。SRC-03 的基準自 2030-01-10 起適用於全職員工與承包人員；SRC-07 自 2030-03-01 起只改變完整符合資格者的第一步，其餘服務台程序保留。[^SRC-03][^SRC-07]

例如 2030-01-20 的已確認鎖定事件位於基準生效期間，仍採服務台流程，不因現在符合自助條件而改判。[^SRC-03][^SRC-07] 本草稿整理至情境日期 2030-03-02；早於 2030-01-10 或晚於本次情境日期的事件，資料不足時不自行推論適用政策。文件未描述的例外，記錄後交由 Example IT Service Desk 的文件負責人確認。[^SRC-07]

## Related Pages

- [帳戶狀態](../concepts/account-state-and-recovery.md)
- [裝置與帳戶註冊的界線](../concepts/device-and-account-enrollment.md)
- [DEMO-101](demo-101.md)
- [密碼到期](password-expired.md)
- [ExampleDesk](../entities/exampledesk.md)
- [基準來源摘要](../sources/account-recovery-v1.md)
- [條件式更新來源](../sources/account-recovery-update-v2.md)

[^SRC-03]: [SRC-03](../sources/account-recovery-v1.md)
[^SRC-04]: [SRC-04](../sources/managed-laptop-remote-access.md)
[^SRC-07]: [SRC-07](../sources/account-recovery-update-v2.md)
