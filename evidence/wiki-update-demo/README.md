# Wiki 來源更新：可檢查的合成案例

本案例是簡報的實際產物證據。來源為本任務撰寫的虛構 ExampleVPN 指南，知識頁與修訂由本輪互動式 Assistant 撰寫；既有 `wiki-lint.py` 與 `wiki-graph-insights.py` 已在獨立 fixture 上執行。Python 用於保存快照、metadata、diff 與工具輸出，沒有呼叫另一個模型 API。

它不是自動 `/ingest`、RAG 問答、Teams 串接或正式發布的端到端測試。問答頁是持久化的 Agent 草稿，所有頁面保留 `draft`，沒有虛構人工核可。未執行來源准入的 governance gate；此處是公開合成測試 fixture，不是已核可的生產知識 bundle。

## 案例變更

- v1：受管理筆電、ExampleVPN 4.x、DEMO-101，由示範服務台確認登錄。
- v2：4.1 及以上先使用合成介面的「同步裝置狀態」一次，仍失敗再交服務台；4.0 保留 v1 流程。v2 明確限制取代範圍。
- 固定問題：受管理筆電、ExampleVPN 4.1、DEMO-101 應如何處理？

來源、錯誤碼、操作與組織均為虛構，不能作真實產品指引。

## 四份快照

| Snapshot | 準備方式 | Lint 結果 | 說明 |
|---|---|---|---|
| [baseline-v1](baseline-v1/wiki/index.md) | v1 來源及其知識頁 | Exit 0 | 只有 v1 時的初始草稿 |
| [stale-v2](stale-v2/wiki/index.md) | 故意新增 v2 來源與摘要，但保留三份 v1 下游頁 | Exit 0 | 結構有效；固定問題的回答少了 v2 的第一步 |
| [missing-summary-v2](missing-summary-v2/wiki/index.md) | 在獨立副本中故意移除 v2 來源摘要 | Exit 1，4 個問題 | 三個斷鏈及一個缺少來源摘要 |
| [revised-v2](revised-v2/wiki/index.md) | 更新 concept、entity、query 並保留兩版來源 | Exit 0 | 結構檢查通過，內容仍待人工 review |

`stale-v2` 與 `missing-summary-v2` 都是明確注入的教學故障，不是從 production 發現的 incident。對 stale-v2 的語義判斷來自此任務中的來源比對，不是 lint 或 graph script 的自動判定。

## 可直接放進簡報的證據

1. [v1 原始來源](baseline-v1/raw/originals/examplevpn-guide-v1.md) 與 [v2 原始來源](revised-v2/raw/originals/examplevpn-guide-v2.md)。來源本身已給出新增條件，Agent 不需要發明它。
2. [變更提案](decisions/v2-change-plan.md)：更新既有 concept、entity、query，保留 4.0 分支，新增 v2 source summary。
3. [舊問答](stale-v2/wiki/queries/demo-101.md) 與 [修訂問答](revised-v2/wiki/queries/demo-101.md)。
4. [實際三頁 diff](records/content-revision.diff)：來源 v1 改指 v2，正文補上版本分支與處理順序。
5. [結構有效但內容過時的 lint 輸出](records/stale-v2-wiki-lint.txt)。
6. [缺來源摘要時的 lint 輸出](records/missing-summary-v2-wiki-lint.txt)。
7. [修訂後的 lint 輸出](records/revised-v2-wiki-lint.txt)。
8. [修訂後 graph report](revised-v2/ops/graph-insights.md)：結構報告提供查閱線索，並非語義影響分析或正式驗收。
9. [待人工確認清單](revised-v2/ops/review-queue.md)。

## 重跑已保存快照的檢查

在 `/Users/cfh00896102/Github/hello-world` 執行：

```sh
../llm-wiki-example/.venv/bin/python ../llm-wiki-example/scripts/wiki-lint.py --root evidence/wiki-update-demo/baseline-v1
../llm-wiki-example/.venv/bin/python ../llm-wiki-example/scripts/wiki-lint.py --root evidence/wiki-update-demo/stale-v2
../llm-wiki-example/.venv/bin/python ../llm-wiki-example/scripts/wiki-lint.py --root evidence/wiki-update-demo/missing-summary-v2
../llm-wiki-example/.venv/bin/python ../llm-wiki-example/scripts/wiki-lint.py --root evidence/wiki-update-demo/revised-v2
```

第三條命令預期回傳 1。每條分別執行；勿用「全部 exit 0」作成功判準。graph script 會寫入選定 fixture 的 `ops/graph-insights.md`：

```sh
../llm-wiki-example/.venv/bin/python ../llm-wiki-example/scripts/wiki-graph-insights.py --root evidence/wiki-update-demo/revised-v2
```

以上重跑的是已保存產物的驗證，沒有重新產生 LLM 內容。工具版本與 hashes 記於 [runs.json](records/runs.json)；頁面生成方式與故障注入記於 [creation.json](records/creation.json)。未提供 `--base`，因此沒有執行 Git history-sensitive checks。

## 可主張的結果

- 本次確實建立了四份合成快照，執行既有工具，保存 stdout、stderr、exit code、命令、時間與工具版本。
- 更新前後的三份知識頁有可讀 diff。
- v1 原件與 canonical 在所有快照中的 SHA-256 相同；這是快照間雜湊比較，不是 Git 歷史或權限不可變性證明。
- 此刻意構造的案例中，結構 lint 沒有抓出語義上的更新遺漏。

## 仍未量測的項目

此案例不能證明自動 Ingest 的穩定性、RAG 準確率提升、人工工時節省、成本優勢、production ACL 或雲端驗收。三份修訂頁數來自預先構造的教學內容，不是維護影響範圍的統計估計。沒有人工 review 的完成紀錄。
