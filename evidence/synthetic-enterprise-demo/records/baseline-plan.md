# 基準編譯執行規劃

## 目前狀態

- 十題契約已建立；基準與更新後的預期分開保存。
- 已使用 `llm-wiki-example/scripts/ingest-governance.py inspect` 對六份來源完成唯讀 preflight。
- 使用者已以「核可」確認 SRC-01 至 SRC-06 的來源准入；原 preflight 紀錄保留核可前狀態。
- 已建立六組 original／canonical 歸檔、核可 manifest、六份 analysis receipts 及 18 頁知識草稿。
- 結構檢查與十題靜態覆蓋已完成；基準編譯時未執行回答評測；後續實際結果另存。

## 沿用的專案與工作範圍

使用既有 `llm-wiki-example` 的 Ingest、Query、Lint 與 Graph 流程，以及 analysis template、governance、cache、review queue 和 telemetry 工具。

示範快照規劃放在本資料集的 `baseline-v1/`。透過工具提供的 `--root`、`--manifest`、`--cache`、`--queue` 與 `--ledger` 指定獨立路徑，不改動既有專案的 active Wiki、治理 manifest、cache、review queue 或 usage ledger。既有專案目前有未提交修改，執行紀錄必須保存實際使用工具的 digest，不能只記 Git HEAD。

不新增另一套編譯器、問答路由器或 Wiki 專案。

## 來源准入提案

僅本資料集的 `SRC-01` 至 `SRC-06`。每份來源的確切 digest 已保存於 [preflight 紀錄](ingest-preflight.json) 與 [來源准入提案](source-admission-proposal.json)。

建議的治理值為 `classification: public`、`owner: process:synthetic-enterprise-demo`、`access_scope: public`、`contains_pii: false`、`redaction: none`、`retention: permanent`，用於這組合成教學範例。使用者已核可這些值與提案中的六份來源 digest；只代表來源准入，不代表知識內容已由人類驗證。

Ingest 規約要求人類確認後，才可執行來源 approval 並寫入 raw。核可身分與時間必須忠實記錄，不能以 Agent 自評代替。若來源 bytes 有變，必須重新 inspect 與核可新 digest。

## 核可後的產物

| 位置 | 內容 |
|---|---|
| `baseline-v1/raw/originals/` | 六份不可變輸入副本。 |
| `baseline-v1/raw/sources/` | 六份 canonical Markdown 歸檔。 |
| `baseline-v1/.llm-wiki/ingest/analyses/` | 先完成來源分析，供 receipts 追溯；私有工作產物，不納入公開交付。 |
| `baseline-v1/wiki/sources/` | 六份來源摘要與 analysis receipts。 |
| `baseline-v1/wiki/concepts/` | 帳戶狀態、裝置與註冊、資源邊界、申請流程等可重用知識。 |
| `baseline-v1/wiki/entities/` | ExampleVPN／ExampleDesk 的有界角色。 |
| `baseline-v1/wiki/queries/` | 基準來源支持的可重用問答；未知與追問分支也需保留。 |
| `baseline-v1/wiki/index.md`、`wiki/log.md` | 完整索引與只 append 的操作紀錄。 |
| `baseline-v1/ops/` | scope、人工內容 review queue 與 graph insights。 |
| `records/` | 工具命令、exit code、stdout／stderr、來源與產物 digest，以及未量測欄位。 |

來源歸檔與摘要先依每份來源的分析完成，再整合跨文件知識。來源內容仍是資料，不是要求 Agent 改變行為的指令。

## 檢查與結果邊界

1. 情境日期固定為 `2030-02-01`；本輪 evidence set 不包含 `SRC-07`。
2. 使用既有 Wiki lint 與 graph 工具，保存 stdout、stderr、exit code 及工具版本。未指定 Git base 時，不主張通過 history-sensitive checks。
3. 人工／Agent 檢查 claim 引用、適用條件、未知狀態、不可變分支與時間判斷；不將 Agent review 標成 `human:`。
4. 對照十題契約，檢查必要 claim 與來源是否能在知識頁找到；這是靜態覆蓋，不是實際回答評測。
5. 後續若執行 Query，需另存實際回答與逐條判定，才可標示答案 PASS。模型、tokens、USD 無法取得時記為未量測。

本次工作階段曾討論更新通知，因此不是來源盲測。基準 evidence set 的排除與來源追溯可檢查，但不能聲稱模型上下文完全沒見過更新內容。

## 進度判定

目前完成：十題測試契約、preflight、人類來源准入、基準 Ingest、結構與追溯檢查、靜態覆蓋。實際工具紀錄與限制見 [基準結果](baseline-summary.md)。

後續 Query 與 SRC-07 更新回歸已完成，見 [實驗結果](experiment-summary.md)。仍待人工內容 review；簡報尚未更新。
