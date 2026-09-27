# LLM Wiki：企業內部知識問答系統的架構演進

## Document control

| Field | Value |
|---|---|
| Document ID | `llm-wiki-architecture-talk` |
| Version | `3.0` |
| Status | `Reframed for 95-point target: architecture thesis, hard knowledge-resolution case, 15-slide story` |
| Prepared on | `2026-09-27` |
| Event | Hello World 2026 |
| Duration | 28 minutes planned narration + 2 minutes buffer |
| Main slides | 15 |
| Appendix | 4 optional evidence sections |
| Language | Traditional Chinese with English technical identifiers |

## 1. 新主軸

正式講題維持：**LLM Wiki：企業內部知識問答系統的架構演進**。

本版真正回答的架構問題是：

> 企業知識問答裡，知識整合到底應該發生在 **Query Time**，還是 **Update Time**？

核心主張：

> **LLM Wiki 不是把 PDF 轉成 Markdown，而是把每次查詢都要重做的知識整合，提前到可審查、可測試、可發布的 Knowledge Update 流程。**

一句話 takeaway：

> **Treat enterprise knowledge like a releaseable software artifact.**

## 2. 為什麼砍掉 v2 主線

v2 最大問題不是不完整，而是案例尺度不夠：來源 v1 到 v2 只新增一個版本分支，主線卻花太多篇幅說明三頁 Markdown 修訂、lint 與 graph。它能證明「產物可追查」，但不足以承擔「架構演進」。

v3 改用 `evidence/knowledge-resolution-demo/`：四份合成企業 IT 文件同時有效，且彼此存在部分取代與情境衝突。這讓演講能展示真正的工程判斷：

- Applicability resolution
- Partial supersession
- Conflict resolution
- Claim-level provenance
- Atomic knowledge release

原本 `evidence/wiki-update-demo/` 不刪除，但主線只保留其洞見：**structural validation is necessary, but not sufficient**。

## 3. 固定案例：DEMO-455 Knowledge Resolution

固定問題：

> 我是台南分公司的正式員工，今天換了一台公司管理的新筆電。登入 ExampleVPN 時出現 DEMO-455，該怎麼處理？

四份來源：

| Source | 內容角色 | 關鍵張力 |
|---|---|---|
| A — Legacy VPN Guide | 舊版正式操作手冊 | DEMO-455 優先檢查帳密，對 Legacy VPN 仍有效 |
| B — Zero Trust Migration Policy | 新版遷移政策 | 只讓分公司正式員工 + managed device 改走 Zero Trust，不是全體取代 |
| C — Service Desk FAQ | 高頻客服知識 | DEMO-455 = 帳密錯誤，但 FAQ 沒區分新舊架構 |
| D — Incident Postmortem | 上線後事件證據 | Zero Trust 分公司 managed device 的 DEMO-455 多半是 device compliance 問題 |

關鍵：四份來源都不是單純錯誤。傳統 RAG 可能把四份都找回來，但模型仍要在 query time 決定哪一份適用於這個人。

## 4. 15 頁主線

| # | Slide | Time | 角色 |
|---|---|---:|---|
| S01 | LLM Wiki：企業內部知識問答系統的架構演進 | 0:30 | 開場與 thesis |
| S02 | 一個 VPN 問題，四個都「正確」的答案 | 2:00 | Hook；建立難題 |
| S03 | 去年我們怎麼做 Agentic RAG | 1:30 | 符合投稿；壓縮技術背景 |
| S04 | Retrieval 成功，為什麼 Answer 還會錯？ | 2:00 | 將問題從 retrieval 拉到 knowledge resolution |
| S05 | Query-time integration 才是真正瓶頸 | 2:00 | 第一張核心架構圖 |
| S06 | 把 Knowledge Work 搬到 Update Time | 2:00 | 定義 LLM Wiki / Knowledge Compilation |
| S07 | Hard Case：四份互相交疊的 VPN 文件 | 2:00 | 展示來源張力 |
| S08 | Impact Discovery：哪些頁面會被牽動？ | 2:00 | 機制一 |
| S09 | Partial Supersession + Conflict Resolution | 3:00 | 機制二；全場技術高潮 |
| S10 | Claim-level Provenance | 2:00 | 機制三；來源與適用條件 |
| S11 | Draft → Validate → Knowledge Release | 2:30 | 機制四；避免半套更新 |
| S12 | Structural Valid ≠ Semantic Correct | 1:30 | 保留 v2 實測 lint 洞見 |
| S13 | LLM Wiki 只是 Knowledge Layer：Teams Agent | 2:00 | 接回企業資訊客服 |
| S14 | WeKnora 與何時值得採用 | 2:00 | 外部佐證 + decision framework |
| S15 | 三句帶走 | 1:00 | 收束 |

總計約 28 分鐘。

## 5. 逐頁規格

### S01 — LLM Wiki：企業內部知識問答系統的架構演進

**目的**：直接把題目拉成架構問題。

**投影主句**：

> We kept improving retrieval. The unresolved work was knowledge resolution.

**講者稿**：今天不是再教一套 RAG pipeline，而是討論企業知識問答裡一個常被忽略的問題：如果多份來源都正確，但適用範圍不同，Agent 到底該在每次查詢時臨場整合，還是事先把可重用的知識整合成可發布的資產？

### S02 — 一個 VPN 問題，四個都「正確」的答案

**目的**：用 hard case 讓觀眾立刻看到「不是找不到文件」。

**投影內容**：固定問題 + 四份來源摘要。

**關鍵說法**：傳統 RAG 可能把 A/B/C/D 全找回來，而且都算 source-grounded。但如果使用者是台南分公司正式員工、公司管理的新筆電，答案不能只照 FAQ 說「先重打密碼」。

### S03 — 去年我們怎麼做 Agentic RAG

**目的**：履行投稿承諾，但不讓 LangGraph 吃掉全場。

**投影圖**：User → Query Planning → Tool Calling → Retrieval → Answer → Self-check / Rewrite。

**限制**：最多 90 秒。不要教 LangGraph API。

### S04 — Retrieval 成功，為什麼 Answer 還會錯？

**目的**：建立 retrieval failure 與 knowledge failure 的分野。

**投影對照**：

| Retrieval problem | Knowledge resolution problem |
|---|---|
| 找不到文件 | 找到四份，但適用範圍不同 |
| 排序錯 | 新文件只部分取代舊文件 |
| query 改寫不足 | FAQ 與 postmortem 同時正確但 scope 不同 |
| chunk 太小 | 每個 claim 需要自己的 provenance |

**主句**：Reranker 可以改善左邊，但不會自動解決右邊。

### S05 — Query-time Integration 是真正瓶頸

**目的**：第一張貫穿全場的核心圖。

**圖**：

```text
Raw Documents
    ↓
Retrieval
    ↓
LLM resolves applicability / conflict / supersession every time
    ↓
Answer
```

**講者稿**：這種模式把很多知識工程工作丟到每一次 query 當下：哪份來源新、哪份仍有效、哪一段被部分取代、哪個例外需要保留。模型每次都要重新解一次迷宮。

### S06 — 把 Knowledge Work 搬到 Update Time

**目的**：定義 LLM Wiki。

**圖**：

```text
Raw Documents
    ↓
Knowledge Compilation
    ↓
Review / Validation
    ↓
Published Knowledge
    ↓
Retrieval / Agent
```

**定義**：LLM Wiki = Knowledge Contract for Agents。Markdown 只是載體；真正重要的是 structure、provenance、ownership、lifecycle、access、relationships。

**主句**：我們沒有消滅複雜度，而是把可重用的複雜度搬到可以 review 和 release 的地方。

### S07 — Hard Case：四份互相交疊的 VPN 文件

**目的**：讀懂來源張力。

**投影**：四份 source 的 one-liner + validity condition。

**重點**：A/C 對 Legacy VPN 仍有效；B 只部分取代 A；D 只支持分公司 managed device 族群，不支持全部使用者。

### S08 — Impact Discovery：哪些頁面會被牽動？

**目的**：展示不是「預先知道改三頁」。

**投影**：候選頁面：`remote-access-authentication`、`device-compliance`、`examplevpn-client`、`demo-455 query`、`faq/demo-455`。

**機制**：semantic match + backlinks + entity matching + source relationships + query logs。

**誠實界線**：這是 worked design，不是已量測的大規模自動召回率。

### S09 — Partial Supersession + Conflict Resolution

**目的**：全場技術高潮。

**投影表**：

| Population | Access path | DEMO-455 first action |
|---|---|---|
| Branch full-time + managed device | Zero Trust | Check device compliance / sync state |
| HQ employee | Legacy VPN | Check credentials / OTP |
| Contractor | Legacy VPN | Check credentials / OTP |
| Unknown context | Unknown | Ask clarification |

**主句**：新政策不是讓舊手冊失效，而是只取代特定族群的 first action。

### S10 — Claim-level Provenance

**目的**：回答「引用如何支持個別主張」。

**投影**：claim → source → applicability。

例：

- Branch managed device migrated to Zero Trust → Source B
- DEMO-455 in that rollout often caused by compliance → Source D
- Legacy users still credential-first → Source A + Source C

**主句**：整頁 citation 不夠，架構上要知道每個 claim 的來源與適用條件。

### S11 — Draft → Validate → Knowledge Release

**目的**：解決「改 A 壞 B」與半套更新。

**圖**：

```text
Impact Discovery → Mutation Plan → Draft Release → Structural Validation → Semantic Validation → Regression Queries → Human Review → Atomic Publish
```

**主句**：企業知識要像軟體 artifact 一樣發布。失敗時 ACTIVE pointer 不動。

### S12 — Structural Valid ≠ Semantic Correct

**目的**：保留原 v2 實證，但壓縮到一頁。

**投影**：

- `wiki-update-demo/stale-v2`：lint exit 0，但語義仍過時。
- `missing-summary-v2`：lint exit 1，可抓斷鏈與缺 source summary。

**結論**：structural lint 必要，但無法單獨保證知識仍符合最新來源。

### S13 — LLM Wiki 只是 Knowledge Layer：Teams Agent

**目的**：把 Teams Agent 放進正確位置，不變成另一場專案分享。

**圖**：Teams → Intent / Issue → FAQ / Knowledge / Ticket → Clarification → Citation → Feedback。

**主句**：Knowledge tells the Agent what is true. Business workflow tells the Agent what to do.

### S14 — WeKnora 與何時值得採用

**目的**：外部佐證 + decision framework。

**投影**：WeKnora 代表 open-source ecosystem 正從 RAG 擴展到 Wiki、Revision、RBAC、Audit、Knowledge Management。

**決策框架**：

不值得：少量 FAQ、單一 authoritative source、低更新頻率、無跨文件衝突。

開始值得：大量文件、頻繁版本更新、部分取代、多人維護、需要 provenance、ACL、lifecycle、同問題反覆查詢。

### S15 — 三句帶走

1. Not every RAG failure is a retrieval failure.
2. LLM Wiki moves knowledge integration from query time to update time.
3. Treat enterprise knowledge like a releaseable software artifact.

最後一句中文：企業知識不只是內容。它也需要編譯、測試、版本與發布。

## 6. Evidence registry

| ID | Source | 用途 |
|---|---|---|
| KR-01 | `evidence/knowledge-resolution-demo/README.md` | 新主案例總覽 |
| KR-02 | `evidence/knowledge-resolution-demo/sources/*.md` | 四份合成來源 |
| KR-03 | `evidence/knowledge-resolution-demo/claim-resolution.md` | claim-level provenance 與 resolution |
| KR-04 | `evidence/knowledge-resolution-demo/mutation-plan.md` | impact discovery / changeset / guardrails |
| KR-05 | `evidence/knowledge-resolution-demo/knowledge-release.md` | release pipeline / validation layers |
| WD-01 | `evidence/wiki-update-demo/README.md` | v2 實際 lint / graph fixture 總覽 |
| WD-02 | `evidence/wiki-update-demo/records/runs.json` | 實際工具執行紀錄 |
| WD-03 | `evidence/wiki-update-demo/records/content-revision.diff` | 舊案例三頁 diff，附錄用 |
| TA-01 | `../teams-agent/README.md` and related docs | Teams Agent 背景與 workflow layer |
| WK-01 | Tencent WeKnora public repository | 外部知識基礎設施趨勢佐證 |

## 7. HTML implementation notes

- 主簡報更新為 15 頁，保留 `#s01`–`#s15`。
- 舊 `#s16`–`#s20` 連結應導到 `#s15` 或閱讀模式備註，避免白屏。
- 保留閱讀模式與來源區，但主畫面不再重複 DEMO-AUTHORED / DEMO-EXECUTED badge。
- `wiki-update-demo` 只出現在 S12 與附錄證據，不再佔半場。
- 每頁投影只保留一個主要機制；完整表格放閱讀模式。

## 8. Acceptance criteria

- [x] 新 demo 已建立在 `evidence/knowledge-resolution-demo/`。
- [ ] `index.html` 主線為 15 頁且與本 spec 同步。
- [ ] 開場 3 分鐘內能說出：這場在討論 query-time vs update-time knowledge integration。
- [ ] S09 能清楚解釋 partial supersession，不把新版政策說成全量取代。
- [ ] S10 能清楚展示 claim-level provenance。
- [ ] S11 明確呈現 atomic knowledge release，而不是 LLM 直接改 production Markdown。
- [ ] S12 壓縮 v2 工具證據，且不讓它重新主導全場。
- [ ] 結尾三句可被觀眾複述。
