# 實際問答、SRC-07 更新與回歸結果

已完成兩階段共 20 則實際模型回答、一次更新提案，以及逐條回歸判定。凍結契約的整題通過數是 **基準 8／10、更新後 8／10**，兩階段均有兩題未通過；不是完整驗收成功。

## 核心觀察

- SYN-01 已依更新改為嘗試虛構自助入口：事件在生效日後、已確認鎖定，且全職員工、公司管理筆電、已註冊自助復原三項皆成立。失敗或結果不明仍轉服務台。
- 其餘九題的 route 與第一步保留；承包人員、未註冊者及 2030-01-20 的歷史事件仍走服務台。這只描述 route／第一步，並不表示九題都完整通過。
- 五份無關問答頁與六份原始來源摘要維持原 bytes；SRC-07 未全面取代舊文件。更新後共 19 頁草稿，23 項有來源摘錄的 claim。
- Lint 與歸檔完整性通過，實際回答仍有引用缺漏，支持將結構檢查與答案回歸分開。

## 十題結果

| 題目 | 基準 | 更新後 | 判讀 |
|---|---|---|---|
| SYN-01 · 符合自助資格的鎖定 | PASS | PASS | 第一步依預期改為自助復原 |
| SYN-02 · 承包人員鎖定 | PASS | PASS | route／第一步保留 |
| SYN-03 · 未註冊自助復原 | PASS | PASS | route／第一步保留 |
| SYN-04 · 生效前歷史事件 | PASS | PASS | route／第一步保留 |
| SYN-05 · DEMO-101 原因未明 | PASS | PASS | route／第一步保留；更新後另有一處繁簡混用 |
| SYN-06 · 密碼到期 | FAIL | FAIL | 兩階段均缺契約要求的 SRC-01 引用 |
| SYN-07 · Branch 遠端 TeamShare | FAIL | FAIL | 兩階段均缺 SRC-04；更新後回答亦漏 HQ 公司網路申請的區分 |
| SYN-08 · 資源情境未知 | PASS | PASS | route／第一步保留 |
| SYN-09 · 海外申請缺日期 | PASS | PASS | route／第一步保留 |
| SYN-10 · 未記載錯誤碼 | PASS | PASS | route／第一步保留 |

## 未通過與格式問題

SYN-06 只引用直接提供到期程序的 SRC-02，更新後另引用 SRC-07；凍結契約仍要求 SRC-01，因此兩階段均判引用覆蓋 FAIL。SYN-07 只引用 SRC-05，未滿足契約要求的 SRC-04；這些缺漏本身不證明流程事實錯誤，也不能靜默放寬原契約。

更新後 SYN-07 的使用者回答沒有說明 HQ Support 在公司網路的不同申請程序。獨立工作階段的模型評判把引用摘錄中的說明當成滿足；維護 Agent 檢查後明確覆寫該項為 FAIL，保留模型原判與覆寫理由。引用有正確原文，仍不能取代回答中要求的說明。

更新後 SYN-05 有一處繁簡混用，另記為提示詞格式缺陷；未改寫原始輸出，也未把此新增觀察混入凍結契約分數。所有實際引用摘錄均能在指定來源找到。

## 更新提案與修正

模型提出四個既有頁面的修改：index、帳戶狀態概念、ExampleDesk 實體與帳戶鎖定問答；另產生 SRC-07 來源摘要。維護 Agent 修正了模型保留舊六份來源 purpose 的提案，將 active 更新快照範圍改為七份來源，並補齊既有 lint 要求的 purpose schema。

這是 **Agent 審查與修正**，沒有偽造人類內容核可。四項人工 review 仍待完成，頁面全部為 draft；沒有發布、實際解鎖、資源啟用或企業 serving 驗收。

## 可查看的證據

- [二十則原始回答與引用](actual-answers.md)
- [逐題、逐條判定與維護者覆寫](regression-results.json)
- [原始模型更新提案](model-runs/update-proposal/response.json)
- [提案審查與修正](update-proposal-review.json)
- [知識差異](knowledge-update.diff)
- [更新後 Wiki](../updated-v2/wiki/index.md)
- [完整性檢查](updated-integrity.json)
- [執行方式與評判限制](execution-protocol.md)
- [實際命令與專案保留紀錄](update-regression-run.json)

## 演講可用的結論

可以展示「明確範圍的新政策只改變一個第一步，舊流程與歷史情境保留」，也可以展示「結構通過，答案回歸仍抓到缺漏」及一次實際提案修正。這些是合成案例中的執行觀察，不能推論整體準確率提升、比普通 RAG 更好或 production release 已完成。

## 執行條件

兩階段沿用同一 Query 提示詞與問題輸入，只改情境日期和知識快照。每階段十題同批生成，答題工作階段未提供參考答案、rubric 或聊天歷史；五次模型推論的事件紀錄皆無工具呼叫。維護 Agent 已看過契約與更新資料，編譯與維護審查不屬盲測。

答案與評判使用不同工作階段、同一模型家族；只有單次樣本，沒有檢索器、Teams、ACL 或普通 RAG 對照。模型 alias 為 gpt-6.1-sol，reasoning 為 high；精確 serving snapshot 及 USD 未量測。

五次 CLI 推論合計實際 usage：input 180513、output 39977 tokens；其中 reasoning output 5987 是 output 的組成欄位，未重複加總。批次時間不是單題 latency。
