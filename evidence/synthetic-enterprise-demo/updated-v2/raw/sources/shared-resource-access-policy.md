---
sourceId: SRC-05
title: Shared Resource Access Policy
owner: Example Access Management
version: "1.0"
effectiveDate: 2030-01-10
reviewDate: 2030-06-10
source_kind: synthetic-teaching
synthetic: true
language: zh-TW
---

> **合成教學資料：**組織、政策、系統、日期與程序均為虛構，不代表任何真實企業政策。

# 共享資源存取範圍

本政策範例說明遠端連線與資源授權是兩個不同判斷。使用者連上 ExampleVPN，只代表目前有一條遠端連線；是否可使用特定資源，仍依下列群組與網路條件判斷。

## 已定義的範圍

- **Branch Support 群組：**經 ExampleVPN 遠端連線時，可以使用 ExampleCRM；此情境不包含 TeamShare。
- **HQ Support 群組：**在公司網路上可提出 TeamShare 權限申請。申請不代表已核准或已生效。

HQ Support 申請時，請透過 ExampleDesk 提供申請人的使用者識別碼（虛構示例：`EMP-DEMO-001`）、邏輯資料夾名稱及所需角色。服務台會依既有核准流程檢視；若角色或資料夾用途不清楚，應先詢問，不可自行授予較高權限。

## 明確限制

Branch Support 即使已連上 ExampleVPN，也不能據此要求 TeamShare 存取。此申請流程不會覆蓋該遠端路徑限制。HQ Support 在公司網路上提出申請，也不表示系統已完成授權。不得把連線成功、群組名稱或已送出請求當成權限核准證明。

若使用者的群組、所在網路或要求角色未知，先向使用者釐清並保留未決狀態。此文件沒有說明任何檢索系統的受眾中繼資料、資料列過濾或存取控制實作；不可從本文推論系統已按群組限制檢索結果。

## 相關流程

ExampleVPN 故障請依 [SRC-01](vpn-common-qa.md) 分流。公司管理筆電設定見 [SRC-04](managed-laptop-remote-access.md)。臨時海外遠端存取需要個別核准，見 [SRC-06](overseas-access-request.md)；一般連線不會取代該程序。
