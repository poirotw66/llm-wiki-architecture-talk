# 問答、更新與回歸執行方式

本輪以已封存的十題契約執行基準與更新後問答。契約、來源與基準知識頁不改寫；操作日誌僅 append。結果另存，失敗項目也保留。更新只建立 `updated-v2/` 草稿快照，不改動既有 llm-wiki-example 的企業知識庫。

## 問答執行

- 使用既有 llm-wiki Query 預設模式：purpose／index → 編譯知識 → 必要時核對 canonical archives。
- 基準情境日期為 `2030-02-01`，只提供 SRC-01 至 SRC-06；更新後日期為 `2030-03-02`，提供七份來源與更新草稿。
- 每階段使用新的、暫存的 Codex CLI inference 工作階段，沿用使用者目前設定的 `gpt-6.1-sol` 與 `high` reasoning。以 JSON schema 收集輸出，保存提示詞、輸入、原始事件、回答與 digest。
- 不提供聊天歷史、參考答案、必須包含／禁止內容或評分規則。請求禁止工具呼叫；實際事件另檢查工具使用數，不能僅依提示詞宣稱隔離。
- 十題同批提供，每題要求獨立判斷；這是兩批小型案例測試，不是十個互相隔離的單題 session，也不是多次取樣的統計評測。
- 這是完整小型 bundle 的問答測試，沒有實作或量測檢索器、企業 ACL、Teams serving 或 RAG 相對效益。

## 更新與審查

SRC-07 依使用者本輪明確指示准入，digest 必須符合原先契約。沿用既有 governance、archive、analysis receipt、cache、review queue 與 lint 工具。

另取得一次實際模型變更提案，保存 impact candidates 與文字修改。維護 Agent 檢查引用與適用條件，再落盤草稿；任何修正另存紀錄。不得把 Agent 審查寫成人類內容核可；所有更新頁維持 draft。

## 判定方式與限制

回答先保存，再依凍結契約逐條判定 route、第一步、必要內容、禁止推論、引用與追問欄位。first_action 的原始標籤保留；語意相同但字串不同者，必須記錄對照理由，不能靜默改寫模型輸出。

模型評判與產生答案使用不同工作階段，但同一模型家族，並非人類盲評。維護 Agent 再依實際回答與來源審查爭議；模型評分不是最終真相。逐題紀錄需明確區分評判者及人工審查是否完成。

只保存 CLI 實際回傳的 usage，成本與精確 serving snapshot 未提供時保持未量測。批次耗時不能當成單題 latency，cached input tokens 也不能重複加總。工作階段之前看過來源與契約的維護 Agent 不屬於盲測；新的答題 inference 是否未見參考答案，另以實際輸入與工具事件界定。

方法參照：[OpenAI 官方的技能評測說明](https://developers.openai.com/blog/eval-skills)。本輪使用其中的事件紀錄與結構化輸出方式，不把編譯產物、引用存在或 lint 通過當成答案正確。
