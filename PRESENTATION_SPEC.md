# LLM Wiki：企業內部知識問答系統的架構演進

## Document control

| Field | Value |
|---|---|
| Document ID | `llm-wiki-architecture-talk` |
| Version | `3.2` |
| Status | `HTML aligned with v3.2; local compilation and regression run pending` |
| Prepared on | `2026-09-27` |
| Event | Hello World 2026 |
| Duration | 28 minutes planned narration + 2 minutes buffer |
| Main slides | 15 |
| Appendix | 5 optional evidence sections |
| Language | Traditional Chinese with English technical identifiers |

## 1. 新主軸

正式講題維持：**LLM Wiki：企業內部知識問答系統的架構演進**。

本版真正回答的架構問題是：

> 企業知識問答裡，知識整合到底應該發生在 **Query Time**，還是 **Update Time**？

核心主張：

> **LLM Wiki 不是把 PDF 轉成 Markdown，而是把每次查詢都要重做的知識整合，提前到可審查、可測試、可發布的 Knowledge Update 流程。**

一句話 takeaway：

> **Treat enterprise knowledge like a releaseable software artifact.**

## 2. v3.2 補強點

這版補兩個尚未落地的關鍵缺口：

1. **Teams Agent 真實案例 slice**：選用 `teams-agent` 既有 VPN / FortiClient eval cluster，不再只靠合成 DEMO-455。這組包含 multi-source troubleshooting、cross-document synthesis、process knowledge、no-answer boundary。
2. **4 題 regression eval contract**：新增 `evidence/teams-agent-vpn-compilation/regression-cases.json`，明確定義 Knowledge Compilation 後要通過的四個案例。

保留 v3.1 的三個補強：

- LLM 不是真相來源，而是 **Knowledge Change Proposal Engine**。
- Source D 使用 37/50 association，不宣稱 universal causation。
- Retrieval A/B bridge 證明這不是放棄 RAG，而是在 retrieval 已比較後往 knowledge lifecycle 追下一層問題。

## 3. 兩層案例設計

### A. 主敘事案例：DEMO-455 Knowledge Resolution

用途：講 partial supersession、evidence strength、claim-level provenance。

固定問題：

> 我是台南分公司的正式員工，今天換了一台公司管理的新筆電。登入 ExampleVPN 時出現 DEMO-455，該怎麼處理？

四份來源：

| Source | 內容角色 | 關鍵張力 |
|---|---|---|
| A — Legacy VPN Guide | 舊版正式操作手冊 | DEMO-455 優先檢查帳密，對 Legacy VPN 仍有效 |
| B — Zero Trust Migration Policy | 新版遷移政策 | 只讓分公司正式員工 + managed device 改走 Zero Trust，不是全體取代 |
| C — Service Desk FAQ | 高頻客服知識 | DEMO-455 = 帳密錯誤，但 FAQ 沒區分新舊架構 |
| D — Incident Postmortem | 上線後事件證據 | 37/50 rollout cases 與 device compliance 未完成相關，屬於 scoped associated evidence，不是 universal causation |

### B. 補強實證案例：Teams Agent VPN / FortiClient cluster

用途：補上「真的來自既有專案 eval 的回歸案例」。

來源：`evidence/teams-agent-vpn-compilation/`。

| Regression | Pattern | Query | Why it matters |
|---|---|---|---|
| R1 | Multi-source troubleshooting | `FortiClient 出現 Permission denied 錯誤碼 -455 怎麼辦？` | 可能同時需要 FortiClient 錯訊與 VPN Q&A |
| R2 | Cross-document synthesis | `VPN 密碼到期了要怎麼處理？` | 症狀與動作分散在相鄰文件 |
| R3 | Process knowledge | `員工要出國，需要短暫申請 VPN 國外連線，流程是什麼？` | procedure / approval / escalation 不是 error-code lookup |
| R4 | No-answer boundary | `VPN連線出現 Error -619，這是什麼問題？` | 不可因為都是 VPN 就腦補未收錄錯誤碼 |

誠實界線：`teams-agent/data/sources/*.md` 未進公開 repo，因此目前新增的是 **selected real-case slice + local run contract**，不是 completed execution result。要達到 95 分，仍需在本機匯出 sanitized corpus 並實際產生 `output/regression-results.json`。

## 4. 15 頁主線

| # | Slide | Time | 角色 |
|---|---|---:|---|
| S01 | LLM Wiki：企業內部知識問答系統的架構演進 | 0:30 | 開場與 thesis |
| S02 | 一個 VPN 問題，四個都「正確」的答案 | 2:00 | Hook；建立 hard case |
| S03 | 我們真的先優化過 Retrieval | 1:30 | Agentic RAG + A/B bridge |
| S04 | Retrieval 成功，為什麼 Answer 還會錯？ | 2:00 | 從 retrieval 拉到 knowledge resolution |
| S05 | Query Time 還承擔了什麼？ | 2:00 | 第一張核心架構圖 |
| S06 | 把 Knowledge Work 搬到 Update Time | 2:00 | 定義 LLM Wiki / Knowledge Compilation |
| S07 | Hard Case：partial supersession + evidence strength | 2:00 | 展示來源張力 |
| S08 | LLM 是 Knowledge Change Proposal Engine | 2:00 | 補足 LLM Wiki 的 LLM 角色 |
| S09 | Impact Discovery：哪些頁面會被牽動？ | 2:00 | 機制一 |
| S10 | Claim-level Provenance + Evidence Strength | 3:00 | 機制二；技術高潮 |
| S11 | Draft → Validate → Knowledge Release | 2:30 | 機制三；避免半套更新 |
| S12 | Teams Agent VPN cluster：可回歸的真實 slice | 2:00 | 補充實證接口 |
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

| Metric | Hybrid RAG | Gemini File Search |
|---|---:|---:|
| P50 latency | 3.00s | 5.71s |
| P95 latency | 4.07s | 7.15s |
| Avg cost/query | US$0.001059 | US$0.001804 |
| Reported answer proxy | 25/25 | 25/25 |

講者稿：這裡不是說 retrieval 不重要。我們真的比較過 retrieval backend。當小語料測試裡品質 proxy 接近，架構選型會看 latency、cost、操作控制。但下一層問題是：如果系統把四份都找回來，哪一份才應該成為這個使用者的答案？

限制：這是歷史 A/B，小語料、proxy metric，不是 LLM Wiki 效益實驗。

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

### S07 — Hard Case：partial supersession + evidence strength

投影四份 source 的 one-liner + validity condition。重點：A/C 對 Legacy VPN 仍有效；B 只部分取代 A；D 只支持「分公司 managed device rollout」族群，而且 37/50 是關聯證據，不是 universal causation。

### S08 — LLM 是 Knowledge Change Proposal Engine

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

### S10 — Claim-level Provenance + Evidence Strength

| Population | Access path | DEMO-455 first action | Evidence wording |
|---|---|---|---|
| Branch full-time + managed device | Zero Trust | Check compliance / sync state | 37/50 reviewed cases associated with incomplete compliance |
| HQ employee | Legacy VPN | Check credentials / OTP | Legacy guide + FAQ remain valid |
| Contractor | Legacy VPN | Check credentials / OTP | Zero Trust policy does not migrate contractors |
| Unknown context | Unknown | Ask clarification | Missing applicability fields |

錯誤寫法：DEMO-455 is caused by device compliance.

較好寫法：During branch Zero Trust rollout, incomplete compliance was observed in 37/50 reviewed DEMO-455 cases; check compliance first for this population.

主句：整頁 citation 不夠，架構上要知道每個 claim 的來源、適用條件與 evidence strength。

### S11 — Draft → Validate → Knowledge Release

```text
Impact Discovery → Mutation Plan → Draft Release → Structural Validation → Semantic Validation → Regression Queries → Human Review → Atomic Publish
```

主句：企業知識要像軟體 artifact 一樣發布。失敗時 ACTIVE pointer 不動。

### S12 — Teams Agent VPN cluster：可回歸的真實 slice

投影：

```text
Teams Agent existing eval slice
  R1 -455              multi-source troubleshooting
  R2 password expiry   cross-document synthesis
  R3 overseas VPN      process / approval flow
  R4 unknown -619      no-answer boundary
```

說法：這組不是新的表演題，而是從既有 Teams Agent eval 選出來的 VPN / FortiClient cluster。它補上這場演講最需要的 bridge：Knowledge Compilation 不只是一個漂亮概念，它可以接回既有 regression practice。

誠實界線：目前公開 repo 沒有 gitignored `data/sources/*.md`，所以這頁先作為 selected real-case slice + local run contract；完成本機 sanitized export 後，再替換成 executed run result。

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
| KR-01 | `evidence/knowledge-resolution-demo/README.md` | DEMO-455 主案例總覽 |
| KR-02 | `evidence/knowledge-resolution-demo/sources/*.md` | 四份合成來源 |
| KR-03 | `evidence/knowledge-resolution-demo/claim-resolution.md` | claim-level provenance 與 resolution |
| KR-04 | `evidence/knowledge-resolution-demo/mutation-plan.md` | impact discovery / changeset / guardrails |
| KR-05 | `evidence/knowledge-resolution-demo/knowledge-release.md` | release pipeline / validation layers |
| KR-06 | `evidence/knowledge-resolution-demo/llm-role.md` | LLM role contract |
| TA-VPN-01 | `evidence/teams-agent-vpn-compilation/README.md` | Teams Agent VPN evidence package |
| TA-VPN-02 | `evidence/teams-agent-vpn-compilation/source-selection.md` | local source export list |
| TA-VPN-03 | `evidence/teams-agent-vpn-compilation/regression-cases.json` | four regression cases |
| TA-VPN-04 | `evidence/teams-agent-vpn-compilation/compilation-target.md` | target output artifacts |
| TA-VPN-05 | `evidence/teams-agent-vpn-compilation/runbook.md` | how to execute the missing local run |
| AB-01 | `evidence/retrieval-ab-bridge.md` | Retrieval A/B bridge |
| WD-01 | `evidence/wiki-update-demo/README.md` | v2 實際 lint / graph fixture 總覽 |
| WD-02 | `evidence/wiki-update-demo/records/runs.json` | 實際工具執行紀錄 |
| WK-01 | Tencent WeKnora public repository | 外部知識基礎設施趨勢佐證 |

## 7. Acceptance criteria

- [x] 新 DEMO-455 hard case 已建立在 `evidence/knowledge-resolution-demo/`。
- [x] LLM role contract 已補入 `llm-role.md` 與主線 S08。
- [x] Source D 已改成 evidence strength / association，不宣稱 universal causation。
- [x] Retrieval A/B bridge 已補入 S03。
- [x] Teams Agent VPN real-case slice 已建立在 `evidence/teams-agent-vpn-compilation/`。
- [x] 4 題 regression contract 已補入 `regression-cases.json` 與 S12。
- [ ] 本機匯出 sanitized `teams-agent/data/sources/*.md` 到 `input-sources/`。
- [ ] 執行 Knowledge Compilation，產生 `output/` artifacts。
- [ ] 實際跑四題 regression，產生 `output/regression-results.json`。
- [x] `index.html` 的 15 頁主線、5 個附錄段落與講者稿同步 v3.2。

## 8. Next evidence needed for 95-point target

目前 v3.2 已經把案例與評測 slice 找好。要進一步把「run contract」升級成「execution evidence」，還需要：

1. 從本機 `teams-agent/data/sources/` 匯出 5 份 sanitized VPN source。
2. 實際跑一次 Knowledge Compilation。
3. 將 `output/compilation-summary.md`、`output/regression-results.json`、`output/diffstat.txt` commit 回 repo。
4. 把 S12 文字從「selected real-case slice + local run contract」改成「executed local sanitized run」。
