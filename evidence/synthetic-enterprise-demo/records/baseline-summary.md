# 基準編譯結果

本頁保留基準編譯當時的結果與狀態；後續實際問答與更新回歸已完成，見 [新實驗結果](experiment-summary.md)。

已沿用既有 `llm-wiki-example` 的 Ingest 規約與工具，將使用者核可的六份合成來源編成獨立草稿快照。沒有新增編譯器，也沒有把資料匯入既有專案的 active Wiki。

| 項目 | 本輪結果 |
|---|---|
| 情境日期 | `2030-02-01`，使用 `SRC-01` 至 `SRC-06`。 |
| 來源封存 | 六組 original／canonical 副本，與核可 digest 相符；12 筆 lineage receipts。 |
| 編譯產物 | 18 頁：六份來源摘要、四份概念、兩份實體、六份可重用問答。全部 `draft`。 |
| Claim 追溯 | 17 項 claim，保存原文摘錄、來源 ID、適用條件與限制。 |
| 結構檢查 | 既有 Wiki lint 通過；Graph 掃描 18 頁，孤立頁及缺摘要的歸檔均為零。 |
| 十題靜態覆蓋 | 10／10 題找到對應草稿內容與必要來源；這不是答案正確率。 |
| 人工內容審查 | 三項待審：帳戶分流、角色與路徑、海外核准流程。來源准入核可不等於內容驗證。 |
| 問答／更新實驗 | 實際十題回答、SRC-07 更新編譯與回歸尚未執行。 |

## 可直接查看的材料

- [基準 Wiki 索引](../baseline-v1/wiki/index.md)
- [十題測試契約](../contracts/README.md)
- [Claim 與原文依據](baseline-claim-map.json)
- [逐題靜態覆蓋紀錄](baseline-contract-coverage.json)
- [來源與產物完整性檢查](baseline-integrity.json)
- [實際命令、exit code 與輸出](baseline-run.json)
- [人工內容審查清單](../baseline-v1/ops/review-queue.md)
- [既有專案保留檢查](existing-project-preservation.json)

## 結果的解讀範圍

這次編譯由目前 Codex 工作階段依來源進行編寫，接著作 Agent 來源比對及工具檢查；沒有另呼叫模型 API。工作階段先前討論過 SRC-07，因此不是來源盲測。可驗證的是基準歸檔與引用僅使用六份來源，不能宣稱模型上下文完全未見過更新內容。

模型精確版本、tokens 與成本均未量測。既有 telemetry 工具無法取得開始快照，因此未寫入零 token 紀錄。Lint 沒有傳入 Git base，沒有主張通過跨版本的 raw 不可變或 append-only 歷史檢查；本輪封存完整性另以 digest 檢查。

Graph 只描述連結結構，沒有自動驗證矛盾或政策適用性。工具產生的報告有 18 個相對連結需要依 `ops/` 位置調整，已只修正此示範報告並保存前後 digest；既有專案程式碼未修改。

三個人工 review 項目保持開啟。私有分析與 cache 位於快照的 `.llm-wiki/`，已列入忽略規則；公開頁面保留 analysis receipts。主要來源檔保留，沒有執行清除、提交、推送或發布。

## 下一個實驗

先以相同十題取得基準實際回答並保存逐條判定，再用 SRC-07 製作更新提案、知識 diff 與相同問題的回歸。必須分開觀察 SYN-01 的預期變動，以及其餘九題的保留行為；完成實際回答與審查後，再將結果放入簡報。
