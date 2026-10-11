---
sourceId: SRC-07
title: Conditional Account Recovery Update
owner: Example IT Service Desk
version: "2.0"
effectiveDate: 2030-03-01
reviewDate: 2030-06-10
source_kind: synthetic-teaching
synthetic: true
language: zh-TW
---

> **合成教學資料：**組織、政策、系統、日期與程序均為虛構，不代表任何真實企業政策。以下入口網站是虛構佔位網址，沒有實際服務或交易。

# 帳戶復原條件式更新通知

自 2030-03-01 起，本通知只變更「已確認帳戶鎖定」時的第一步，而且必須同時符合下列三項條件：

1. 使用者是全職員工。
2. 使用者正在使用公司管理筆電。
3. 使用者已註冊自助帳戶復原。

三項都確認為符合時，請使用者前往虛構入口網站 <https://support.example.com/account-recovery> 嘗試自助復原。此連結僅供教學示例，不能執行真實交易，也不可視為已完成復原的證據。完成後仍須由使用者確認結果；若流程失敗或狀態不明，轉由 Example IT Service Desk 處理。

## 不符合或未知

已確認為承包人員、不受公司管理的裝置，或尚未註冊自助復原時，沿用 [SRC-03](account-recovery-v1.md) 的 ExampleDesk 服務台路徑。符合自助條件但自助復原失敗者，也轉服務台。

若任一資格條件或情境日期未知，先追問使用者身分類型、裝置管理狀態、自助復原註冊狀態或發生日期中的缺漏項目，再決定適用分支。不要為了使用入口網站而推定資格；若資訊互相矛盾或無法確認，交由服務台釐清，不承諾適用自助復原。

## 取代範圍矩陣

| 基準文件與段落 | 2030-03-01 起的變更 | 仍適用的部分 |
| --- | --- | --- |
| [SRC-01](vpn-common-qa.md)：DEMO-101 中「已確認鎖定」的服務台第一步 | 僅符合上述三項條件者，第一步改為嘗試自助復原 | 其他 DEMO-101 原因、診斷方式與不符合者的服務台路徑不變 |
| [SRC-03](account-recovery-v1.md)：已確認鎖定的基準復原入口 | 僅符合三項條件者，先走本通知的虛構自助入口 | 其餘使用者仍由 ExampleDesk 提交請求；不得蒐集秘密，也不保證服務台會直接解除鎖定 |

本通知不變更 [SRC-02](examplevpn-error-reference.md) 的密碼到期程序、DEMO-202 網路診斷、DEMO-303 裝置註冊或授權檢查、[SRC-05](shared-resource-access-policy.md) 資源規則，亦不變更 [SRC-06](overseas-access-request.md) 海外核准流程。到期密碼仍依公司網路與 Ctrl+Alt+Delete 的虛構程序處理，不能以鎖定復原替代。

## 時間判斷

2030-03-01 之前發生的情境依當時基準處理；自生效日起才依本通知的完整資格條件套用新第一步。這是局部更新，不代表所有舊文件失效。若文件未說明的例外出現，記錄問題並交由 Example IT Service Desk 的文件負責人確認，不要自行擴大適用範圍。
