---
type: source
title: Account Recovery Baseline Procedure
description: Account Recovery Baseline Procedure
archive_slug: account-recovery-v1
sourceId: SRC-03
sources:
- id: archive
  resource: ../../raw/sources/account-recovery-v1.md
  title: Account Recovery Baseline Procedure
analysis_receipt:
  version: '1'
  sha256: 18436fbe2ee8fa264b995e84f47361dc2ca1e1a897e7d5ba9063b55040202e7f
  source_sha256: 8be47d524d37d33abd258fa27cab30b46bb4e41937bb18f25ea87b086ec26928
  generated_by: codex/in-session
  generated_at: '2026-10-11T03:49:06.774829+00:00'
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

# Account Recovery Baseline Procedure

## Summary

- 已確認帳戶鎖定時，基準是 ExampleDesk 服務台請求。[^archive]
- 來源明確區分鎖定、到期與未明狀態，禁止蒐集登入秘密。[^archive]

## Key Concepts

- [相關概念](../concepts/account-state-and-recovery.md)

## Entities

- [ExampleVPN](../entities/examplevpn.md)
- [ExampleDesk](../entities/exampledesk.md)

## Notable Claims

- 已確認帳戶鎖定時，提交 ExampleDesk 帳戶復原請求，由服務台檢視。[^archive]
- 復原請求需附非機密錯訊、時間及管理／復原註冊狀態；不清楚時可標未知。[^archive]
- 請求不得包含密碼、驗證碼或復原連結。[^archive]

## Limitations / Gaps

合成教學來源，無資訊性視覺資產，視覺轉換閘未適用。來源准入已核可；摘要與跨文件解讀仍為待人工內容審查的草稿。未執行任何解鎖、授權或海外啟用。

[^archive]: [Canonical archive](../../raw/sources/account-recovery-v1.md)
