---
type: query
title: Confirmed Account Lock Baseline Answer
description: Confirmed Account Lock Baseline Answer
sources:
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

# 帳戶已確認鎖定時怎麼處理？

> 合成教學知識草稿；依情境日期 2030-02-01 的六份來源整理，尚未人工內容驗證或發布。

## Question

帳戶已明確顯示鎖定，應採用哪個流程？即使使用者是全職員工、使用公司管理筆電，或自稱已註冊某種復原服務，也只按此快照已收錄的基準處理。

## Answer

請透過 ExampleDesk 提交帳戶復原請求，由 Example IT Service Desk 檢視。附上識別與聯絡資訊、非機密錯訊、發生時間、裝置管理狀態、復原註冊狀態及已確認的帳戶狀態；不清楚的狀態填未知。請求中不得包含密碼、驗證碼或復原連結。[^SRC-03]

目前尚未替您解鎖，服務台收到請求也不保證直接解除鎖定。若問題實際是密碼到期，應使用另頁的密碼更新流程。[^SRC-03]

## Applicability

本基準適用於全職員工與承包人員的已確認鎖定情境。未確認鎖定時先釐清；本快照僅支持情境日期 2030-02-01 的既有規則。例如 2030-01-20 的已確認鎖定事件位於此基準生效期間，仍採服務台流程；早於 2030-01-10 或晚於本快照日期的事件，資料不足時不自行推論適用政策。[^SRC-03]

## Related Pages

- [帳戶狀態](../concepts/account-state-and-recovery.md)
- [DEMO-101](demo-101.md)
- [密碼到期](password-expired.md)
- [ExampleDesk](../entities/exampledesk.md)

[^SRC-03]: [SRC-03](../sources/account-recovery-v1.md)
