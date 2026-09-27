# LLM Wiki：企業內部知識問答系統的架構演進

## Document control

| Field | Value |
|---|---|
| Document ID | `llm-wiki-presentation-spec` |
| Version | `2.0` |
| Status | `Content revised; demonstration artifacts captured; visual implementation pending` |
| Prepared on | `2026-09-27` |
| Event | Hello World 2026 |
| Language | Traditional Chinese with English technical identifiers |
| Duration | 28 minutes of planned narration + 2 minutes of buffer |
| Main slides | 20 |
| Appendix slides | 5 |
| Target | Standalone HTML presentation and reading mode |
| Scope | Presentation specification and isolated synthetic evidence artifacts |

## 1. 受眾、主張與六項修正

受眾為具備 LLM／RAG 基本知識的工程師與架構師。正式講題維持「LLM Wiki：企業內部知識問答系統的架構演進」。

核心問題改為：**來源規則改了，既有知識與回答如何跟著改，而且能讓人檢查？**

核心主張：LLM 可以協助提出知識頁的修訂，但需要明確的來源、變更範圍、差異紀錄與查核責任。結構檢查能攔下部分錯誤，內容是否仍符合來源需要另外驗證。

| 原缺點 | 本版修正 | 對應頁面 |
|---|---|---|
| Wiki 到第 12 分鐘才登場 | 第 2 頁直接展示來源更新與修訂產物，第 3 分鐘前建立完整作業地圖 | S02–S03 |
| LLM 的額外責任不清楚 | 明列輸入、提案、改寫、工具驗證與人工責任；展示範圍判斷及未完成項目 | S07、S09、S13–S14 |
| RAG 數字與 Wiki 動機連接薄弱 | RAG 量測濃縮為一頁；Wiki 動機直接來自來源更新案例 | S04–S06 |
| 只有理想對話 | 保存四份實體快照、既有工具的執行紀錄、三份頁面 diff 和待 review 清單 | S02、S10–S15 |
| 缺少架構決策 | 明確比較三個設計選擇、替代方案與代價 | S08、S09、S14 |
| 後段支線與單頁過載 | Teams interface、release 分成兩頁；後端選型與 WeKnora 合成一頁，完整 A/B 放附錄 | S16–S18、A04 |

本版以「可展示產物 → 已有系統的責任 → 一次來源更新 → 三項設計取捨 → 整合邊界」展開。不補寫未查證的開發歷史，也不宣稱本輪展示代表自動 Ingest、線上問答或導入效益已被驗證。

## 2. 時間與敘事配置

| 段落 | Slides | Duration | 要回答的問題 |
|---|---|---:|---|
| 先看到產物，再界定問題 | S01–S05 | 5 min | 問答之外，知識更新還缺哪項責任？ |
| 一次來源更新與檢查 | S06–S15 | 15 min | LLM、工具與人如何分工，哪些錯誤能被抓到？ |
| 系統整合與選型 | S16–S19 | 6 min | 產物怎麼進服務，何時該換後端，下一次測什麼？ |
| 可帶回團隊的方法 | S20 | 2 min | 從哪個小實驗開始？ |
| 緩衝 | — | 2 min | 停頓、現場提問與轉場 |

投影畫面只呈現一個主要機制或證據；閱讀模式保留完整說明與來源。每頁講者稿是核心說法，指圖、對照 diff 與停頓包含在時間內。時間配置尚待實際排練。

### 2.1 證據類型

- `MEASURED`：指定資料集的歷史量測，保留版本與分母。
- `DEMO-EXECUTED`：本任務實際建立的公開合成快照、執行命令與結果。
- `DEMO-AUTHORED`：本輪互動式 Assistant 撰寫的來源、知識頁、提案與修訂；不是模型 API 的獨立測試。
- `IMPLEMENTED`：可在現有程式碼定位的介面或行為，不等同已部署驗收。
- `DOCUMENTED`：專案規約或操作契約。
- `PROPOSED`：未接通的系統路徑或未執行的實驗。
- `EXTERNAL`：外部官方描述，不當成本系統效能證據。
- `FRAMING` / `SYNTHESIS`：問題組織與有根據的收束。

這些英文類型放製作 metadata。投影用簡短中文註記說明來源性質，毋須每頁放一排 badge。

## 3. 固定案例與證據契約

### 3.1 DEMO-02：來源改版與過時回答

本版以 [實際保存的案例包](./evidence/wiki-update-demo/README.md) 取代 v1 spec 的預寫理想聊天劇本。產品 ExampleVPN、錯誤碼 DEMO-101、介面操作及組織均為虛構。所有相關頁面顯示「合成案例；本輪產物與工具檢查」。

固定問題：

> 我用受管理筆電、ExampleVPN 4.1，出現 DEMO-101，怎麼處理？

來源 v1 明定：受管理筆電上的 4.x 出現 DEMO-101，由示範服務台確認裝置登錄。來源 v2 明定：4.1 及以上先使用「同步裝置狀態」一次，仍失敗再交服務台；4.0 沿用 v1。v2 明確限定取代範圍，版本不明須追問。

| Snapshot | 實際內容 | 檢查結果 |
|---|---|---|
| `baseline-v1` | v1 來源、摘要、concept、entity、query | wiki-lint exit 0 |
| `stale-v2` | 加入 v2 來源與摘要，刻意保留三份 v1 下游頁 | wiki-lint exit 0；內容仍少了 4.1 的同步步驟 |
| `missing-summary-v2` | 在獨立副本中刻意移除 v2 摘要 | wiki-lint exit 1：三個斷鏈、一個缺少摘要 |
| `revised-v2` | 三份下游頁補上版本分支與新引用 | wiki-lint exit 0；仍是待人工 review 的 draft |

兩種故障都是教學注入，不能說成 production incident。結構 lint 沒有判定 stale-v2 的語義過時；語義判斷由本輪 Assistant 比對固定來源與問題作出。不能宣稱系統已自動發現所有受影響頁面。

### 3.2 本輪實際做了什麼

1. Assistant 撰寫兩版來源、簡短的變更提案與知識頁；Python 僅將內容保存為快照、metadata 與 diff。
2. 使用 `llm-wiki-example` 的原有 `wiki-lint.py --root` 與 `wiki-graph-insights.py --root` 執行四份快照。
3. 保存命令、時間、exit code、stdout、stderr、工具版本與 SHA-256。
4. 保存 concept、entity、query 三份頁面的實際內容差異。
5. 比較各快照的 v1 原件與 canonical SHA-256，確認本輪未覆寫它們。

未執行自動 `/ingest`、另一個模型 API、RAG runtime、Teams、governance gate、Git history checks 或雲端發布。沒有人工核可、準確率提升或工時節省的測量。這些界線在 S03 一次說清楚，後續只在相關結論旁保留必要標示。

### 3.3 保留的歷史數據

`EVAL-L3-01`：156 題 frozen blind test，116 題有目標證據標註，136 題單輪、20 題多輪；Document Hit@4 99.14%（115/116），Answer Accuracy 96.79%（151/156），multi-turn 90%（18/20），Citation Precision 98.82%。Failure taxonomy 為答案遺漏 5、引用錯誤 3。此語料沒有 group-gated documents。

報告 commit 為 `bdd3894f7a99c07230ebd8069b1179e0be77f601`，release 為 `release-4f49088db9ca`，完成時間 `2026-09-22T18:15:53.449649+00:00`。115/116 與 151/156 由報告比例和相應分母換算。不同指標不相減；failure taxonomy 與 evidence drop diagnostics 不相加。

`AB-01`：2026-08-07、30 題、19 份文件、同模型 `gemini-3.5-flash-lite`、top_k=4。Hybrid／File Search 的 P50 為 3.00／5.71 s，P95 為 4.07／7.15 s，平均每題成本 US$0.001059／US$0.001804。品質欄位使用來源命中等代理判準，不能與 EVAL-L3-01 當成同一定義比較。兩筆 ACL 案例皆預期命中；專用合成 ACL 探測另外陳述。完整數據移至 A01、A02、A04。

## 4. 逐頁內容規格

### S01 — LLM Wiki：企業內部知識問答系統的架構演進

**Timing:** `00:00–00:30` / 30 seconds. **Type:** `FRAMING`.

**本頁目的**：直接提出整場需要回答的工程問題。

**投影文案**：正式題目；副標「來源規則改了，既有知識與回答如何跟著改？」；Hello World 2026 · Justin。未確認職稱與組織不新增。

**畫面**：深色封面，標題旁只露出一段 v1／v2 修訂片段，保留 4.0、4.1 和處理步驟的差異。不用無資訊背景填滿版面。

**揭露**：整體淡入，不逐字打字。

**講者稿**：「今天用一次來源改版，說明企業知識問答的架構責任。我們會看到知識頁怎麼更新、工具能抓到什麼錯誤，以及為什麼通過檢查之後，內容仍需要有人負責。」

**轉場**：「先看這次實際保存的產物。」

**來源／素材**：SRC-14、SRC-17。

**驗收**：正式題目不變；副標是問題，不預先宣稱導入效益。

### S02 — 來源改了，回答也需要改

**Timing:** `00:30–01:30` / 60 seconds. **Type:** `DEMO-AUTHORED` + `DEMO-EXECUTED`.

**本頁目的**：一分鐘內讓觀眾看到 Wiki 的具體產物與更新任務。

**投影文案**：

- 固定問題：「受管理筆電、4.1、DEMO-101，怎麼處理？」
- v1 問答：「請由示範服務台確認登錄紀錄。」
- 修訂問答：「先同步裝置狀態一次；仍失敗再交服務台。」
- 來源 v2 同時保留：「4.0 沿用原流程」。
- 圖說：「合成內容；兩版頁面與 diff 已保存。此處是持久化問答草稿。」

**畫面**：畫面中央放實際 query diff 的兩段正文，右側只有 v2 對應來源句。用一條引用連線讓觀眾看到新步驟從何而來。不要把產物假裝成 Teams 聊天截圖。

**揭露**：先問題與舊文，再顯示來源修訂，最後顯示更新文字。

**講者稿**：「同一個問題，指南更新後多了一個先做的步驟，而且只適用於 4.1 以上。這裡的來源是合成的，但頁面和 diff 是這次實際保存的產物。接下來要解決的工作，是把這個範圍準確帶進相關知識頁，並讓別人能檢查修改是否正確。」

**轉場**：「這次展示的流程與系統邊界先交代清楚。」

**來源／素材**：SRC-14、SRC-17；`stale-v2/wiki/queries/demo-101.md` 與 `revised-v2/wiki/queries/demo-101.md`。

**驗收**：第一分鐘已有 Wiki 產物；版本限制可讀；問答頁不被稱成 runtime 回答實測。

### S03 — 這次展示的知識維護工作

**Timing:** `01:30–03:00` / 90 seconds. **Type:** `DEMO-AUTHORED` + `DEMO-EXECUTED` + `PROPOSED`.

**本頁目的**：定義 LLM Wiki 與本次證據範圍。

**投影文案**：

> LLM Wiki：由來源支持、相互連結，並由 LLM 與人協作維護的知識頁。

`來源修訂 → 變更提案 → 知識頁 diff → 結構檢查 → 待內容 review`

下方兩行：「本輪：互動式 Assistant 撰寫產物，既有腳本執行檢查」；「尚未：自動 Ingest、RAG 問答、人工核可與發布」。

**畫面**：五節點作業圖，只保留一條主路徑。LLM 提案／改寫標為本輪互動作業，腳本檢查標為實際執行，review 的完成狀態明確留空並寫 pending。

**揭露**：按產物先後顯示，最後同時出現執行範圍的兩行說明。

**講者稿**：「這裡用 LLM Wiki 指一組來源支持、互相連結且持續維護的頁面。本輪由互動式 Assistant 產生草稿和修改，然後用專案既有腳本檢查。我們沒有執行整套自動 Ingest，也沒有宣稱模型自己找出了全部影響範圍。這個展示的證據是可讀的輸入、修改和工具輸出。」

**轉場**：「這項維護責任，與查詢時的 RAG 責任如何相接？」

**來源／素材**：SRC-03、SRC-14、SRC-15。

**驗收**：第 3 分鐘前解釋 Wiki；五節點不被畫成已部署的自動 pipeline。

### S04 — 問答評測能定位哪些問題

**Timing:** `03:00–04:15` / 75 seconds. **Type:** `MEASURED`.

**本頁目的**：用一頁交代 RAG 脈絡，避免喧賓奪主。

**投影文案**：Document Hit@4 **115/116**；Answer Accuracy **151/156**。下方單案 `v3-blind-ans-05`：「retrievalEvidenceRecall 1.0 → answerEvidenceRecall 0.0」。

結論：「來源被取回後，回答仍可能遺漏；內容維護需要自己的驗證。」

**畫面**：上方兩個獨立數值及分母，下方一條簡短診斷路徑。不要再加入四張統計圖。圖說顯示「2026-09-23 frozen blind L3；單次固定快照；兩個總體指標分母不同」。

**揭露**：先總體數值，再單案，最後結論。

**講者稿**：「既有報告顯示文件命中與答案評分各有自己的分母。其中一筆案例有檢索證據，答案卻沒有涵蓋。這應該往回答階段追查。今天的 Wiki 展示處理另一個責任：當來源改版，知識內容是否同步更新。這份 RAG 報告沒有證明 Wiki 已改善準確率。」

**轉場**：「我們把分享範圍收斂到一個可以完整追查的更新任務。」

**來源／素材**：SRC-01；完整方法與失敗分類見 A01–A02。

**驗收**：75 秒內能解釋；不做百分點減法；不藉 RAG 失敗直接推論 Wiki 成效。

### S05 — 這次更新任務的完成條件

**Timing:** `04:15–05:00` / 45 seconds. **Type:** `FRAMING`.

**本頁目的**：讓觀眾知道後續如何判定展示完成。

**投影文案**：

1. 找到需要修改的既有知識頁。
2. 保留來源仍有效的版本範圍。
3. 讓修改、引用與工具結果都能被檢查。

下方：「今天展示修改與驗證；效益與自動化程度需另測。」

**畫面**：同一份來源旁的三條註記，分別指到頁面、scope、diff。不是三張抽象能力卡。

**揭露**：一次完整呈現。

**講者稿**：「這次更新任務有三個完成條件：知道要動哪些頁、保留仍有效的舊條件、讓修改可供檢查。接下來每一個工具與設計選擇，都用這三個條件來看。」

**轉場**：「先讀完整的來源差異。」

**來源／素材**：DEMO-02。

**驗收**：沒有事先承諾自動影響分析的召回率或人力效益。

### S06 — v2 改動的範圍

**Timing:** `05:00–06:30` / 90 seconds. **Type:** `DEMO-AUTHORED`.

**本頁目的**：展示 LLM 必須處理的具體語義。

**投影文案**：左側 v1：「4.x → 服務台確認登錄」。右側 v2 的三行：「4.1+ → 同步一次，仍失敗再交服務台」「4.0 → 保留原流程」「版本不明 → 追問」。下方保留原文：「本版只取代 v1 對 4.1 及以上版本的處理步驟」。

**畫面**：來源兩欄對照，標示相同的裝置條件及錯誤碼，只有處理步驟的版本分支高亮。使用已保存來源原文，不能新增來源沒有的處理方式。

**揭露**：先看共同條件，再看新增分支，最後圈出「只取代」的範圍句。

**講者稿**：「更新不是把 v1 全部換成 v2。兩份來源仍共用裝置與錯誤碼條件，但 v2 只改了 4.1 以上的步驟。若更新時只留下『先同步一次』，就會把 4.0 也帶到錯誤路徑。這是維護者與 LLM 都必須保存的語義邊界。」

**轉場**：「LLM 在這個任務中應該產出什麼？」

**來源／素材**：SRC-18，兩份 `raw/originals/examplevpn-guide-v*.md`。

**驗收**：新內容來自來源；不靠模型補寫事實；未聲稱文件日期較新就自動優先。

### S07 — LLM 的輸入、提案與修改

**Timing:** `06:30–08:00` / 90 seconds. **Type:** `DEMO-AUTHORED` + `PROPOSED`.

**本頁目的**：具體回答 LLM 相較純格式檢查負責什麼。

**投影文案**：

| 輸入 | 預期產物 |
|---|---|
| 來源 v1、v2 與既有頁面 | 哪些主張改變、哪些保留 |
| 頁面連結與角色 | 新增 source，修訂既有 concept、entity、query 的提案 |
| 格式與引用規約 | 可供 review 的草稿、diff 與來源連結 |

下方：「本輪以互動式 Assistant 完成提案與草稿；自動發現範圍的可靠度未測量。」

**畫面**：左側三份輸入物，右側一份實際 `v2-change-plan.md` 摘錄；表格只作旁註。LLM 節點不畫成自動批准修改的主管。

**揭露**：輸入先出現，提案後出現。把「保留 4.0」與「全部頁面維持 draft」標為兩個可查核輸出。

**講者稿**：「LLM 的工作在這裡是協助解讀來源差異，提出哪些頁面要改，再寫出有引用的草稿。腳本可以檢查 schema 與連結，但不會自然理解『只取代 4.1 以上』。本輪提案與草稿由互動式 Assistant 寫出，這還不能說明自動跑一百份文件的可靠度，所以我們保留可讀產物和待審查狀態。」

**轉場**：「第一項設計取捨是，我們為什麼保留三層內容？」

**來源／素材**：SRC-16、SRC-14；下一次重做可採此輸入／輸出契約，但不把它偽稱為保存過的模型 API prompt。

**驗收**：清楚區分 LLM 撰寫、檔案保存、工具檢查、人工確認；不宣稱這是比較實驗證明的 LLM 優勢。

### S08 — 決策一：保留原件、Canonical 與 Wiki

**Timing:** `08:00–09:30` / 90 seconds. **Type:** `DOCUMENTED` + `DEMO-AUTHORED`.

**本頁目的**：以替代方案與代價解釋三層產物。

**投影文案**：

| 選擇 | 好處 | 代價 |
|---|---|---|
| 只保留整理後頁面 | 檔案較少 | 難追查整理時漏掉了什麼 |
| 原件＋canonical＋Wiki | 可回查輸入、可檢查轉換、可閱讀與重用 | 多份產物、版本與 lineage 都需要管理 |

圖中三份產物標示：「原件保留輸入」「canonical 保留詳盡內容」「Wiki 保存可重用主張」。

**畫面**：主要是三份真正保存的文件局部，以細線連結同一條 scope。比較表縮成兩行補充，不能反客為主。此 demo 原件已是 Markdown，因此 canonical 可與原件內容相同；沒有多模態轉換成果可展示。

**揭露**：從可讀 Wiki 往回展開來源，最後顯示代價。

**講者稿**：「只留整理後頁面比較簡單，但發現爭議時很難判斷是來源有問題，還是整理時遺漏。這個範本保留三層，換取可追查性，也承擔更多版本與產物管理成本。這次原件本來就是 Markdown，所以沒有表演文件轉換；我們展示的是保留與追溯的責任。」

**轉場**：「第二項取捨是，直接寫頁面，還是先提出變更範圍？」

**來源／素材**：SRC-03、SRC-18。

**驗收**：不把相同 Markdown 複本說成轉檔成功；不把更多檔案宣稱為零成本。

### S09 — 決策二：先提出變更範圍

**Timing:** `09:30–11:00` / 90 seconds. **Type:** `DOCUMENTED` + `DEMO-AUTHORED`.

**本頁目的**：解釋兩段式作業為什麼值得增加一步。

**投影文案**：實際提案的四項輸出：「新增 v2 來源摘要」「更新登錄 concept」「更新用戶端 entity」「更新固定問答 query」。共同限制：「保留 4.0；保留 v1 歸檔；全部維持 draft」。

比較註記：「直接改寫：步驟少，範圍難先檢查」「先提案再改寫：可先檢查範圍，但多了提案維護與生成成本」。

**畫面**：一份實際簡短變更提案，右側用既有檔案路徑對應四個落點。不要展示模型內部思考；只展示可審閱的決策摘要。

**揭露**：先顯示落點，再圈出不應被覆寫的版本分支。

**講者稿**：「直接讓模型重寫所有頁面容易開始，但維護者很難先知道它打算動哪裡。先寫變更提案，讓頁面選擇與版本範圍成為可審查物。本輪三份下游頁是教學案例設計中的已知目標，不是對未知大型 Wiki 自動影響分析的成功率。」

**轉場**：「頁面關係工具能幫我們看到哪些線索？」

**來源／素材**：SRC-04、SRC-16。

**驗收**：提案只含結論與依據；沒有私有推理逐字稿；不把已知三頁目標當成自動召回實驗。

### S10 — 關係圖能提示，不能替代判讀

**Timing:** `11:00–12:30` / 90 seconds. **Type:** `DEMO-EXECUTED`.

**本頁目的**：展示 graph script 的實際能力與邊界。

**投影文案**：`stale-v2` 的 graph report：「pages scanned: 5」「no inbound link: 1」，對象為 v2 source summary。下方：「index 有列入，但既有 concept／query 仍引用 v1」。

**畫面**：五節點圖，從實際 snapshot 的 Markdown 連結重建；v2 摘要位於旁側，其他知識頁仍指向 v1。index 用淡色單獨註記，不計入 graph report 的 Concept 間 inbound 統計。

**揭露**：先顯示既有引用，再顯示新 v2 摘要，最後呈現工具輸出。

**講者稿**：「工具掃描到了五個頁面，指出 v2 摘要沒有來自其他知識頁的 inbound link。它提供了值得檢查的位置，但不會自動判定這是語義上的更新遺漏。修訂後 no-inbound 的數量仍可能是一，因為保留歷史的 v1 頁不再被現行問答引用。要看的是哪個頁面與什麼理由。」

**轉場**：「接著看結構檢查對這份過時內容給出什麼結果。」

**來源／素材**：SRC-18 的 stale-v2 與 revised-v2 graph reports。

**驗收**：不把 graph exit 0 當品質全綠；不把指標數量一樣解讀為修訂沒用；未部署 GraphRAG 的字樣不必反覆佔主畫面。

### S11 — 內容過時，結構檢查仍通過

**Timing:** `12:30–14:00` / 90 seconds. **Type:** `DEMO-EXECUTED` + `DEMO-AUTHORED`.

**本頁目的**：提供整場最重要的實際失敗場景。

**投影文案**：

- 來源 v2：「4.1+ 先同步一次，仍失敗再交服務台」。
- 既有 query：「請由示範服務台確認登錄紀錄」。
- 真實工具輸出：`wiki-lint: ok`，exit 0。
- 結論：「schema、連結與來源配對有效，仍可能漏掉新的處理步驟」。

**畫面**：來源句與舊 query 正文上下對照，中間留出少掉的步驟位置；右下放短工具輸出。保留「故意注入更新遺漏的合成快照」。

**揭露**：先來源，再舊答案，最後顯示 exit 0，停 2 秒。

**講者稿**：「這份快照刻意加進 v2 來源，但沒有更新下游問答。工具實際回傳通過，因為文件結構、連結和原有引用仍成立。對固定的 4.1 問題來說，答案卻少了來源新增的第一步。這裡清楚看到格式驗證的能力邊界，內容更新仍需要另一個檢查。」

**轉場**：「結構檢查有它能確實攔下的問題。」

**來源／素材**：SRC-15；`stale-v2-wiki-lint.txt` 與相同 snapshot 的 query。

**驗收**：不得稱為線上事故、LLM 自動發現或 lint bug；說明它是刻意注入的教學故障。

### S12 — 缺少來源摘要時，檢查能攔下

**Timing:** `14:00–15:30` / 90 seconds. **Type:** `DEMO-EXECUTED`.

**本頁目的**：以另一個實際結果說明工具適合承擔的責任。

**投影文案**：獨立 fixture 中刪去 v2 summary 後，`wiki-lint: 4 issue(s)`，exit 1。合併展示：「3 × broken link」「1 × raw archive missing wiki/sources summary page」。下方：「這份結果來自刻意移除摘要的副本」。

**畫面**：一個原本連到來源摘要的三叉引用圖，中間缺頁以空框標示；工具輸出占右側，不放整頁密集 terminal。

**揭露**：先缺少的摘要，再三條斷鏈與一筆配對錯誤。

**講者稿**：「我們在另一份副本中移除來源摘要。這次工具抓到三個引用斷鏈和一個 canonical 沒有對應摘要的問題。這是規則可以明確判斷的事情。前一頁與這一頁共同說明，機械檢查很有用，但它通過之後還不能保證內容正確。」

**轉場**：「真正的內容修訂長什麼樣子？」

**來源／素材**：SRC-15 的 `missing-summary-v2-wiki-lint.txt`。

**驗收**：四個問題的名稱、數量與原輸出一致；graph script 生成報告不稱為 blocking gate。

### S13 — 三份知識頁的實際修訂

**Timing:** `15:30–17:00` / 90 seconds. **Type:** `DEMO-AUTHORED` + `DEMO-EXECUTED`.

**本頁目的**：用內容差異呈現 LLM 協助維護的具體產物。

**投影文案**：

- Concept：「4.1+ 先同步；4.0 沿用服務台；版本不明先追問」。
- Entity：記錄相同版本範圍與支援條件。
- Query：固定 4.1 問題新增同步一步；引用改向 v2。
- 圖說：「本輪 Assistant 撰寫的修訂；三份頁面保持 draft」。

**畫面**：主圖只放 query 的實際 diff；concept 與 entity 以兩個短行註記說明同步修改。保留 source resource 從 v1 改向 v2 的那一行。最多展示 10 行變更，完整 68 行 diff 放閱讀區。

**揭露**：先正文變化，再引用變化，最後補充其他兩頁的修改範圍。

**講者稿**：「這份 diff 同時改了答案與引用。Concept 保留不同版本的分支，entity 更新適用性，query 回答固定的 4.1 問題。這些頁面是本輪 Assistant 依合成來源撰寫的草稿，不是不可檢查的黑盒輸出；人工可以逐行確認，必要時拒絕修改。」

**轉場**：「草稿已寫好之後，為什麼仍保留 pending review？」

**來源／素材**：SRC-17、SRC-16；完整產物位於 revised-v2。

**驗收**：diff 真正對應保存檔案；不新增不存在的來源；不得改為已核可狀態。

### S14 — 決策三：草稿寫入與核可分開

**Timing:** `17:00–18:30` / 90 seconds. **Type:** `DOCUMENTED` + `DEMO-AUTHORED` + `PROPOSED`.

**本頁目的**：說明非同步 review 的取捨及執行邊界。

**投影文案**：

| 選擇 | 得到什麼 | 必須承擔 |
|---|---|---|
| 先核可再產生所有頁面 | 寫入節奏受控 | 等待人審，草稿可見性低 |
| 先保存可檢查草稿，再做內容 review | 可先看完整差異、集中待辦 | draft 必須與可提供服務的內容區分 |

頁面下半放實際 `review-queue.md`：「pending human review」「concept, entity, query」「保留 4.0」。

**畫面**：草稿產物旁放 review queue，通往 serving 的箭頭用虛線標「另行發布與授權驗證」。來源准入檢查用一句圖說定位在更前方，不再畫第二張複雜流程。

**揭露**：先提案與 draft，再顯示待審查紀錄，最後說明取捨。

**講者稿**：「先保存草稿讓人能看到完整差異，也可能降低等待期間的資訊落差；代價是 draft 與可提供服務的內容必須分開管理。這次 review queue 仍是 pending，沒有人工核可。來源能否進入環境的准入審查是前面的另一個門檻，不能用後段內容 review 取代。」

**轉場**：「現在把這次確實驗證到的事情列清楚。」

**來源／素材**：SRC-04、SRC-05、SRC-14；來源准入是專案規約，本輪 fixture 沒有執行該 gate。

**驗收**：不稱 `status: draft` 自動阻止 serving；發布 gate 是整合要求，需實作與驗證。

### S15 — 本次執行結果與仍未回答的問題

**Timing:** `18:30–20:00` / 90 seconds. **Type:** `DEMO-EXECUTED`.

**本頁目的**：完成 15 分鐘 Wiki 案例，提供具體結果而非泛稱有效。

**投影文案**：

| Snapshot | Lint | 內容狀態 |
|---|---|---|
| baseline-v1 | 0 | v1 草稿 |
| stale-v2 | 0 | 刻意保留過時處理步驟 |
| missing-summary-v2 | 1 | 刻意缺頁，4 個問題 |
| revised-v2 | 0 | 已修訂，待人審 |

表下：「三頁 diff 已保存；v1 原件與 canonical 的跨快照 SHA-256 相同」。

**畫面**：一張四列表；旁邊只保留「結構通過 ≠ 內容核可」的短標註。完整命令與 hashes 放附錄 A05。

**揭露**：逐行展現，最後同時顯示可主張與未量測範圍。

**講者稿**：「這次能證明的是產物存在、工具確實執行、修改可回看，舊來源在快照間保持相同。它也證明這個構造案例能穿過結構檢查。仍沒有量到自動化成功率、工時、成本或線上答案改善。這些需要下一個實驗，不應從四份教學快照外推。」

**轉場**：「要把這些草稿放進 Teams，接下來只看兩個整合責任。」

**來源／素材**：SRC-15、SRC-17。

**驗收**：雜湊比較不冒充不可變存取控制或 Git history gate；exit 0 不標成全系統已驗收。

### S16 — 接軌點：KnowledgeService

**Timing:** `20:00–21:30` / 90 seconds. **Type:** `IMPLEMENTED` + `PROPOSED`.

**本頁目的**：只解釋業務流程與知識查詢的接口。

**投影文案**：`Teams workflow → search(query, user_context, …) → answer + sources`。下方三項接軌工作：「欄位與範圍映射」「實際權限過濾」「來源 URI 可解析」。

**畫面**：兩條泳道，業務流程只寫「追問／工單／人工接手」，知識服務只寫「證據／回答／引用」。Wiki bundle 用虛線接到需要驗證的映射層。最多五個主要節點，不塞八個 workflow node。

**揭露**：先現有介面，再 proposed Wiki 接軌。

**講者稿**：「Teams 的工單與接手流程有自己的責任，KnowledgeService 提供查詢與結果介面。Wiki 內容接過來，需要確保範圍欄位能對應、權限真的被執行、來源能被點開。介面存在可以讓這些工作有明確邊界，但不代表 bundle 已經直接相容。」

**轉場**：「第二個整合責任，是知識版本怎麼進入執行中的服務。」

**來源／素材**：SRC-07、SRC-08；不是本輪 demo 的 runtime 路徑。

**驗收**：不帶入 release 圖；三項工作不預設已完成；接口摘錄與原始碼一致。

### S17 — 知識更新與應用發布

**Timing:** `21:30–23:00` / 90 seconds. **Type:** `DOCUMENTED` + `PROPOSED`.

**本頁目的**：獨立說清楚知識版本與服務的關係。

**投影文案**：`已核可內容 → Immutable knowledge release → Active pointer → Agent 載入與驗證`。回滾箭頭標「選回已驗證的舊 release」。圖外：「應用程式 image 與知識 release 分開管理」。

**畫面**：最多四個節點加一條回滾線；由現有操作文件支持，Wiki bundle 接入點仍標 proposed。manifest 小註只列版本、hash、模型／向量相容性，不把完整JSON貼滿。

**揭露**：先發布路徑，最後回滾。

**講者稿**：「修完 Markdown 還不等於線上已用到它。Teams 專案的操作契約把知識 release 與應用程式 image 分開，Agent 讀取指定版本並驗證。Wiki 要接進來，也要走相同的發布責任，不能讓未核可草稿因檔案存在就被服務讀取。這頁說明現有契約與接軌要求，不代表本輪發布驗收。」

**轉場**：「這樣的責任邊界也影響我們如何選外部知識平台。」

**來源／素材**：SRC-09。

**驗收**：不說已部署或已回滾成功；本輪 hash snapshot 與 runtime release hash 是不同證據。

### S18 — 平台選型只比較介面後面的責任

**Timing:** `23:00–24:30` / 90 seconds. **Type:** `MEASURED` + `EXTERNAL` + `PROPOSED`.

**本頁目的**：保留選型脈絡，集中在一頁，不切斷 Wiki 主線。

**投影文案**：

| 對象 | 本次可引用的依據 | 尚需回答 |
|---|---|---|
| Hybrid | 原有介面與歷史 A/B | 語料與維護需求變化後的表現 |
| File Search | 同條件 30 題實驗；完整數據在 A04 | 權限語義、同步、引用粒度與維運成本 |
| WeKnora | 官方描述涵蓋 RAG、Agent、Wiki | 與本系統的介面及治理需求是否相容 |

下方一句：「企業服務規則留在 workflow；知識平台在明確契約下評估」。

**畫面**：三列證據狀態表，沒有星等、虛構勝負或功能打勾矩陣。表格旁只留一條 workflow／knowledge boundary。

**揭露**：先決策邊界，再逐列顯示證據狀態。

**講者稿**：「我們有 Hybrid 與 File Search 的歷史 A/B，但它是小語料與特定計分方式，完整條件放附錄。WeKnora 是官方文件上的外部參照，尚未在這裡整合。這一頁要帶走的是比較標準：後端能否滿足權限、來源、更新和成本的契約，而不是只看功能名稱。」

**轉場**：「下一次驗證應該讓我們有能力回答這些問題。」

**來源／素材**：SRC-02、SRC-10。外部官方描述沿用前輪查閱 2026-09-27 的紀錄，發布前須再確認版本。

**驗收**：不在主線新增第二組大數據圖；三者的證據程度清楚；WeKnora 未整合不被藏在筆記。

### S19 — 下一次量測：更新品質與維護成本

**Timing:** `24:30–26:00` / 90 seconds. **Type:** `PROPOSED`.

**本頁目的**：補上「值得投入多少」的工程判斷。

**投影文案**：

| 要量什麼 | 觀察方式 |
|---|---|
| 修改範圍是否正確 | 受影響頁面的 precision／recall，依事先標註的 holdout 變更集 |
| 是否保留有效條件 | 版本、scope、引用的內容回歸案例 |
| 人工負擔 | Review 時間、退回原因、修改次數 |
| 執行成本 | 端到端時間、模型使用量與實際費用 |

註記：「比較人工維護與 LLM 輔助；題目、來源事實與驗收條件固定」。

**畫面**：四列表，右側放一次更新從開始到 review 的時間線；所有數值留成指標名稱，不填虛構百分比。

**揭露**：先品質，後時間與費用。

**講者稿**：「要判斷這個做法是否值得，需要測影響範圍、內容回歸、審稿工時和執行成本。下一次應使用事先標註且未參與提示調整的更新案例，比較人工與 LLM 輔助的結果。這次三頁教學修訂只能提供可重跑的起點，不能推算百分比改善。」

**轉場**：「最後把方法縮成你回到團隊可以實作的一次小實驗。」

**來源／素材**：本 spec 的後續實驗設計；非完成結果。

**驗收**：候選不暗中多出來源事實；計入 review 工時；不以 token 數代替完整維護成本。

### S20 — 從一次來源更新開始

**Timing:** `26:00–28:00` / 120 seconds. **Type:** `SYNTHESIS`.

**本頁目的**：給觀眾可採取的方法，並重述這次真正展示的結論。

**投影文案**：

1. 選一份會更新的來源，保留更新前後版本。
2. 用一組固定問題，追查受影響的知識頁與引用。
3. 保存提案、diff、工具輸出與 review 結果，再決定是否擴大自動化。

主結語：「來源更新之後，知識也要留下可檢查的修改紀錄。」

**畫面**：回到 S02 的實際 query diff，旁邊疊加 source、check、review 三種產物入口；深色結語。證據包與來源索引提供可點擊入口，不新增第 21 張謝謝頁。

**揭露**：先重現來源與 diff，再出現三步方法。保留最後 20–30 秒停留畫面與邀請提問。

**講者稿**：「這次我們看到來源更新會改變答案，但結構正確仍可能留下過時步驟。LLM 可以協助提出修訂，原件、來源、diff 和工具結果讓這些修改可被檢查；內容核可仍需要明確責任。回到團隊，先找一份常更新的文件，保存兩個版本，配上一組固定問題，把更新走過一次。看清楚失敗與審稿成本，再決定擴大哪些自動化。案例包保留了四份快照與檢查輸出，可以用來理解這個驗證方式。謝謝，歡迎討論。」

**轉場**：主簡報結束；若被問到指標、欄位或重跑方式，使用附錄入口。

**來源／素材**：SRC-14–SRC-18。

**驗收**：結語回到開場的來源改版；沒有把 draft、lint 通過或示範產物當作正式上線。

## 5. 技術附錄

主線在 S20 結束，附錄不自動接著播放。閱讀模式全部可見；按需要從相關頁跳入並可返回。

### A01 — 156 題評測的指標與分母

**目的**：回答 RAG 量測範圍。**投影內容**：156 total、116 evidence-labeled、136 single-turn、20 multi-turn；Document Hit@4 115/116、Answer Accuracy 151/156、multi-turn 18/20、Citation Precision 98.82%。每個數值旁列定義。頁底放 commit bdd3894、release ID、freezeVersion 5、test split。

**畫面**：單一表格；dataset hash 與模型詳細 metadata 放閱讀模式。**講者稿**：「分母不同表示檢查的案例範圍不同。引用精確率也有自己的彙總定義。數字是固定快照的結果，不能直接推廣到其他語料或群組。」

**來源**：SRC-01。**驗收**：保留 group-gated corpus 未涵蓋的限制；不把 raw recallAt4 改稱 documentHitAt4。**預留回答時間**：90 秒。

### A02 — 答案遺漏與引用錯誤

**目的**：讓聽眾看懂不同診斷軸。**投影內容**：failure taxonomy 為 ANSWER_OMISSION 5、BAD_CITATION 3；另表列 GENERATION_IGNORED 12、CANDIDATE_MISS 1、SELECTION_OR_PACKING_DROP 1。兩表不能合併相加。

案例表：`v3-blind-ans-05` 的 candidate/retrieval/answer evidence recall 為 1/1/0，citation precision 為 1；`v3-blind-ans-23` 為 1/1/1，citation precision 為 0。

**畫面**：兩表加兩列案例，不放內部問題全文。**講者稿**：「答案遺漏與引用錯誤的處理方向不同。診斷欄位是定位線索，要回到 trace 確認根因。」

**來源**：SRC-01。**驗收**：8 筆 failure 不稱 8 題 answer accuracy 錯誤；12 個生成診斷不等同 12 題答案失敗。**預留回答時間**：90 秒。

### A03 — 知識頁欄位與來源責任

**目的**：回答資料格式如何支援維護。**投影內容**：直接節錄 revised-v2 的 query frontmatter 與正文，保留以下實際欄位：

```yaml
type: query
title: Managed client 4.1 DEMO-101
sources:
  - id: guide
    resource: ../sources/examplevpn-guide-v2.md
status: draft
classification: public
owner: team:demo-it
access_scope: public
contains_pii: false
retention: permanent
redaction: none
```

節錄已省略 generated；完整頁面在來源連結中可讀。不存在的 verified 不補寫。Source summary 另有 archive_slug 和 analysis_receipt，連到真實保存的來源／提案 digest；不能把 concept 或 query 模板當成 source schema。

**畫面**：最多 14 行 code 配三個註記：來源、內容狀態、治理責任。**講者稿**：「這些欄位支援追蹤，但不會自行執行權限或發布。generated 是產生紀錄，owner 是責任，verified 需要真實查核事件。」

**來源**：SRC-06、SRC-18。**驗收**：所有行可在 demo 找到；完整產物不以模板 placeholder 代替。**預留回答時間**：120 秒。

### A04 — Hybrid 與 File Search 的歷史 A/B

**目的**：保留先前選型證據，讓主線不必承擔第二段評測故事。

| 指標 | Hybrid | File Search |
|---|---:|---:|
| P50 | 3.00 s | 5.71 s |
| P95 | 4.07 s | 7.15 s |
| 平均每題成本 | US$0.001059 | US$0.001804 |
| 平均 LLM 呼叫次數 | 2.17 | 1.00 |
| 報告的 answer 代理指標 | 25/25 | 25/25 |
| No-answer | 5/5 | 5/5 |

**投影限制**：2026-08-07、30 題、19 份文件、同模型、top_k=4；品質以來源命中等代理判準計分。兩筆 ACL 案例都預期命中，另外的合成 ACL 探測不能代替真實語料群組驗收。

**畫面**：表格或零起點延遲圖＋完整表，保留單位。**講者稿**：「這批次的延遲與成本支持當時保留 Hybrid。語料小、計分特定，所以重點是可重跑的決策方法，不能推導通用優劣。」

**來源**：SRC-02。**驗收**：不把 100% 代理指標和 156 題 L3 分數畫改善曲線；不沿用 File Search 沒有圖片的過期說法。**預留回答時間**：120 秒。

### A05 — 重跑案例與證據包

**目的**：讓讀者能檢查與重跑這次保存的產物。

**投影內容**：四份 snapshots 的位置，四筆 lint 命令結果 `0 / 0 / 1 / 0`，以及 source → proposal → diff → logs → pending review 的檔案索引。

**完整重跑說明**：見 [案例 README](./evidence/wiki-update-demo/README.md)。使用現有 Python runtime 與既有工具的 `--root` 參數，對保存的 fixtures 執行；第三份 snapshot 預期失敗。這些命令重跑的是產物檢查，不會重新產生 LLM 回答。

**畫面**：一段命令範例＋四列結果；完整路徑、工具 hashes 與所有原輸出放閱讀模式，不要求觀眾抄長路徑。

**講者稿**：「資料都是虛構的，檢查輸出是真正執行過的。這裡能重跑結構檢查，也能直接閱讀 diff。若要重做模型生成或測量更新成功率，則要使用 S19 的獨立實驗設計。」

**來源**：SRC-14–SRC-18。**驗收**：刻意失敗不被隱藏；保留原始輸出；不宣稱重跑 fixture 等於端到端重現。**預留回答時間**：90 秒。

## 6. 設計與 HTML 呈現規格

### 6.1 設計方向

Design read: An evidence-led technical conference deck for developers, using an editorial engineering case-study layout with readable diagrams and document comparisons.

- `DESIGN_VARIANCE: 7`
- `MOTION_INTENSITY: 3`
- `VISUAL_DENSITY: 5`

主體採清晰的淺色技術頁，封面和結語使用深色。以文件對照、證據追蹤與架構圖建立視覺記憶。避免連續多頁純黑背景加大字，也避免用裝飾性插圖代替實際機制。

### 6.2 設計 token

| Token | Specification |
|---|---|
| Canvas | 1600×900 logical units, 16:9 |
| Background | `#F5F7F8` |
| Surface | `#FFFFFF`，只用於文件、程式碼或必要圖面 |
| Primary text | `#17242B` |
| Secondary text | `#4E6069` |
| Accent | `#126B62` |
| Rule / neutral diagram | `#CBD5D9` |
| Dark canvas | `#132326` |
| Dark text | `#F5F7F8` |
| Dark accent | `#8ED5C6`，同一色相的對比變體 |
| Main font | System CJK sans: PingFang TC, Noto Sans TC, Microsoft JhengHei, sans-serif |
| Code font | ui-monospace, SFMono-Regular, Consolas, monospace |
| Title size | 50–64 logical px；封面可 68–80 |
| Body size | 28–34 logical px |
| Dense labels / code | 24–28 logical px；必要時將次要細節移往閱讀區 |
| Source note | 18–20 logical px；影響結論的限制須至少 24 |
| Safe area | Left/right 80; top 64; bottom 72 logical px |

字級是 1600×900 設計座標的起點，需在 1280×720 與投影檢查後調整。不能以縮小全文到不可讀來通過溢出檢查。

### 6.3 頁型與資訊負荷

| Layout | Slides | 限制 |
|---|---|---|
| 來源與文件差異 | S01、S02、S06、S08、S13 | 一個主要差異焦點；細節可展開 |
| 作業／介面圖 | S03、S07、S09、S16、S17 | 每頁最多五至六個主要節點；每條箭頭有語義 |
| 實際檢查證據 | S10、S11、S12、S15 | 先展示來源與結果，再說明工具能證明什麼 |
| 責任與取捨 | S05、S14、S18、S19 | 少量可比較列，不做功能卡網格 |
| 歷史評測 | S04 | 兩個指標與一筆診斷，不展開第二段 RAG 課程 |
| 收束 | S20 | 回到 S02 的 diff 與可帶走的實驗方法 |

原生文字、表格與技術圖保持可編輯。S13 的完整 diff 在閱讀模式顯示，投影只選必要行。大圖超出節點上限時拆頁或移附錄，不縮小所有文字。

### 6.4 動畫

- 只用於順序、分支或來源對應，避免純裝飾循環。
- 一般轉頁 180–250 ms；圖內逐步高亮 250–400 ms。
- 不自動換頁、不自動啟動影片、不連續放大背景。
- 多步頁依序前進；返回時可退回前一步。
- 不延遲來源與關鍵限制的顯示；其必須與相應結論同時出現。
- `prefers-reduced-motion` 時移除移動效果，內容完整可見。

### 6.5 互動與分享

| Requirement ID | Behavior |
|---|---|
| UI-01 | 左右方向鍵、PageUp/PageDown 及空白鍵支援前進／後退；按鈕具相同功能 |
| UI-02 | Home/End 跳到主簡報首尾；附錄不改變主簡報頁數 |
| UI-03 | N 開關講者筆記，O 開關頁面總覽，F 請求全螢幕，Esc 關閉非全螢幕 overlay |
| UI-04 | 可直接使用 `#s01`–`#s20`、`#a01`–`#a05` 連到指定頁；未知 hash 回封面 |
| UI-05 | 保留原 `#1`–`#17` 數字連結的合理相容對應，見 §9；不得因舊連結白屏 |
| UI-06 | 閱讀模式顯示所有主頁、附錄、完整說明與來源；搜尋可找到正文 |
| UI-07 | 手機以閱讀模式為預設；圖或表可在自身區域水平捲動，正文不被等比例縮到過小 |
| UI-08 | 列印模式每頁完整呈現最終狀態，隱藏控制列與動畫；來源仍可讀 |
| UI-09 | 單一 HTML 可離線開啟；不依賴 CDN、API、線上字型或服務端 |
| UI-10 | 原始碼可維護；即使最終交付內嵌素材，也須保留可編輯文字、圖表資料與來源清單 |
| UI-11 | 所有控制可鍵盤操作、有可辨識標籤與焦點；hidden slides 不留可聚焦元素 |
| UI-12 | 全螢幕請求失敗時保持可操作，不顯示未捕捉例外；嵌入與檔案模式皆有按鈕退路 |

主簡報預設不依賴 live demo。S02、S11–S15 已提供離線的實際產物與檢查結果。若未來加入實機畫面，仍需保留靜態備援，並標示錄製日期與環境。

### 6.6 素材策略

- 現有兩張生成圖片可作封面視覺候選；須經整體風格檢查，不能因已存在就強制沿用。
- 核心素材由證據圖表、教學文件、schema、架構與回答路徑構成。
- 真實產品截圖只有在確有可公開內容且能支持該頁時採用；沒有截圖時使用明確標為示意的文字或流程。
- 圖中說明皆為繁體中文；程式碼與 metadata identifiers 用英文。
- 不下載、嵌入或散布內部分類的來源原文、操作畫面或可還原內容。
- 技術圖若用 SVG 實作，文字、節點、連線仍應可維護；裝飾性插畫另用合適素材，不以程式畫假產品截圖。
- 大型內嵌圖片使用正常 image element 或可驗證的資產載入方式；不得再依賴會被瀏覽器忽略的超長 CSS custom property。

## 7. 證據來源與版本

### 7.1 證據角色

主要論證由 DEMO-02 的來源、修訂及工具結果支持。156 題與 30 題報告只提供問答系統的既有脈絡，不再拿它們推導 Wiki 成效。

Teams 原始碼與文件依 v1 spec 查閱的 `2601aac3b22c6a4001b6bb682ecef6fb4bc5d652` 工作樹版本；Wiki 文件依 `0c02fd346e9711d8b556cc2b94c841a2185ac77e`。本輪檢查工具的實際 HEAD 與檔案 SHA-256 另以 `records/runs.json` 的 `toolProvenance` 為準。引用存在不代表本輪重跑了專案測試或雲端驗收。

### 7.2 Source registry

| ID | Source | 用於 | 限制 |
|---|---|---|---|
| SRC-01 | [Frozen L3 report](../teams-agent/data/eval/reports/rag-l3-v3-blind-full-live-20260923-bdd3894.json) | S04、A01、A02 | 指定歷史快照，不是 Wiki 實驗 |
| SRC-02 | [Retrieval A/B report](../teams-agent/docs/retrieval-ab-test-report.md) | S18、A04 | 小語料、代理指標、歷史設定與費用 |
| SRC-03 | [Wiki README](../llm-wiki-example/README.md) | S03、S08 | 範本定位與資料角色 |
| SRC-04 | [Ingest pipeline](../llm-wiki-example/docs/ingest-pipeline.md) | S09、S14 | 規約；本輪沒有執行自動 Ingest |
| SRC-05 | [Data governance](../llm-wiki-example/docs/data-governance.md) | S14、A03 | 治理與 runtime ACL 各有責任 |
| SRC-06 | [Wiki rules](../llm-wiki-example/AGENTS.md), [Source template](../llm-wiki-example/docs/templates/page-template-source.md), [Concept template](../llm-wiki-example/docs/templates/page-template-concept.md) | A03 | 本倉擴充不全是 OKF 必填 |
| SRC-07 | [KnowledgeService](../teams-agent/agent_service/src/agent_service/knowledge.py), [Contracts](../teams-agent/agent_service/src/agent_service/contracts.py) | S16 | 現有介面不表示 Wiki adapter 完成 |
| SRC-08 | [Workflow graph](../teams-agent/agent_service/src/agent_service/workflow_subgraphs.py) | S16 | 僅用於確認 workflow 與服務責任 |
| SRC-09 | [Knowledge release operations](../teams-agent/docs/knowledge-release-operations.md) | S17 | 文件契約，不等同本輪發布驗收 |
| SRC-10 | [WeKnora official repository](https://github.com/Tencent/WeKnora) | S18 | 前輪查閱 2026-09-27；未整合、未實測 |
| SRC-11 | [OKF specification](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md), [Local mapping](../llm-wiki-example/docs/okf.md) | 資料格式背景 | 依本倉採用版本，不稱全球最新 |
| SRC-12 | [Existing HTML](./index.html) | 遷移清單 | 不作技術證據 |
| SRC-13 | [Hybrid service](../teams-agent/agent_service/src/agent_service/knowledge_hybrid.py) | 問答系統背景 | 詳細 pipeline 已移出主線 |
| SRC-14 | [Demo README](./evidence/wiki-update-demo/README.md), [Creation record](./evidence/wiki-update-demo/records/creation.json) | S02、S03、S07、S14、S20、A05 | 互動式 Assistant 撰寫；不是獨立模型 API 實驗 |
| SRC-15 | [Executed commands and results](./evidence/wiki-update-demo/records/runs.json) | S11、S12、S15、A05 | 工具實測；不含 governance、history 或 runtime 檢查 |
| SRC-16 | [v2 change proposal](./evidence/wiki-update-demo/decisions/v2-change-plan.md) | S07、S09、S13 | 簡短變更提案；不是私有推理或人工核可 |
| SRC-17 | [Actual three-page diff](./evidence/wiki-update-demo/records/content-revision.diff) | S01、S02、S13、S15 | 合成內容的真實檔案差異 |
| SRC-18 | [v1 source](./evidence/wiki-update-demo/baseline-v1/raw/originals/examplevpn-guide-v1.md), [v2 source](./evidence/wiki-update-demo/revised-v2/raw/originals/examplevpn-guide-v2.md), [Stale graph report](./evidence/wiki-update-demo/stale-v2/ops/graph-insights.md), [Revised graph report](./evidence/wiki-update-demo/revised-v2/ops/graph-insights.md), [Final query](./evidence/wiki-update-demo/revised-v2/wiki/queries/demo-101.md) | S06、S08、S10、A03 | 合成產物與原樣保存的結構報告 |

### 7.3 分享時的引用

- 投影上保留必要的「合成案例」「工具實際執行」「待驗證」與分母，不反覆朗讀所有限制。
- 講者筆記記錄來源 ID、檔案、欄位和時間；閱讀模式可展開完整內容。
- 分享 HTML 內嵌公開合成案例的必要片段與原始工具輸出，或使用隨附、可搬移的相對資產。不依賴作者電腦絕對路徑。
- 既有專案原始碼與報告僅連結可公開版本；內部分類來源不複製進素材。
- graph report 原樣保留；圖中連結的方向與數值來自實際 snapshot。產生器輸出的相對連結如在獨立閱讀環境不適用，分享頁另建立正確的導覽，不改寫原始日誌。
- 上游 main 會變；正式製作時固定外部文件版本或記錄查閱日期，不把新版本功能套到歷史測量。

## 8. 素材與完成狀態

| Asset | 內容 | 狀態 |
|---|---|---|
| ASSET-01 | v1、v2 合成來源 | 已保存 |
| ASSET-02 | baseline、stale、missing-summary、revised 四份快照 | 已保存 |
| ASSET-03 | 簡短變更提案與 pending review queue | 已保存；未經人審 |
| ASSET-04 | 四份 lint stdout/stderr 與 exit code | 已執行、已保存 |
| ASSET-05 | 四份 graph reports | 已執行、原樣保存 |
| ASSET-06 | 三頁內容 revision diff | 已產生，68 行 |
| ASSET-07 | 舊來源跨快照 hashes 與工具 hashes | 已保存於 runs.json |
| ASSET-08 | S16 interface 圖、S17 release 圖 | 內容規格完成；視覺實作待完成 |
| ASSET-09 | 代表頁 S02、S11、S13、S16 的視覺樣稿 | 待製作 |
| ASSET-10 | 全部新版 HTML、閱讀模式與附錄 | 待依本 spec 實作 |

本規格與案例證據包已完成修訂。視覺成品、實際口述排練、自動化生成測試及端到端服務測試沒有被冒稱已完成。

## 9. 舊版內容遷移

### 9.1 v1 spec 到 v2

| v1 spec | v2 destination | 處置 |
|---|---|---|
| S01–S03 | S01–S03、S05 | 改由產物開場，未知條件提問退居背景 |
| S04–S09 | S04、A01、A02 | RAG 介紹與評測壓縮；與 Wiki 動機分開 |
| S10–S15 | S06–S15、A03 | 規約説明改由來源改版、失敗與 diff 串起來 |
| S16 理想對話 | S02、S11、S13 | 以保存的問答頁與修訂差異替代 |
| S17 整合大圖 | S16、S17 | interface 與 release 拆頁 |
| S18 後端 A/B | S18、A04 | 主線只保留決策角色，完整數據進附錄 |
| S19 WeKnora | S18 | 合併為外部候選與比較契約 |
| S20 | S19、S20 | 增加更新品質與 review 成本實驗 |
| A05 未來實驗 | S19、A05 | 主線講下一次量測，附錄提供已執行檢查的重跑方式 |

### 9.2 現有 HTML 的數字 hash 相容

本次核對的 HTML 已採 v1 規格的 20 頁主線與 5 頁附錄，使用 `#s01`–`#s20`、`#a01`–`#a05`，並保留更早 17 頁版本的數字 hash 對應。後續依 v2 更新內容時沿用這組具名 anchor；舊數字 hash 依下表調整至新版相應主題。v1 與 v2 的同號頁主題可能不同，內容遷移以 §9.1 為準。本次未修改 HTML。

| Old hash | New anchor | Old hash | New anchor |
|---|---|---|---|
| #1 | #s01 | #2 | #s02 |
| #3 | #s05 | #4 | #s04 |
| #5 | #s04 | #6 | #a02 |
| #7 | #s03 | #8 | #s08 |
| #9 | #a03 | #10 | #s09 |
| #11 | #s13 | #12 | #s16 |
| #13 | #a04 | #14 | #s18 |
| #15 | #s16 | #16 | #s19 |
| #17 | #s20 | — | — |

## 10. 驗收標準

### 10.1 內容與論證

- [ ] 20 頁主線＋5 頁附錄全部具備投影內容、畫面、講者說法、來源與驗收條件。
- [ ] 第 2 頁看得到真實保存的 Wiki 產物；第 3 分鐘前明確定義本例的 LLM Wiki。
- [ ] RAG 背景只占一頁；主要案例在第 5 分鐘開始。
- [ ] 三項決策各自包含選擇、替代方案、代價與本例適用理由。
- [ ] 核心案例有來源 v1/v2、提案、過時 snapshot、修訂 snapshot、diff、工具輸出與 pending review。
- [ ] 注入故障、Assistant 草稿、實際腳本結果與未執行的 runtime 清楚區分。
- [ ] 不宣稱 LLM 自動發現全部影響範圍、不宣稱工時節省或答案準確率已提高。
- [ ] Graph 結構線索不被描寫為語義判定；數量不變時仍檢查實際節點。
- [ ] 問答的 4.0／4.1+ 分支與來源一致；版本不明保留追問。
- [ ] 156 題與 30 題資料集分母、計分方式與日期不混用。
- [ ] 不把 draft、工具 exit 0、schema 欄位或可替換介面當成正式 serving 驗證。

### 10.2 版面與操作

- [ ] S02、S11、S13、S16 先做代表頁檢查，再擴展全 deck。
- [ ] S16 最多五個主要節點；S17 只有 release 主路徑與回滾，不重新塞回整個 workflow。
- [ ] S13 主畫面最多 10 行 diff，其餘在閱讀區；S11／S12 原始輸出不佔滿整頁。
- [ ] 各頁在 1920×1080、1600×900、1280×720 可讀；390×844 閱讀模式正文不縮成微字。
- [ ] 表格、數據與圖上的標籤與文件內容一致；虛線代表 proposed，不只靠顏色。
- [ ] 所有新與舊 anchor 可跳轉；附錄與子步驟不破壞主線頁數。
- [ ] 圖片、來源片段、筆記、閱讀及列印模式可離線使用。
- [ ] reduced-motion、鍵盤操作、焦點與全螢幕 fallback 可用。

### 10.3 證據與重跑

- [x] 四份 snapshot 已建立；四次 lint exit code 為 0、0、1、0。
- [x] 缺頁 snapshot 的 4 個 lint issue 原輸出已保存。
- [x] 四次 graph script 已執行；報告原樣保留。
- [x] 三頁 revision diff 及來源 hashes 已保存。
- [x] v1 raw 原件與 canonical 在所有快照 hash 相同。
- [ ] 最終分享版可從頁面開到對應來源／片段；不依賴本機絕對路徑。
- [ ] HTML 最終畫面與實際產物逐一對照；不以重新手打的假 terminal 輸出取代證據。

### 10.4 排練

- [ ] 主線時間相加為 28 分鐘，另留 2 分鐘；需實際排練而非只算字數。
- [ ] 開場 3 分鐘內，測試聽眾能說出這場如何使用 LLM Wiki。
- [ ] 聽完 S11，觀眾能解釋為什麼 lint 通過仍可能內容過時。
- [ ] 聽完 S13，觀眾能指出更新了什麼、來源在哪、哪個舊分支保留。
- [ ] 結束時，觀眾能提出一份適合做同類更新實驗的文件。

## 11. 後續製作順序

1. 以 S02、S11、S13、S16 製作代表頁，驗證真實文字、diff 和圖能否在投影距離讀懂。
2. 依本 spec 實作其餘主頁與附錄，資料內容從已保存 artifact 擷取，避免抄寫漂移。
3. 補全來源展開、閱讀模式、講者筆記與舊 hash 相容。
4. 進行視覺、操作、離線檢查及一次 28 分鐘排練。
5. 交付 HTML 與可搬移證據；部署與公開發布另依使用者指示。

目前完成的是本 spec 的修訂及範圍明確的案例執行。成品視覺品質、演講效果與真實系統效益各自需要對應驗證，不用單一自評分數替代。
