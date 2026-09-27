# Knowledge Resolution Demo

這是一組專為「LLM Wiki：企業內部知識問答系統的架構演進」設計的**合成企業 IT 知識案例**。目的不是證明某個模型的準確率，而是讓架構討論具備足夠難度：多份來源同時有效、部分取代、適用範圍不同、以及看似衝突但其實是 context-dependent truth。

## 固定問題

> 我是台南分公司的正式員工，今天換了一台公司管理的新筆電。登入 ExampleVPN 時出現 DEMO-455，該怎麼處理？

## 四份來源

| Source | 內容角色 | 關鍵事實 |
|---|---|---|
| A — Legacy VPN Guide | 舊版正式操作手冊 | Legacy VPN 使用帳密 + OTP；DEMO-455 優先檢查帳密 |
| B — Zero Trust Migration Policy | 新版遷移政策 | 2026-09-01 起，分公司正式員工 + managed device 改用 Entra ID + Conditional Access；總公司與 contractor 暫時維持 Legacy VPN |
| C — Service Desk FAQ | 高頻客服知識 | DEMO-455 常見原因為帳密錯誤，但條目未區分新舊架構 |
| D — Incident Postmortem | 上線後事件證據 | Zero Trust 上線後，分公司 managed device 的 DEMO-455 主要與 device compliance 未完成有關 |

四份來源**都不是單純「錯的」**。真正的工程問題是：針對特定使用者情境，哪些主張仍有效、哪些被部分取代、哪些需要限定 scope。

## 架構問題

傳統 Query-time RAG 可以把 A/B/C/D 都找回來，但仍需在每一次查詢當下重新完成：

1. Applicability resolution
2. Partial supersession
3. Conflict resolution
4. Claim-level provenance
5. Missing-context detection

LLM Wiki / Knowledge Compilation 的核心主張是：把可重用的知識整合工作提前到 **Update Time**，產出可審查、可版本化、可發布的 knowledge release，再讓 Query Time 專注於身份、當下 context 與 business workflow。

## Worked Resolution

最終不應寫成「DEMO-455 = 密碼錯誤」或「新版文件全部取代舊版」，而是：

- Branch employee + managed device + Zero Trust path → 先檢查 device compliance / registration。
- HQ employee → Legacy VPN 流程仍有效。
- Contractor → Legacy VPN 流程仍有效。
- 使用者角色、裝置狀態或接入模式未知 → 不直接給唯一處理步驟，先追問。

詳見：

- [claim-resolution.md](claim-resolution.md)
- [mutation-plan.md](mutation-plan.md)
- [knowledge-release.md](knowledge-release.md)
- [sources/](sources/)

## 證據邊界

這是**合成 worked example**，用來展示架構決策，不是 production incident，也不是模型 benchmark。舊版 `evidence/wiki-update-demo/` 仍保留實際執行過的 lint / graph fixture，作為「Structural Validation ≠ Semantic Correctness」的可重跑證據。
