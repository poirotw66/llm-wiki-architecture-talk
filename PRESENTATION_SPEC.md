# LLM Wiki：企業內部知識問答系統的架構演進

## Document control

| Field | Value |
|---|---|
| Document ID | `llm-wiki-architecture-talk` |
| Version | `3.1` |
| Status | `Added LLM role contract, ambiguous evidence strength, and retrieval A/B bridge` |
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

## 2. v3.1 補強點

這版補三件會影響分數的內容：

1. **LLM 角色定義**：LLM 不是真相來源，而是 **Knowledge Change Proposal Engine**。它提出 impact candidates、conflict candidates、mutation plan、regression queries；deterministic checks、semantic validation 與 human review 決定是否發布。
2. **更不乾淨的 incident evidence**：Source D 改為「50 起 rollout cases 中 37 起與 device compliance 未完成相關」。這支持優先檢查，不支持把 DEMO-455 寫成 universal compliance cause。
3. **Retrieval A/B bridge**：保留既有 Hybrid RAG vs Gemini File Search 的歷史數據，證明這不是放棄 RAG，而是在 retrieval 已被優化與比較後，往 knowledge lifecycle 追下一層瓶頸。

## 3. 固定案例：DEMO-455 Knowledge Resolution

固定問題：

> 我是台南分公司的正式員工，今天換了一台公司管理的新筆電。登入 ExampleVPN 時出現 DEMO-455，該怎麼處理？

四份來源：

| Source | 內容角色 | 關鍵張力 |
|---|---|---|
| A — Legacy VPN Guide | 舊版正式操作手冊 | DEMO-455 優先檢查帳密，對 Legacy VPN 仍有效 |
| B — Zero Trust Migration Policy | 新版遷移政策 | 只讓分公司正式員工 + managed device 改走 Zero Trust，不是全體取代 |
| C — Service Desk FAQ | 高頻客服知識 | DEMO-455 = 帳密錯誤，但 FAQ 沒區分新舊架構 |
| D — Incident Postmortem | 上線後事件證據 | 37/50 rollout cases 與 device compliance 未完成相關，屬於 scoped associated evidence，不是 universal causation |

關鍵：四份來源都不是單純錯誤。傳統 RAG 可能把四份都找回來，但模型仍要在 query time 決定哪一份適用於這個人，以及 incident evidence 應該如何措辭。

## 4. 15 頁主線

| # | Slide | Time | 角色 |
|---|---|---:|---|
| S01 | LLM Wiki：企業內部知識問答系統的架構演進 | 0:30 | 開場與 thesis |
| S02 | 一個 VPN 問題，四個都「正確」的答案 | 2:00 | Hook；建立難題 |
| S03 | 我們真的先優化過 Retrieval | 1:30 | Agentic RAG + A/B bridge |
| S04 | Retrieval 成功，為什麼 Answer 還會錯？ | 2:00 | 從 retrieval 拉到 knowledge resolution |
| S05 | Query Time 還承擔了什麼？ | 2:00 | 第一張核心架構圖 |
| S06 | 把 Knowledge Work 搬到 Update Time | 2:00 | 定義 LLM Wiki / Knowledge Compilation |
| S07 | Hard Case：四份互相交疊的 VPN 文件 | 2:00 | 展示來源張力與 evidence strength |
| S08 | LLM 是 Knowledge Change Proposal Engine | 2:00 | 補足 LLM Wiki 的 LLM 角色 |
| S09 | Impact Discovery：哪些頁面會被牽動？ | 2:00 | 機制一 |
| S10 | Partial Supersession + Evidence Strength | 3:00 | 機制二；全場技術高潮 |
| S11 | Claim-level Provenance | 2:00 | 機制三；來源與適用條件 |
| S12 | Draft → Validate → Knowledge Release | 2:30 | 機制四；避免半套更新 |
| S13 | Structural Valid ≠ Semantic Correct | 1:30 | 保留 v2 實測 lint 洞見 |
| S14 | Knowledge Layer 接到 Teams Agent / WeKnora | 2:00 | 落地邊界 + 外部佐證 |
| S15 | 三句帶走 | 1:00 | 收束 |

總計約 28 分鐘。

## 5. 逐頁規格

### S01 — LLM Wiki：企業內部知識問答系統的架構演進

**投影主句**：

> We kept improving retrieval. The unresolved work was knowledge resolution.

**講者稿**：今天不是再教一套 RAG pipeline，而是討論企業知識問答裡一個常被忽略的問題：如果多份來源都正確，但適用範圍不同，Agent 到底該在每次查詢時臨場整合，還是事先把可重用的知識整合成可發布的資產？

### S02 — 一個 VPN 問題，四個都「正確」的答案

固定問題 + A/B/C/D 四份來源摘要。主句：傳統 RAG 可能把四份都找回來，而且都算 source-grounded，但答案仍可能錯，因為問題不是 retrieval missing，而是 applicability / scope / evidence strength。

### S03 — 我們真的先優化過 Retrieval

**投影內容**：

| Metric | Hybrid RAG | Gemini File Search |
|---|---:|---:|
| P50 latency | 3.00s | 5.71s |
| P95 latency | 4.07s | 7.15s |
| Avg cost/query | US$0.001059 | US$0.001804 |
| Reported answer proxy | 25/25 | 25/25 |

**講者稿**：這裡不是說 retrieval 不重要。我們真的比較過 retrieval backend。當小語料測試裡品質 proxy 接近，架構選型會看 latency、cost、操作控制。但下一層問題是：如果系統把四份都找回來，哪一份才應該成為這個使用者的答案？

**限制**：這是歷史 A/B，小語料、proxy metric，不是 LLM Wiki 效益實驗。

### S04 — Retrieval 成功，為什麼 Answer 還會錯？

| Retrieval problem | Knowledge resolution problem |
|---|---|
| 找不到文件 | 找到四份，但適用範圍不同 |
| 排序錯 | 新文件只部分取代舊文件 |
| query 改寫不足 | FAQ 與 postmortem 同時正確但 scope 不同 |
| chunk 太小 | 每個 claim 需要自己的 provenance |
| citation 存在 | citation 沒有表達 evidence strength |

主句：Reranker 可以改善左邊，但不會自動解決右邊。

### S05 — Query Time 還承擔了什麼？

```text
Raw Documents
    ↓
Retrieval
    ↓
LLM resolves applicability / conflict / supersession / evidence strength every time
    ↓
Answer
```

講者稿：這種模式把很多知識工程工作丟到每一次 query 當下：哪份來源新、哪份仍有效、哪一段被部分取代、哪個例外需要保留、incident evidence 要寫成因果還是關聯。模型每次都要重新解一次迷宮。

### S06 — 把 Knowledge Work 搬到 Update Time

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

定義：LLM Wiki = Knowledge Contract for Agents。Markdown 只是載體；真正重要的是 structure、provenance、ownership、lifecycle、access、relationships。

主句：我們沒有消滅複雜度，而是把可重用的複雜度搬到可以 review 和 release 的地方。

### S07 — Hard Case：四份互相交疊的 VPN 文件

投影四份 source 的 one-liner + validity condition。重點：A/C 對 Legacy VPN 仍有效；B 只部分取代 A；D 只支持「分公司 managed device rollout」族群，而且 37/50 是關聯證據，不是 universal causation。

### S08 — LLM 是 Knowledge Change Proposal Engine

投影：

```text
Source change
    ↓
LLM proposes:
  impacted pages
  applicability changes
  conflict candidates
  mutation plan
  regression queries
    ↓
deterministic checks + semantic validation + human review
    ↓
active knowledge
```

主句：LLM proposes knowledge changes. It does not become the source of truth.

這頁用來回答：「這不就是傳統 knowledge management 嗎？」差別是 LLM 降低了產生可審查變更提案的成本，但治理仍決定真相。

### S09 — Impact Discovery：哪些頁面會被牽動？

候選頁面：`remote-access-authentication`、`device-compliance`、`examplevpn-client`、`demo-455 query`、`faq/demo-455`。

機制：semantic match + backlinks + entity matching + source relationships + query logs。

誠實界線：這是 worked design，不是已量測的大規模自動召回率。

### S10 — Partial Supersession + Evidence Strength

| Population | Access path | DEMO-455 first action | Evidence wording |
|---|---|---|---|
| Branch full-time + managed device | Zero Trust | Check compliance / sync state | 37/50 reviewed cases associated with incomplete compliance |
| HQ employee | Legacy VPN | Check credentials / OTP | Legacy guide + FAQ remain valid |
| Contractor | Legacy VPN | Check credentials / OTP | Zero Trust policy does not migrate contractors |
| Unknown context | Unknown | Ask clarification | Missing applicability fields |

主句：新政策不是讓舊手冊失效，而是只取代特定族群的 first action；postmortem 不是 universal cause，而是 priority signal。

### S11 — Claim-level Provenance

例：

- Branch managed device migrated to Zero Trust → Source B
- Incomplete compliance observed in 37/50 DEMO-455 rollout cases → Source D
- Legacy users still credential-first → Source A + Source C

錯誤寫法：DEMO-455 is caused by device compliance.

較好寫法：During branch Zero Trust rollout, incomplete compliance was observed in 37/50 reviewed DEMO-455 cases; check compliance first for this population.

主句：整頁 citation 不夠，架構上要知道每個 claim 的來源、適用條件與 evidence strength。

### S12 — Draft → Validate → Knowledge Release

```text
Impact Discovery → Mutation Plan → Draft Release → Structural Validation → Semantic Validation → Regression Queries → Human Review → Atomic Publish
```

主句：企業知識要像軟體 artifact 一樣發布。失敗時 ACTIVE pointer 不動。

### S13 — Structural Valid ≠ Semantic Correct

保留 `wiki-update-demo` 實測證據：

- `stale-v2`：lint exit 0，但語義仍過時。
- `missing-summary-v2`：lint exit 1，可抓斷鏈與缺 source summary。

結論：structural lint 必要，但無法單獨保證知識仍符合最新來源。

### S14 — Knowledge Layer 接到 Teams Agent / WeKnora

左半：Teams Agent。Knowledge tells the Agent what is true. Business workflow tells the Agent what to do.

右半：WeKnora。Open-source ecosystem 也正在從 RAG 擴展到 Wiki、Revision、RBAC、Audit、Knowledge Management。

決策框架：少量 FAQ / 單一權威來源 / 低更新頻率 → 普通 RAG 足夠。大量文件 / 頻繁版本 / 部分取代 / 需要 provenance、ACL、lifecycle → 開始值得做 LLM Wiki / Knowledge Compilation。

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
| KR-03 | `evidence/knowledge-resolution-demo/claim-resolution.md` | claim-level provenance、evidence strength 與 resolution |
| KR-04 | `evidence/knowledge-resolution-demo/mutation-plan.md` | impact discovery / changeset / guardrails |
| KR-05 | `evidence/knowledge-resolution-demo/knowledge-release.md` | release pipeline / validation layers |
| KR-06 | `evidence/knowledge-resolution-demo/llm-role.md` | LLM role contract |
| AB-01 | `evidence/retrieval-ab-bridge.md` | Retrieval A/B bridge |
| WD-01 | `evidence/wiki-update-demo/README.md` | v2 實際 lint / graph fixture 總覽 |
| WD-02 | `evidence/wiki-update-demo/records/runs.json` | 實際工具執行紀錄 |
| WD-03 | `evidence/wiki-update-demo/records/content-revision.diff` | 舊案例三頁 diff，附錄用 |

## 7. Acceptance criteria

- [x] 新 demo 已建立在 `evidence/knowledge-resolution-demo/`。
- [x] LLM role 已補成 `llm-role.md`，並進入 S08。
- [x] Source D 已改成 37/50 關聯證據，並進入 S10 / S11。
- [x] Retrieval A/B bridge 已補成 `evidence/retrieval-ab-bridge.md`，並進入 S03。
- [ ] `index.html` 主線與本 spec 同步。
- [ ] 開場 3 分鐘內能說出：這場在討論 query-time vs update-time knowledge integration。
- [ ] S10 清楚解釋 partial supersession 與 evidence strength，不把新版政策說成全量取代。
- [ ] S11 清楚展示 claim-level provenance。
- [ ] S12 明確呈現 atomic knowledge release，而不是 LLM 直接改 production Markdown。
- [ ] S13 壓縮 v2 工具證據，且不讓它重新主導全場。
- [ ] 結尾三句可被觀眾複述。
