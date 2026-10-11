---
type: entity
title: ExampleDesk Teaching Entity
description: ExampleDesk Teaching Entity
sources:
- id: SRC-03
  resource: ../sources/account-recovery-v1.md
  title: SRC-03
- id: SRC-05
  resource: ../sources/shared-resource-access-policy.md
  title: SRC-05
- id: SRC-06
  resource: ../sources/overseas-access-request.md
  title: SRC-06
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

# ExampleDesk

> 合成教學知識草稿；保留 2030-02-01 的六份來源基準，另納入 SRC-07，情境日期為 2030-03-02；待人工內容審查。

ExampleDesk 是虛構服務台的請求入口。基準帳戶鎖定請求交由服務台檢視，應提供非機密錯訊與必要狀態；提交請求不代表已解除鎖定。[^SRC-03]

自 2030-03-01 起，已確認鎖定且同時符合全職員工、正在使用公司管理筆電及已註冊自助帳戶復原者，第一步改為嘗試 SRC-07 的虛構自助入口。已確認不符合者仍走 ExampleDesk；自助失敗或結果不明者轉服務台。任一資格或發生日期未知時先詢問缺漏資訊，矛盾或無法確認時交服務台釐清；生效日前的事件保留當時基準。[^SRC-07]

HQ Support 在公司網路的 TeamShare 申請也透過此入口，但不能覆蓋 Branch Support 遠端限制，更不表示已核准。[^SRC-05]

海外接入先補齊資料並經主管核准，再轉交 Network Operations 及 Security Review；只有獲准才安排啟用。[^SRC-06]

## Related Pages

- [鎖定問答](../queries/account-locked.md)
- [條件式更新來源](../sources/account-recovery-update-v2.md)
- [TeamShare 問答](../queries/teamshare-access.md)
- [海外申請](../queries/overseas-request.md)

[^SRC-03]: [SRC-03](../sources/account-recovery-v1.md)
[^SRC-05]: [SRC-05](../sources/shared-resource-access-policy.md)
[^SRC-06]: [SRC-06](../sources/overseas-access-request.md)
[^SRC-07]: [SRC-07](../sources/account-recovery-update-v2.md)
