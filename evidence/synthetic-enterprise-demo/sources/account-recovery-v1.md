---
sourceId: SRC-03
title: Account Recovery Baseline Procedure
owner: Example IT Service Desk
version: "1.0"
effectiveDate: 2030-01-10
reviewDate: 2030-06-10
source_kind: synthetic-teaching
synthetic: true
language: zh-TW
---

> **合成教學資料：**組織、政策、系統、日期與程序均為虛構，不代表任何真實企業政策。

# 帳戶鎖定復原基準流程

本文件記錄 2030-01-10 起使用的鎖定復原基準。DEMO-101 只是可能的診斷線索，不能單獨證明帳戶已鎖定。處理前須區分以下狀態：

- **已確認鎖定：**使用者或支援流程已有明確鎖定訊息。
- **密碼到期：**使用者收到到期提示或以核准方式確認到期；依 [SRC-02](examplevpn-error-reference.md) 的到期步驟處理。
- **密碼錯誤或未明：**沒有足夠證據確認鎖定或到期，先記錄情況並釐清。

## 基準處理方式

已確認鎖定時，使用者透過 ExampleDesk 提交帳戶復原請求，交由 Example IT Service Desk 檢視。此基準流程不表示服務台人員一定會直接解除鎖定，也不承諾特定處理時間。後續操作須依核實結果與支援流程決定。

請求應包含：

1. 使用者識別資訊與聯絡方式。
2. 不含秘密的錯誤文字或代碼，以及發生時間。
3. 裝置是否由公司管理；若不清楚，填「未知」。
4. 自助復原是否已註冊；若不清楚，填「未知」。
5. 使用者已確認的狀態，例如「收到鎖定提示」或「尚未確認」。

不得在請求中放入密碼、驗證碼、復原連結或其他登入秘密。請求內容應足以讓服務台判斷下一步，而不是要求服務台依單一代碼猜測原因。

## 範圍與時間

此版本適用於全職員工與承包人員的已確認帳戶鎖定情境，直到有明確範圍的變更生效。後續變更須明示取代的段落、條件與生效日；不可只按文件日期採取「較新文件全面取代較舊文件」的規則。

本流程不描述密碼到期處理、網路診斷、授權或資源權限；相關範圍分別見 [SRC-02](examplevpn-error-reference.md)、[SRC-04](managed-laptop-remote-access.md) 與 [SRC-05](shared-resource-access-policy.md)。
