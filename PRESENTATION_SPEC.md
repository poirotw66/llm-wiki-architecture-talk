# LLM Wiki：企業內部知識問答系統的架構演進

## Document control

| Field | Value |
|---|---|
| Document ID | `llm-wiki-presentation-spec` |
| Version | `1.0` |
| Status | `Ready for content review` |
| Prepared on | `2026-09-27` |
| Language | Traditional Chinese; English identifiers and technical terms |
| Event | Hello World 2026 |
| Duration | 30 minutes: 28 minutes of planned narration + 2 minutes of buffer |
| Main slides | 20, including the cover and conclusion |
| Appendix slides | 5, excluded from the main presentation sequence |
| Target artifact | Standalone HTML presentation with presentation and reading modes |
| Current scope | Content, narrative, evidence, visual direction, interaction, and acceptance specification |
| Implementation status | This specification does not modify the existing HTML |

## 1. 簡報目標與受眾

正式題目固定為「LLM Wiki：企業內部知識問答系統的架構演進」。受眾是理解 LLM 與 RAG 基本概念、正在開發或導入企業 AI 的工程師、架構師與技術主管。假設觀眾知道 embedding 與檢索的大致用途，但不知道本專案的檔案結構、服務介面或評測方法。

觀眾聽完後，應能解釋以下問題：

1. 一次問答失敗，如何沿著來源、檢索、證據選擇、生成與引用定位問題？
2. LLM Wiki 裡的原件、canonical 稿、來源摘要、概念與實體各自負責什麼？
3. 來源如何轉成可追溯、可更新的知識？其中哪些步驟需要人工判斷？
4. 知識維護流程如何與 Teams IT Agent 的服務流程銜接？
5. 哪些結果已被測量，哪些只是設計方向，下一次應該驗證什麼？

核心論點：企業問答的可靠度取決於一整條證據鏈。Agent 與檢索改善「如何取得及使用證據」；LLM Wiki 為「證據如何被整理、連結及維護」提供一種工程做法。

這份簡報用架構責任的演進組織內容。未查證的開發日期、個人頓悟或導入順序不得補寫成歷史。現有量測不能直接證明 LLM Wiki 導入前後的準確率增益。

## 2. 敘事與資訊分層

### 2.1 五段敘事

| 段落 | 頁面 | 敘事任務 |
|---|---|---|
| 問題與系統邊界 | S01–S03 | 讓觀眾知道這場處理哪種企業問題，以及一次回答牽涉哪些責任 |
| Agentic RAG 與診斷 | S04–S09 | 說明執行流程、評測方法與實測落差，建立合理的知識工程動機 |
| LLM Wiki 的具體做法 | S10–S16 | 用同一個教學案例展示資料表示、轉換、關聯、治理與回答使用 |
| 服務整合與選型 | S17–S19 | 回到 Teams，說明責任介面、A/B 決策及 WeKnora 的參照角色 |
| 成果與下一步 | S20 | 明確交代已知結果、待驗證項目與觀眾可採用的方法 |

### 2.2 三種閱讀深度

- **投影畫面**：每頁一個主要問題、一項主要證據或機制；觀眾在 5–10 秒內能辨識主旨。
- **講者筆記與閱讀模式**：保存說明、具體例子、轉場與完整來源，讓會後讀者能自行理解。
- **技術附錄**：保存指標定義、案例診斷、完整 schema、實驗條件與驗收設計。

增加詳細度的方法是補足因果、例子、邊界及資料流。不得將講者稿全文塞進投影片，亦不得把主論證需要的限制全藏進附錄。

### 2.3 事實類型與呈現規則

| Type | 頁面可用標示 | 使用條件 |
|---|---|---|
| `MEASURED` | 指定日期／資料集的實測 | 有報告、分母與版本；不代表現在部署狀態 |
| `IMPLEMENTED` | 原始碼已有此介面／流程 | 可定位程式碼；未重跑測試時不宣稱本次驗證通過 |
| `DOCUMENTED` | 專案規約／操作契約 | 文件可支持；部署狀態需另外證明 |
| `ILLUSTRATIVE` | 合成教學案例 | 資料、對話和行為為示範；不計入評測 |
| `PROPOSED` | 設計方向／待驗證 | 明確以虛線或文字標示 |
| `EXTERNAL` | 官方文件描述／外部參照 | 註明來源與查閱日期；不等同本專案測試結果 |
| `FRAMING` | 問題設定／責任分類 | 用於組織說明，不假設它是實測發現 |
| `SYNTHESIS` | 綜合結論 | 只能收束先前頁面已有依據的內容 |

這些英文值是製作 metadata，不應全部變成投影畫面上的膠囊標籤。必要的中文限制用簡短圖說直接放在相關證據旁。

## 3. 固定案例與證據契約

### 3.1 教學案例 `DEMO-01`

使用完全虛構的 `ExampleVPN`、錯誤碼 `DEMO-101` 與示範服務台。它們不對應真實產品、公司、使用者或作業指引。所有涉及此案例的頁面顯示「合成教學案例」。

此案例展示「資料表示與回答策略」，不宣稱修正了任何真實 VPN 問題，也不宣稱已實際執行 LLM Wiki 或 Teams 的完整串接。

**開場提問**

> 我在筆電上登入 ExampleVPN，一直進不去。

此時尚不知道裝置是否受管理、用戶端版本或錯誤訊息。提問本身不能支持唯一根因。

**刻意簡化的舊式教學文件**

> ExampleVPN 登不進去時，先重新安裝；若仍有問題，聯絡服務台。

此段也是人工撰寫的示範素材。不得標成專案真實舊文件或真實模型輸出。

**完整的示範來源 `DEMO-SRC-01`**

| 欄位 | 合成值 |
|---|---|
| Title | ExampleVPN 裝置登錄與登入指南 |
| Version | `2.0` |
| Effective date | `2026-09-01` |
| Review date | `2026-12-01` |
| Scope | 示範組織管理的筆電、ExampleVPN 4.x |
| Source fact A | 在上述範圍內，`DEMO-101` 表示裝置登錄尚未完成 |
| Source fact B | 服務台須確認裝置登錄紀錄；來源未要求使用者重新安裝 |
| Source fact C | 無錯誤碼、非受管理裝置或版本不符時，來源不足以判定此根因 |
| Owner | `team:demo-it` |
| Classification | `public` |
| Access scope | `public` |
| PII | `false` |
| Redaction | `none` |
| Retention | `permanent`，僅指此虛構教學素材 |

**概念頁核心文案**

> 裝置登錄是 ExampleVPN 4.x 在受管理筆電上的適用條件之一。當符合指南範圍且出現 DEMO-101 時，服務台應確認裝置登錄紀錄。[D1] 無錯誤碼時，需先取得錯誤訊息與裝置資訊。

`[D1]` 對應 `DEMO-SRC-01` 的相應主張，也是附錄 schema 中 `sources[].id: guide` 的投影用名稱。正文須保留 scope，不能只留下「DEMO-101＝裝置未登錄」的無條件敘述。

**目標回答劇本**

1. 使用者：「我在筆電上登入 ExampleVPN，一直進不去。」
2. 助理：「畫面顯示什麼錯誤訊息？這是受管理的筆電嗎？使用哪個用戶端版本？」
3. 使用者：「受管理筆電、4.x，畫面是 DEMO-101。」
4. 助理：「依示範指南 v2.0，這組條件下的 DEMO-101 對應裝置登錄未完成。請由示範服務台確認登錄紀錄。[D1] 這份指南沒有提供重新安裝作為處理步驟。」

這是設計行為的教學劇本。不得以聊天截圖外觀或「實測」標籤暗示它是已保存的真實執行結果。

### 3.2 真實量測 `EVAL-L3-01`

固定引用報告 `rag-l3-v3-blind-full-live-20260923-bdd3894.json`，不使用「最新」或「現在達到」等字眼。

| 項目 | 固定值／解讀 |
|---|---|
| Dataset | `retrieval_eval_v3_blind.json`，test split |
| Total cases | 156 |
| Evidence-labeled cases | 116 |
| Single-turn / multi-turn | 136 / 20 |
| Document Hit@4 | 99.14%；由比例與 116 題分母換算為 115/116 |
| Answer Accuracy | 96.79%；由比例與 156 題分母換算為 151/156 |
| Multi-turn Answer Accuracy | 90%；18/20 |
| Citation Precision | 98.82%；保留報告定義，不換算為引用筆數 |
| Failure categories | `ANSWER_OMISSION`: 5；`BAD_CITATION`: 3 |
| Evidence drop diagnostics | `GENERATION_IGNORED`: 12；`CANDIDATE_MISS`: 1；`SELECTION_OR_PACKING_DROP`: 1 |
| ACL coverage | `CORPUS_HAS_NO_GROUP_GATED_DOCUMENTS` |
| Commit | `bdd3894f7a99c07230ebd8069b1179e0be77f601` |
| Release | `release-4f49088db9ca` |
| Completed at | `2026-09-22T18:15:53.449649+00:00`，臺灣時間為 2026-09-23 |

`failureTaxonomy` 與 `evidenceDropStages` 是不同診斷維度，不相加、不畫成同一份圓餅圖。8 筆 failure entries 不等於 8 題 Answer Accuracy 錯誤。零 ACL 洩漏次數不能代表已涵蓋群組受限文件。

### 3.3 後端實驗 `AB-01`

固定引用 `docs/retrieval-ab-test-report.md` 內 2026-08-07 的報告。它與 `EVAL-L3-01` 使用不同資料集和評分定義。

| 指標 | Hybrid | Gemini File Search |
|---|---:|---:|
| P50 latency | 3.00 s | 5.71 s |
| P95 latency | 4.07 s | 7.15 s |
| Average reported cost per query | US$0.001059 | US$0.001804 |
| Average LLM calls per query | 2.17 | 1.00 |
| Reported answer metric | 25/25 | 25/25 |
| No-answer cases | 5/5 | 5/5 |

共同條件：30 題、19 份文件、`top_k=4`、同一模型 `gemini-3.5-flash-lite`。模型名稱屬歷史實驗 metadata，不作現時模型推薦。

報告中的 Answer Accuracy 以來源文件是否正確命中為準，不能改寫成人工驗證答案全部正確。兩筆 ACL 測試都預期命中，無法比較權限辨識能力。報告另外記錄合成受限文件的 ACL 探測通過，這項結果須獨立陳述。

## 4. 逐頁內容規格

每頁以下列內容作為實作依據：精確標題、投影文案、畫面與揭露順序、講者稿、來源、驗收條件。講者稿是可直接練習的核心說法；主持停頓、指圖與例子解說也計入分配時間。

### S01 — LLM Wiki：企業內部知識問答系統的架構演進

**Timing:** `00:00–00:45` / 45 seconds. **Type:** `FRAMING`.

**本頁目的**：建立分享範圍與整場問題。

**投影文案**

- 正式題目完整保留，斷行以「LLM Wiki：／企業內部知識問答系統／的架構演進」為優先。
- 副標：「一次回答背後，知識如何被取得、整理與維護」
- 「Hello World 2026 · Justin」；不自行新增職稱或組織。

**畫面**：深色封面。題目占左側約 60%；右側用 DEMO-01 的文件片段與來源連結構成一個可讀的內容局部。右側必須能辨識「來源、主張、引用」的關係。裝飾性照片最多作低對比背景，不承擔說明。

**揭露**：直接呈現完整標題，300 ms 淡入即可；不逐字打字。

**講者稿**：「今天分享的是企業內部問答的架構思考。我會先說 Agentic RAG 怎麼找資料，再看評測告訴我們哪些問題還存在，接著用一個完整例子說明 LLM Wiki 如何整理來源與維護知識。最後回到 Teams IT Agent，討論這些知識怎麼進入服務流程，以及哪些部分適合交給共用知識平台。」

**轉場**：「先從一個每個服務台都可能遇到的提問開始。」

**來源／素材**：講題來自本任務；案例局部使用 DEMO-01。

**驗收**：正式題目不被改寫；沒有模型能力、上線狀態或效益數字的無來源宣稱。

### S02 — 一句提問，還缺哪些條件？

**Timing:** `00:45–02:00` / 75 seconds. **Type:** `ILLUSTRATIVE`.

**本頁目的**：讓觀眾看到輸入不完整如何影響回答。

**投影文案**

> 「我在筆電上登入 ExampleVPN，一直進不去。」

- 錯誤訊息：未知
- 裝置狀態：未知
- 用戶端版本：未知
- 下方結論：「目前資訊不足以選定處理方式」
- 圖說：「ExampleVPN 為合成教學案例」

**畫面**：一個大型提問置於畫面上半；下半三條細註記直接連到問題中的「登入」「筆電」「ExampleVPN」。以空白與標註呈現未知，不使用三張功能卡。

**揭露**：先顯示提問並停 3 秒，再一次顯示三項未知。這是整場唯一安排的觀眾思考停頓。

**講者稿**：「如果系統立刻回答重新安裝，聽起來很有行動感，但這句提問其實沒有給我們錯誤訊息、裝置狀態或版本。問題可能需要追問，也可能已有適用的指南。我們先保留這個案例，後面會用它追蹤來源如何被整理，以及回答怎麼取得足夠依據。」

**轉場**：「要處理這個缺口，需要先看一次回答穿過哪些系統。」

**來源／素材**：DEMO-01。所有對話以可編輯文字呈現。

**驗收**：不提前出現 DEMO-101；不把未知條件當成已知；不展示真實使用者對話。

### S03 — 企業問答的責任分工

**Timing:** `02:00–03:15` / 75 seconds. **Type:** `IMPLEMENTED` + `PROPOSED`.

**本頁目的**：建立後續所有頁面共用的系統地圖。

**投影文案與圖中節點**

1. 服務入口：Teams／使用者身分／對話。
2. 業務流程：辨識問題／追問／工單／人工接手。
3. 知識服務：取得證據／產生回答／提供來源。
4. 知識維護：來源整理／責任人／版本／更新。

下方結論：「一次可靠的回答，需要這些責任彼此對齊」

**畫面**：四條橫向泳道。實線標示 Teams Agent 中可由程式碼定位的呼叫邊界；「LLM Wiki 範本 → 知識服務」用虛線並標「接軌設計」。禁止以一條無標示箭頭暗示兩個 repository 已串接。

**揭露**：入口與業務流程先出現，接著知識服務，最後知識維護。後續章節沿用這張圖的節點名稱。

**講者稿**：「Teams 接收訊息，業務流程負責追問、工單與人員接手，知識服務處理證據與回答。這次另外要放大的，是來源怎麼變成可維護的知識。圖上的虛線代表接軌方向；Wiki 範本與 Teams Agent 是不同的實作脈絡，不能因為畫在一起就當成整合已完成。」

**轉場**：「先放大知識服務裡的一次查詢。」

**來源／素材**：SRC-07、SRC-08；Wiki 範本角色依 SRC-03。

**驗收**：業務流程與檢索內部流程分層；原始碼存在與部署驗收分開。

### S04 — Agentic RAG 的查詢流程

**Timing:** `03:15–04:45` / 90 seconds. **Type:** `DOCUMENTED` + `IMPLEMENTED`.

**本頁目的**：解釋系統如何取得與使用證據。

**投影文案與圖中節點**

`Query + User context → Retrieval → Relevance check → Evidence selection → Answer + Citations`

- Retrieval 下方：「詞彙與向量訊號」
- Relevance check 分支：「必要時改寫查詢並重查」
- 全流程上方：「受時間、呼叫次數與證據 token 預算限制」
- 圖說：「依專案結構整理的概念圖；非逐函式呼叫圖」

**畫面**：橫向主路徑，占畫面 70%；回查箭頭只畫一個清楚回圈。用線條粗細和文字區分條件分支；不畫出每次都執行的多 Agent 循環。

**揭露**：沿查詢方向高亮；回查分支最後出現。閱讀與列印模式顯示完整圖。

**講者稿**：「Agentic RAG 讓查詢過程能根據結果調整。先找到候選，再判斷相關性，必要時改寫問題或補查，最後選擇證據交給回答階段。這裡的自主性仍需要預算。每次多查一次，都會增加延遲或成本；每個候選也不一定能放進最後的 context。」

**轉場**：「所以除了能不能查到資料，我們也要決定何時繼續、何時追問、何時停止。」

**來源／素材**：SRC-13；概念圖節點以查閱的 pipeline 檔案為準。

**驗收**：不虛構每題都有 planner；不標示未測量的逐階段毫秒數；不以無限回圈表示自主搜尋。

### S05 — 查詢控制與停止條件

**Timing:** `04:45–06:00` / 75 seconds. **Type:** `ILLUSTRATIVE` + `PROPOSED`.

**本頁目的**：說明控制流程改善的是決策與查詢策略。

**投影文案**

| 目前資訊 | 合理的下一步 |
|---|---|
| 關鍵條件未知 | 追問錯誤訊息、裝置與版本 |
| 已找到適用證據 | 回答並附來源 |
| 資料互相衝突或不適用 | 說明缺口，轉人工確認 |
| 執行預算用完 | 回報未完成原因，保留後續路徑 |

頁底：「查詢策略能改善證據取得；文件本身的缺口仍需處理」

**畫面**：左側 DEMO-01 的已知／未知欄位，右側決策表。使用連續對照，不做聊天 UI 操作演示。

**揭露**：從第一列走到最後一列；每列只高亮一次。表內行為標「設計判準」，不等同每一條已部署。

**講者稿**：「同樣是沒有回答，缺少使用者條件、來源不足和執行逾時是不同原因，後續處理也不同。這張表是我們用來檢查設計的判準。Agent 可以透過追問補足資訊，透過重查取得證據，但文件若沒有適用範圍，還是需要從來源整理這一端處理。」

**轉場**：「接著用評測把『看起來能回答』拆成可檢查的結果。」

**來源／素材**：DEMO-01；本頁為設計判準，不引用無法對應的線上結果。

**驗收**：逾時與查無資料分開；不把 Wiki 當成所有執行失敗的解法。

### S06 — 評測資料與判定範圍

**Timing:** `06:00–07:30` / 90 seconds. **Type:** `MEASURED`.

**本頁目的**：先建立數字的意義，再展示數字。

**投影文案**

- 主標示：「156 題 frozen blind test · L3 live-model run」
- 測試組成：「136 題單輪 + 20 題多輪」
- 證據標註：「116 題有目標證據標註」
- 三個檢查點：「目標文件有沒有進來？／答案是否符合評測？／引用是否對齊？」
- 限制：「指定模型與 knowledge release 的單次結果；未涵蓋真實群組受限語料」

**畫面**：156 題的總體水平帶，單輪與多輪依 136:20 分段；另以獨立括線表示 116 題證據標註，不能畫成與單輪／多輪互斥的第三組。右下保留資料集與報告日期。

**揭露**：先總體，再兩種不同的分類方式。口述說明「有證據標註」與「多輪」不是同一分類維度。

**講者稿**：「這次量測共有 156 題，包含 20 題多輪；其中 116 題有目標證據標註。因此不同指標的分母可能不同。這是固定資料集、模型與知識 release 上的一次執行，適合用來定位這個版本的問題。它沒有涵蓋真正的群組受限文件，所以不能只靠零洩漏次數就宣稱 ACL 已完成驗證。」

**轉場**：「在這個範圍內，檢索命中與最後答案分別得到什麼結果？」

**來源／素材**：SRC-01；更完整定義見 A01。

**驗收**：156、136、20、116 均正確；圖中不暗示分類互斥；不稱生產流量測試。

### S07 — 文件命中與答案正確率

**Timing:** `07:30–09:00` / 90 seconds. **Type:** `MEASURED`.

**本頁目的**：呈現量測結果及指標邊界。

**投影文案**

| 指標 | 結果 | 分母 |
|---|---|---|
| Document Hit@4 | **99.14%** | 115/116 題證據標註案例 |
| Answer Accuracy | **96.79%** | 151/156 題全部案例 |

- 結論：「找到目標文件後，答案與引用仍需要各自檢查」
- 必見註記：「兩項指標分母不同，不以百分點相減解讀流失」
- 次要資訊放筆記：「多輪 Answer Accuracy 為 18/20」

**畫面**：兩個上下排列的獨立證據區，各有 0–100% 的短比例軸、數字和分母。不可使用兩段 funnel、共同損失區塊或減法箭頭。

**揭露**：文件命中先出現，答案結果其次，最後顯示分母提示。

**講者稿**：「有證據標註的題目中，115 題能在前四份文件命中目標。全體 156 題的答案正確率則是 151 題。這兩個分母不同，我們不直接相減。它們提醒我們，文件命中只是其中一個檢查點；還要看證據是否被使用、回答是否遺漏，以及引用是否真的對到主張。」

**轉場**：「下一頁把平均數拆成一筆可以追蹤的失敗。」

**來源／素材**：SRC-01，EVAL-L3-01；不插入 AB-01 的 100% 指標。

**驗收**：百分比四捨五入至小數第二位；分母與單次測量範圍可在投影上讀到。

### S08 — 一筆答案遺漏案例的證據路徑

**Timing:** `09:00–10:45` / 105 seconds. **Type:** `MEASURED`.

**本頁目的**：展示實際診斷方式，建立技術深度。

**投影文案**

- Case ID：`v3-blind-ans-05`
- `candidateRecallAt24 = 1.0`
- `retrievalEvidenceRecall = 1.0`
- `answerEvidenceRecall = 0.0`
- Failure category：`ANSWER_OMISSION`
- 結論：「候選與檢索證據已涵蓋目標；答案未涵蓋該證據」
- 限制：「以上為單一案例的報告診斷值；尚不能單憑此定位具體程式根因」

**畫面**：三個檢查站，按候選、檢索、答案順序排列；同一個抽象 evidence token 從前兩站走到第三站，以空心輪廓表示未被答案涵蓋。不得填入想像的原始問題、段落或模型回答。

**揭露**：逐站顯示。最後補一條調查支線：「需檢查證據傳遞、prompt、生成與評分 trace」。

**講者稿**：「這是報告中的實際案例 ID。候選與檢索證據召回值都是 1，答案證據召回是 0，分類為答案遺漏。它支持我們把調查重點往後段移動，但還不足以只憑三個數字判定是哪個函式或模型決策造成的。這也是為什麼先分類很重要：若一開始就換 embedding，未必處理到這個案例的問題。」

**轉場**：「把這種診斷方法套到整體，就能清楚區分各層責任。」

**來源／素材**：SRC-01 的 `failures` 中指定 case。只展示 ID 與數值，不複製內部問題文字。

**驗收**：三項數值逐欄對應；不將 retrieval recall 1.0 描述成已驗證 prompt 內必然完整保留所有證據。

### S09 — 問題所在層與工程處置

**Timing:** `10:45–12:15` / 90 seconds. **Type:** `MEASURED` + `FRAMING`.

**本頁目的**：完成評測到知識工程的合理轉場。

**投影文案**

| 問題所在層 | 檢查內容 | 對應工作 |
|---|---|---|
| 來源 | 範圍、版本、矛盾、責任人是否清楚 | 知識整理與維護 |
| 取得與傳遞 | 授權、召回、選擇、context 是否正確 | 檢索與證據管線 |
| 回答與引用 | 主張是否完整、引用是否支持主張 | 生成與引用修正 |

下方量測註記：「本次報告：答案遺漏 5；引用錯誤 3」

下方轉場句：「LLM Wiki 處理的是來源整理與維護這一層」

**畫面**：三條責任泳道，量測計數只貼在回答與引用一列。來源一列沒有量測數字，標「設計關注」。

**揭露**：先重現已測到的回答問題，再展開完整診斷表。不能由 5+3 畫箭頭直接指向「Wiki 有效」。

**講者稿**：「這份報告實際量到的是答案遺漏與引用錯誤。我們應該修這些問題。同時，來源是否說清楚版本、適用範圍與責任人，是另一項需要獨立管理的工程工作。接下來介紹的 LLM Wiki，是處理這層責任的做法；目前沒有同條件前後實驗，不能說這些錯誤已被 Wiki 解決。」

**轉場**：「先定義一份可維護的知識，至少要帶著哪些資訊。」

**來源／素材**：SRC-01、SRC-03–SRC-06。

**驗收**：8 筆 failure entries 不等同 8 題答案錯誤；來源問題不冒充本報告的實測分類。

### S10 — LLM Wiki 的知識單位

**Timing:** `12:15–13:30` / 75 seconds. **Type:** `DOCUMENTED` + `ILLUSTRATIVE`.

**本頁目的**：提供可操作的 LLM Wiki 定義。

**投影文案**

> 本例的 LLM Wiki：由來源支持、以 Markdown 頁面與連結組織，並由 Agent 和人共同維護的知識集合。

一份可用知識旁的標註：

- 說什麼：主張與操作內容。
- 何時適用：版本、日期、條件。
- 根據什麼：來源與逐項引用。
- 由誰負責：owner、審查紀錄。
- 如何維護：狀態、更新與關聯頁。

**畫面**：中央是一頁 DEMO-01 知識內容，五種資訊直接標在相應位置；延續全場的來源連結視覺。

**揭露**：先正文，再顯示來源與其他標註。保留正文在第一視覺層級。

**講者稿**：「這裡用 LLM Wiki 指的是一種來源支持的知識集合，頁面會被整理、互相連結，也要有人負責。整理後的文字仍需要保存適用條件。我們採用的範本以 Markdown 和 OKF v0.2 表達內容，再加上本專案的歸檔與治理規約。這是這個範本的設計，不代表所有叫 LLM Wiki 的工具都採用相同格式。」

**轉場**：「先沿著一份輸入文件，看它如何變成這種知識頁。」

**來源／素材**：SRC-03、SRC-06、SRC-11；DEMO-01。

**驗收**：LLM Wiki 不被誤定義成單一產品或通用標準；OKF 與本倉擴充分開。

### S11 — 一份來源的 Ingest 流程

**Timing:** `13:30–15:00` / 90 seconds. **Type:** `DOCUMENTED`.

**本頁目的**：把管線講成具體責任與產物。

**投影文案與圖中階段**

`輸入 → 准入檢查 → 轉換與歸檔 → 分析 → 知識頁與連結 → Review 與留痕`

- 准入檢查：分類、PII、來源核可。
- 轉換與歸檔：原件、canonical、必要視覺證據。
- 分析：概念、實體、既有連結、矛盾與缺口。
- 知識頁與連結：來源摘要、概念、實體、index。
- Review 與留痕：待查核項目、log、快取。

**畫面**：六階段水平流程；分析階段下方用一條小支線表示中間分析稿。這是完整 0–16 步規約的簡化投影，不列所有命令。

**揭露**：一次顯示兩階段，合計三次。將來源核可標成寫入前的門檻；內容 review 在後段。

**講者稿**：「Ingest 的第一件事是確認資料能不能被處理與保存。接著才轉換、歸檔，並先分析概念、實體及既有知識關聯，再寫 Wiki 頁。範本要求保留來源摘要，最後更新索引、review queue 與日誌。來源准入會阻擋不合適的輸入；後段的內容 review 可以非同步進行，兩者目的不同。」

**轉場**：「其中最容易混淆的，是原件、canonical 與 Wiki 摘要為什麼需要分開。」

**來源／素材**：SRC-04、SRC-05。

**驗收**：來源核可在歸檔前；內容 review 不被畫成所有 Wiki 寫入前的必經核准；SHA 快取只在筆記提及，不搶主線。

### S12 — 原件、Canonical 與 Wiki 摘要

**Timing:** `15:00–16:45` / 105 seconds. **Type:** `DOCUMENTED` + `ILLUSTRATIVE`.

**本頁目的**：用完整對照說清楚三種資料產物。

**投影文案**

| 層 | 保存內容 | 更新方式 |
|---|---|---|
| `raw/originals` | 原始輸入的位元副本 | 保留原件，新版本另存 |
| `raw/sources` | 盡量完整還原的 canonical Markdown | 新修訂另建歸檔 |
| `wiki/sources` | 可閱讀的來源摘要與主張連結 | 依來源更新知識頁 |

示範片段按層顯示：

- 原件：`ExampleVPN guide v2.0`，頁面上有 scope 表與處理說明。
- Canonical：範圍、`DEMO-101` 語義、服務台處理及未涵蓋條件皆保留。
- Wiki 摘要：「受管理筆電、4.x、DEMO-101 → 服務台確認裝置登錄。[D1]」

**畫面**：由左至右的三欄文件對照，每欄有不同內容密度；以相同底線連出同一組適用條件。文件可以有自然邊框，但不可做成三張產品功能卡。

**揭露**：先看原件，接著 canonical 的保留項，最後縮成 Wiki 摘要。適用條件在三層中保持高亮。

**講者稿**：「原件讓我們回到當時收到的資料，canonical 讓不同格式的內容能以一致文字形式被檢查，Wiki 摘要則支援閱讀與重用。摘要可以變短，適用條件不能消失。若來源更新，我們留下新的歸檔，讓讀者仍能追查先前版本的依據。」

**轉場**：「要讓這些頁面能被管理，光有正文還不夠。」

**來源／素材**：SRC-03、SRC-04；DEMO-01。

**驗收**：canonical 不稱摘要；資料減量不表示無損壓縮；原件不可變不等於自動獲准公開。

### S13 — 知識頁的來源與生命週期

**Timing:** `16:45–18:15` / 90 seconds. **Type:** `DOCUMENTED` + `ILLUSTRATIVE`.

**本頁目的**：展示 metadata 如何支持維護。

**投影文案**：使用下列精簡 frontmatter 摘錄，不把它標成完整 schema。

```yaml
type: concept
title: ExampleVPN device enrollment
sources:
  - id: guide
    resource: ../sources/examplevpn-guide-v2.md
status: draft
stale_after: "2026-12-01"
owner: team:demo-it
classification: public
access_scope: public
```

右側說明：

- `sources`：主張回到哪份來源。
- `status` / `stale_after`：內容狀態與重看日期。
- `owner`：負責維護與判斷的人或團隊。
- `classification` / `access_scope`：治理資訊；實際授權仍由服務執行。

**畫面**：左側約 55% 為十餘行可編輯程式碼，右側是對應行的細註記。頁底：「節錄；完整合成頁面見附錄 A03」。

**揭露**：先來源，再生命週期，最後責任與治理；同時高亮對應行。

**講者稿**：「這些欄位讓知識除了文字之外，還有可追蹤的維護資訊。sources 指向依據，status 和 stale_after 提醒我們內容狀態，owner 承擔內容責任。分類欄位只記錄治理決策；真正的讀取權限仍需要 repository 與應用服務執行。欄位存在本身不會自動完成授權控制。」

**轉場**：「除了頁面自己的資訊，頁面之間的連結也要有用途。」

**來源／素材**：SRC-05、SRC-06、SRC-11。

**驗收**：`owner` 不誤等同 `generated.by`；不造假 `verified: human`；`draft` 不宣稱已人審通過。

### S14 — 來源、概念與實體的關係

**Timing:** `18:15–19:30` / 75 seconds. **Type:** `DOCUMENTED` + `ILLUSTRATIVE`.

**本頁目的**：說明 Wiki 連結如何支持查閱與維護。

**投影文案與圖中節點**

- Source：ExampleVPN 登入指南 v2.0。
- Concept：裝置登錄與登入適用條件。
- Entity：ExampleVPN 4.x。
- Query：出現 DEMO-101 時應確認什麼？

箭頭語義：`來源支持主張`、`概念適用於實體`、`問答引用概念與來源`。主結論：「來源更新時，可以沿連結檢查相關知識頁」。

**畫面**：四個節點的可讀關係圖，線條標明語義；不用數十節點的星空網絡。圖說：「頁面關係示意；不代表已部署 GraphRAG」。

**揭露**：先 source 與 concept，再 entity，最後 query；保留所有標籤。

**講者稿**：「來源頁回答資料從哪裡來，概念頁整理可重用的知識，實體頁描述具體系統，問答頁保存可重用問題。連結讓維護者知道一份指南更新後，還有哪些頁面可能需要重看。這張圖描述文件關係，不代表 runtime 一定會做圖遍歷，也不代表我們已量到 GraphRAG 的效益。」

**轉場**：「連結能指出影響範圍，但內容如何被確認與更新，仍需要操作規則。」

**來源／素材**：SRC-03、SRC-04、SRC-06。

**驗收**：箭頭方向與圖例一致；雙向連結不表示雙向因果；不宣稱自動語義矛盾判定已實現。

### S15 — 來源准入與內容審查

**Timing:** `19:30–21:00` / 90 seconds. **Type:** `DOCUMENTED`.

**本頁目的**：呈現實際治理分工，讓觀眾知道哪些工作不能只交給生成模型。

**投影文案**

| 階段 | 要回答的問題 | 責任與結果 |
|---|---|---|
| 寫入前的來源准入 | 這份資料能否進入指定環境？ | 人工確認分類、scope、PII；核可綁定來源 digest |
| 產物驗證 | 這些衍生檔是否來自核可來源？ | 每個產物各自留下 lineage 與 digest |
| 寫入後的內容 review | 主張是否正確、完整、仍適用？ | Review queue 與責任人處理內容缺口 |

頁底：「來源核可與內容正確性是不同問題」

**畫面**：一條從來源到 Wiki 的主流程，上下兩條審查泳道；寫入前准入畫門檻，寫入後 review 畫回到內容的迴圈。`stable` 只作內容狀態，不能直接連到「正式發布」。

**揭露**：先完整主流程，再補兩層人工責任；以文字和線型表示差異。

**講者稿**：「來源可以保存，不表示內容每一項都已被確認；內容看起來合理，也不表示它能進公開環境。範本把兩件事分開：來源准入在寫入前完成，產物逐檔保留 lineage，內容疑問則進入 review queue。模型可以協助提出待查核項目，但不能把自己的判斷記成人工審核。」

**轉場**：「接著把整理好的知識帶回開場問題，看回答策略應該如何改變。」

**來源／素材**：SRC-04、SRC-05。

**驗收**：准入 approval、editorial review、runtime publication 三者不混用；不把 CI 描述為完整 DLP 或人工判讀替代品。

### S16 — 同一問題的回答證據鏈

**Timing:** `21:00–23:00` / 120 seconds. **Type:** `ILLUSTRATIVE` + `PROPOSED`.

**本頁目的**：完成案例，展示 Wiki 資訊如何支持回答決策。

**投影文案**

左側對話依 DEMO-01 的四段劇本完整呈現，必要時分兩步展開。右側固定顯示：

| 檢查點 | 本案例的資訊 |
|---|---|
| 身分與可見範圍 | 合成公開知識 |
| 適用條件 | 受管理筆電、4.x、DEMO-101 |
| 使用來源 | 示範指南 v2.0，[D1] |
| 支持的動作 | 由示範服務台確認登錄紀錄 |
| 未支持的動作 | 直接要求重新安裝 |

頁底必見：「設計行為示範，未作為導入成效量測」

**畫面**：左側約 60% 為四段簡潔對話，右側約 40% 為證據表；回答中的「這組條件」「確認登錄紀錄」「[D1]」分別連到表格對應列。使用對話文本排版，不冒用真實 Teams 截圖。

**揭露**：第一步重現原始提問與追問；第二步顯示補充資訊；第三步顯示有來源的回答。主簡報頁碼仍是 S16，子步驟以 `1/3` 輔助顯示。

**講者稿**：「現在回到同一個問題。第一次提問缺少條件，所以先追問；當使用者補上裝置、版本與錯誤碼，才選用對應指南。回答中的動作由來源支持，沒有把指南沒說的重新安裝補進去。這個示範的價值在於把條件、來源與答案連起來。這是我們希望系統遵循的行為；若要宣稱改善了準確率，還需要固定題目與設定做前後比較。」

**轉場**：「當這個能力進入 Teams，回答之外還有完整的服務流程。」

**來源／素材**：DEMO-01；設計依據為 S10–S15 的表示與治理規則。

**驗收**：D1 真的指向完整示範來源；回答沒有新增來源外的操作；沒有寫成實際成功工單或已跑通整合。

### S17 — Teams IT Agent 與 KnowledgeService

**Timing:** `23:00–24:45` / 105 seconds. **Type:** `IMPLEMENTED` + `DOCUMENTED` + `PROPOSED`.

**本頁目的**：將知識設計放回現有業務架構，說清楚接軌點與缺口。

**投影文案與圖中節點**

- Teams workflow：「載入對話 → 接手分流 → 擷取問題 → IT 分流 → 處理問題 → 接手判斷 → 回覆與保存」；人工已接手時另有旁路。
- 接口摘錄：`search(query, user_context, ...) → KnowledgeResult`。
- Result 核心：「found、answer、sources、images、backend」。
- Wiki 接軌虛線：「內容欄位映射／權限映射／來源 URI／release 發布」。
- 下方：「介面存在；Wiki bundle 接軌仍需逐項驗證」

**畫面**：上半呈現業務 workflow，中央放大 KnowledgeService 介面，下半從 Wiki bundle 拉虛線到需要完成的映射工作。右下小圖表示應用程式 image 與 knowledge release 分開更新。

**揭露**：先業務流程，再 interface，最後 Wiki 接軌與 release。不要一開始展示所有線條。

**講者稿**：「Teams 的工作還包括對話狀態、問題拆解、工單以及人員接手。KnowledgeService 提供明確的查詢介面與結果格式，所以知識後端可以在這個邊界被評估。Wiki bundle 要接入仍有實際工作：scope 與權限怎麼映射、來源連結怎麼解析、內容怎麼進入可回滾的 release。這些不能靠一個相同的函式名稱就假設已經相容。」

**轉場**：「有了介面邊界之後，選後端就能回到可比較的實驗。」

**來源／素材**：SRC-07、SRC-08、SRC-09。介面省略參數清楚標成摘錄。

**驗收**：不把 frontmatter 自動當作 ACL；不把 `KnowledgeResult` 中內部 excluded 欄位說成完整公開 API；不宣稱目前雲端部署已驗收。

### S18 — 同一組題目的後端取捨

**Timing:** `24:45–26:15` / 90 seconds. **Type:** `MEASURED`.

**本頁目的**：展示選型如何落在測量與維運條件上。

**投影文案**

- 條件：「2026-08-07 · 30 題 · 19 份文件 · 同模型 · top_k=4」
- 左圖：「P50 latency：Hybrid 3.00 s；File Search 5.71 s」
- 右圖：「平均每題成本：Hybrid US$0.001059；File Search US$0.001804」
- 解讀：「此批次的品質代理指標未拉開差距；延遲、成本與維運因素支持當時保留 Hybrid」
- 必見註記：「品質代理指標以來源命中等方式計分；不等同 156 題 L3 答案正確率。30 題中的 ACL 欄位無鑑別力。」

**畫面**：兩張並排、各自單位清楚的水平長條圖，零起點；Hybrid 使用主 accent，File Search 使用中性灰。不把不同單位堆在同一條量尺上。

**揭露**：先共同條件，再延遲，接著成本，最後結論。品質 100% 不製作巨大宣傳數字。

**講者稿**：「這是另一個較早的後端 A/B：同一模型、同一組 30 題、19 份文件。P50 與平均每題成本在這批次都偏向 Hybrid，因此報告維持當時選擇。這裡的品質指標主要反映來源命中等代理判準，不能和前面的 L3 答案評分拼成改善曲線。選型結論也只適用於這次條件，語料或需求改變後要重跑。」

**轉場**：「外部知識平台則讓我們進一步思考，哪些能力值得自己維護。」

**來源／素材**：SRC-02；完整表與限制見 A04。

**驗收**：精確數值與單位不變；不宣稱後端普遍優劣；不得忽略報告另有合成 ACL 探測。

### S19 — WeKnora 與企業流程的分工

**Timing:** `26:15–27:15` / 60 seconds. **Type:** `EXTERNAL` + `PROPOSED`.

**本頁目的**：提供外部參照，清楚界定值得評估的替代範圍。

**投影文案**

- 外部參照：「WeKnora 官方定位涵蓋 RAG、Agent 與 Wiki」
- 平台候選責任：「文件處理、知識組織、檢索與相關操作能力」
- 企業需定義的責任：「身分對接、服務目錄、工單規則、人工接手」
- 接入前比較項：「API 契約／ACL 語義／引用／同步與回滾／延遲與成本」
- 頁底：「目前為外部候選；本簡報沒有 WeKnora 整合或成效實測」

**畫面**：兩個平面責任區，上方為企業流程，下方為知識平台候選，中間有 interface 邊界。旁邊只放 WeKnora 名稱及官方來源，不用 GitHub star 數或未驗證功能打勾矩陣。

**揭露**：先官方定位，再企業責任，最後接入檢查項。

**講者稿**：「WeKnora 是一個外部參照，官方文件把 RAG、Agent 與 Wiki 放在同一知識平台裡。對企業來說，評估重點是它能否在既有介面下，滿足引用、權限、同步與維運需求。服務目錄和工單政策仍需要企業自己定義。這裡是在提出評估邊界，沒有把它描述成已接入的後端。」

**轉場**：「最後用已知、未知與下一次實驗收束這段架構演進。」

**來源／素材**：SRC-10；官方描述查閱日為 2026-09-27。

**驗收**：不宣稱與 KnowledgeService 即插即用；不把平台功能清單當效能或權限驗證結果。

### S20 — 已知結果與下一次驗證

**Timing:** `27:15–28:00` / 45 seconds. **Type:** `SYNTHESIS`.

**本頁目的**：讓觀眾清楚帶走方法與證據範圍。

**投影文案**

| 已有依據 | 下一次要回答 |
|---|---|
| 固定資料集上的檢索與答案量測 | 不同知識表示是否在同條件下改善回答？ |
| Wiki 的來源、連結與治理規約 | 知識更新能否完整追蹤到相關頁面與 serving release？ |
| KnowledgeService 介面與後端 A/B | Wiki 接軌及群組權限是否符合真實服務情境？ |

結語：「可靠的企業問答，需要一路追到答案背後的來源與維護責任。」

**畫面**：回到 S03 的責任地圖，左側用短句列已知、右側列下一步。深色底只保留一個結論焦點。來源索引入口放頁腳；不新增結尾第 21 頁。

**揭露**：直接顯示完整畫面；結語可在最後輕度高亮。

**講者稿**：「這次分享有實測的問答結果，也有 Wiki 的維護設計與可接軌的服務邊界。接下來要驗證的是，不同知識表示在固定條件下是否改善回答，以及內容更新與權限是否能完整走進真實服務。當答案出錯時，沿著來源、證據與回答往回查，會讓下一個工程決策更有依據。謝謝。」

**來源／素材**：綜合 SRC-01–SRC-10；後續實驗詳 A05。

**驗收**：不新增無來源 ROI、節省人力或上線保證；保留 2 分鐘給超時緩衝與現場提問。

## 5. 技術附錄規格

附錄 A01–A05 在閱讀模式完整可見，簡報模式預設於 S20 結束。講者可用總覽或明確連結跳轉；附錄顯示 `A01/05`，不得計入主頁 `01/20`。

### A01 — 評測指標、分母與版本

**Purpose:** 解釋統計範圍，支援「99% 是什麼意思」的問答。**Suggested narration:** 90–120 seconds when selected.

**投影內容**

| Metric | Value | Interpretation |
|---|---:|---|
| Case count | 156 | 全部 test cases |
| Evidence-labeled cases | 116 | 證據標註子集 |
| Document Hit@4 | 99.14% | 115/116，由報告比例與分母換算 |
| Answer Accuracy | 96.79% | 151/156，由報告比例與分母換算 |
| Multi-turn Answer Accuracy | 90% | 18/20 |
| Citation Precision | 98.82% | 報告彙總值，不能直接當引用筆數比例 |
| ACL leakage count | 0 | 語料沒有 group-gated documents，涵蓋不足 |

表下顯示 `commit bdd3894`、`release-4f49088db9ca`、`freezeVersion 5`、`test split` 與完成日期。完整 dataset hash 與模型 metadata 放閱讀模式的來源詳情。

**講者稿**：「不同指標回答不同問題。文件命中檢查能否取回目標，答案正確率檢查評測中的答案條件，引用精確率有自己的彙總定義。這些數字屬同一固定快照，不能自動推廣到其他模型、語料或使用者群組。」

**畫面與行為**：單一清楚表格，不縮到不可讀。若 1280×720 顯示不下，將完整 provenance 放閱讀區，投影表仍保留所有七列。

**Source:** SRC-01。**Acceptance:** 所有指標從相同報告取得；原始 `recallAt4` 不誤標為 `documentHitAt4`；不推導未確認的 confidence interval。

### A02 — 失敗分類與證據流失診斷

**Purpose:** 說明報告中不同診斷欄位的關係。**Suggested narration:** 90 seconds.

**投影內容**

左表「Failure taxonomy」：

| Category | Count |
|---|---:|
| ANSWER_OMISSION | 5 |
| BAD_CITATION | 3 |

右表「Evidence drop diagnostics」：

| Stage | Count |
|---|---:|
| GENERATION_IGNORED | 12 |
| CANDIDATE_MISS | 1 |
| SELECTION_OR_PACKING_DROP | 1 |

下方兩列單案：

| Case | Candidate recall | Retrieval evidence recall | Answer evidence recall | Citation precision |
|---|---:|---:|---:|---:|
| v3-blind-ans-05 | 1.0 | 1.0 | 0.0 | 1.0 |
| v3-blind-ans-23 | 1.0 | 1.0 | 1.0 | 0.0 |

必見結論：「分類軸不同，計數不能合併；回到個案判斷下一步。」

**講者稿**：「左邊描述失敗類型，右邊描述證據在哪個階段沒被使用，兩邊不是互斥的同一份分類。第一筆案例主要是答案遺漏，第二筆答案涵蓋了目標但引用精確率為零。因此兩種情況需要不同的調查與回歸測試。」

**畫面與行為**：兩張診斷表上半並排，下半為 case table；無動畫，適合現場直接跳入。

**Source:** SRC-01。**Acceptance:** 不推斷 12 個 GENERATION_IGNORED 等於 12 題 Answer Accuracy 失敗；不包含內部問題及答案全文。

### A03 — 合成知識頁與欄位責任

**Purpose:** 讓工程師看見可落地的資料表示。**Suggested narration:** 120 seconds.

**投影內容**：選取以下完整教學頁的來源、狀態、責任三段，旁邊標示「OKF 欄位」與「本倉治理擴充」。完整內容在閱讀模式展開。

```markdown
---
type: concept
title: ExampleVPN device enrollment
description: Enrollment conditions for the fictional ExampleVPN demo
tags: [demo, remote-access]
sources:
  - id: guide
    resource: ../sources/examplevpn-guide-v2.md
    title: ExampleVPN demonstration guide v2.0
generated:
  by: process:presentation-demo
  at: "2026-09-27T00:00:00Z"
status: draft
stale_after: "2026-12-01"
classification: public
owner: team:demo-it
access_scope: public
contains_pii: false
retention: permanent
redaction: none
---

# ExampleVPN device enrollment

## Summary

This page describes a fictional teaching example, not an operational procedure.

## Key Points

- For a managed demo laptop running ExampleVPN 4.x, DEMO-101 indicates
  incomplete device enrollment. The demo service desk checks the enrollment
  record. The guide does not prescribe reinstalling the client.[^guide]
- Without the error message and device context, this guide cannot establish
  the cause of the login failure.[^guide]

## Evidence

- [Demonstration source](../sources/examplevpn-guide-v2.md)

## Relationships

- related_to: [ExampleVPN 4.x](../entities/examplevpn-client.md)

## Open Questions

- No real product behavior or integration result is represented by this demo.

[^guide]: ExampleVPN demonstration guide v2.0, fictional scope and procedure.
```

這是 `DEMO-01` 的自足教學定義。`generated.at` 是固定示範 metadata，不作真實執行紀錄；未填 `verified`，因為不能虛構人工確認。相對連結代表預定 demo bundle 結構，交付 HTML 時要連到對應教學內容的內部 anchor，不得成為不存在的本機路徑。

**講者稿**：「資料表示的重點是讓主張能回到來源，讓維護者知道狀態與責任。generated 記錄產生者，owner 記錄內容責任；兩者可能不同。verified 只有真的有人查核才填。本頁採用範本欄位，但內容完全是教學資料。」

**Source:** SRC-06、SRC-11、DEMO-01。**Acceptance:** 完整 schema 與畫面摘錄一致；source 頁需另依來源頁版型建立，不能以這個 concept 模板冒充 source schema。

### A04 — 後端 A/B 的方法與限制

**Purpose:** 支援延遲、成本、ACL 與圖像來源的深入提問。**Suggested narration:** 120 seconds.

**投影內容**：使用 §3.3 的六列比較表，加上以下條件：

- 30 題中有 25 題預期找到資料、5 題預期查無資料；錯誤碼、ACL 與圖片案例是交疊標籤。
- 19 份文件、同模型、top_k=4；測量時間 `2026-08-07T03:20:43Z`。
- 報告的 Answer Accuracy 以目標來源命中判定。
- 30 題內的兩個 ACL 案例皆預期命中，無法驗證拒絕授權。
- 另有兩份合成文件的專用 ACL 探測，報告記錄四項檢查通過；不代表現有全部語料的群組治理已完成。

**閱讀模式追加說明**：File Search 的圖片 registry 在此報告已接線，不能重複宣稱完全不支援圖片；報告描述的是文件層級對應，相較 Hybrid 的 chunk 層級定位仍有粒度差別。上傳重試可能產生重複文件是當時紀錄的維運注意項，現況需重新確認。

**講者稿**：「小語料很容易碰到指標天花板，所以我們更關心可比較的延遲、成本與操作負擔。權限測試尤其要看題目是否真的包含拒絕案例。這個報告有補做合成 ACL 探測，但不能因此把主資料集的 ACL 欄位當作有效比較。」

**Source:** SRC-02。**Acceptance:** 不將交疊標籤相加為總題數；歷史成本不當作目前供應商報價；不把此批次的效能差異歸因成已證實的服務內部原因。

### A05 — Wiki 接軌與效益驗證設計

**Purpose:** 給出明確、可執行的下一次驗證，而不虛構成果。**Suggested narration:** 120 seconds.

**投影內容**

| 驗證面向 | 做法 | 需要觀察的結果 |
|---|---|---|
| 知識表示 | 相同來源內容分別使用 canonical 與 Wiki 表示，固定模型、題目與檢索設定 | 答案正確、引用、缺答與成本差異 |
| 條件與版本 | 加入相似問題、不同版本、資訊缺失與過期來源 | 適用性判斷與追問是否正確 |
| 授權 | 建立真實的允許與拒絕矩陣 | 檢索、回答、引用和附件皆符合權限 |
| 更新與回滾 | 新來源 → 相關頁更新 → 發布 → serving → 回滾 | 來源、版本與 release 可一致追查 |

**實驗約束**：baseline 與 candidate 必須保留相同可用事實；若候選新增了內容，須另標為內容補強實驗。固定測試集後不以測試答案修改候選知識；保留獨立 holdout。預先定義重要改善及可接受退步，使用配對案例、重複執行與區間估計，不預填「提升 X%」目標。

**講者稿**：「要知道 Wiki 是否有效，先把內容量與模型設定控制住。若 Wiki 版本額外補了原本不存在的事實，就無法把改善全歸因於表示方式。除了答對多少，我們還要看過期內容、權限拒絕與更新回滾。這些共同決定知識能不能穩定進入服務。」

**Source:** 本 spec 提議的實驗設計；接口與 release 責任參照 SRC-07、SRC-09。

**Acceptance:** 頁面清楚標「待執行的驗證設計」；不把未執行的測試寫成通過；沒有需要真實秘密或使用者資料的演示步驟。

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

### 6.3 頁型分配

| Layout | Slides | Main visual object |
|---|---|---|
| Cover / closing | S01, S20 | 標題＋文件關係局部／責任地圖 |
| Question annotation | S02 | 提問與未知條件 |
| Architecture / flow | S03, S04, S11, S15, S17 | 泳道、主路徑、介面與審查位置 |
| Decision / responsibility table | S05, S09, S19 | 條件對應動作、工程責任、平台分工 |
| Evidence / chart | S06, S07, S08, S18 | 分母、比率、case trace、同條件 A/B |
| Document / schema | S10, S12, S13 | 知識頁、三層產物、欄位責任 |
| Relationship map | S14 | 四個可讀知識節點 |
| Answer trace | S16 | 對話、適用條件與來源 |

同頁只使用一個主要構圖。圖表、比較表和架構圖需保持可編輯；不要將文字與資料全部烘焙成圖片。前後頁可重用同一張系統地圖以保持方向感，但必須明確放大不同責任。

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

主簡報預設不依賴 live demo。S16 已提供離線、完整、可驗證的劇本。若未來加入實機畫面，仍需保留靜態備援，並標示錄製日期與環境。

### 6.6 素材策略

- 現有兩張生成圖片可作封面視覺候選；須經整體風格檢查，不能因已存在就強制沿用。
- 核心素材由證據圖表、教學文件、schema、架構與回答路徑構成。
- 真實產品截圖只有在確有可公開內容且能支持該頁時採用；沒有截圖時使用明確標為示意的文字或流程。
- 圖中說明皆為繁體中文；程式碼與 metadata identifiers 用英文。
- 不下載、嵌入或散布內部分類的來源原文、操作畫面或可還原內容。
- 技術圖若用 SVG 實作，文字、節點、連線仍應可維護；裝飾性插畫另用合適素材，不以程式畫假產品截圖。
- 大型內嵌圖片使用正常 image element 或可驗證的資產載入方式；不得再依賴會被瀏覽器忽略的超長 CSS custom property。

## 7. 來源登錄與主張對應

### 7.1 查閱快照

以下是內容規格查閱時的版本，不代表演講當日的部署狀態。

| Repository | Inspected HEAD | Scope |
|---|---|---|
| teams-agent | `2601aac3b22c6a4001b6bb682ecef6fb4bc5d652` | 所列來源檔查閱時沒有未提交變更；未在本任務執行專案測試或部署驗收 |
| llm-wiki-example | `0c02fd346e9711d8b556cc2b94c841a2185ac77e` | 所列 README、規約與模板查閱時沒有未提交變更；不代表 Wiki 串接或成效已驗證 |

### 7.2 Source registry

| Source ID | Source | Supports | Boundary |
|---|---|---|---|
| SRC-01 | [Frozen L3 report](../teams-agent/data/eval/reports/rag-l3-v3-blind-full-live-20260923-bdd3894.json) | S06–S09, A01–A02 的實測值與 case 診斷 | 歷史指定快照；不是 Wiki 前後實驗 |
| SRC-02 | [Retrieval A/B report](../teams-agent/docs/retrieval-ab-test-report.md) | S18, A04 的測量與方法 | 小語料、代理品質指標、歷史價格與設定 |
| SRC-03 | [LLM Wiki README](../llm-wiki-example/README.md) | 範本定位、三層產物、目錄與整體管線 | 範本文件不證明所有採用者的 runtime 行為 |
| SRC-04 | [Ingest pipeline](../llm-wiki-example/docs/ingest-pipeline.md) | 准入、兩段分析、來源頁、review、log | 文件規約；未在此任務重跑 ingest |
| SRC-05 | [Data governance](../llm-wiki-example/docs/data-governance.md) | 治理欄位、來源 approval、產物 lineage、權限邊界 | 與實際 serving ACL 是不同責任 |
| SRC-06 | [Wiki rules](../llm-wiki-example/AGENTS.md), [Source template](../llm-wiki-example/docs/templates/page-template-source.md), [Concept template](../llm-wiki-example/docs/templates/page-template-concept.md) | 頁面 schema、引用與連結 | 治理擴充不可全部稱 OKF 必填欄位 |
| SRC-07 | [KnowledgeService](../teams-agent/agent_service/src/agent_service/knowledge.py), [Contracts](../teams-agent/agent_service/src/agent_service/contracts.py) | 介面與結果欄位 | 不證明 Wiki adapter 已完成 |
| SRC-08 | [Workflow graph](../teams-agent/agent_service/src/agent_service/workflow_subgraphs.py) | Teams 業務流程節點及旁路 | 不代表所有分支都經過同一條 path |
| SRC-09 | [Knowledge release operations](../teams-agent/docs/knowledge-release-operations.md) | 應用與知識 release 分離、manifest、active pointer、回滾契約 | 文件可證明契約，雲端狀態需另驗 |
| SRC-10 | [Tencent/WeKnora official repository](https://github.com/Tencent/WeKnora) | S19 外部定位，查閱 2026-09-27 | 只描述官方定位；不形成效能比較 |
| SRC-11 | [OKF specification](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md), [Local OKF mapping](../llm-wiki-example/docs/okf.md) | 該範本採用的 v0.2 與本倉擴充區分 | 不稱全球最新版本；上游 main 可變 |
| SRC-12 | [Current HTML](./index.html) | 舊版頁面與功能遷移 | 舊簡報不作技術主張的獨立來源 |
| SRC-13 | [Hybrid service](../teams-agent/agent_service/src/agent_service/knowledge_hybrid.py), [Retrieval stage](../teams-agent/agent_service/src/agent_service/knowledge_pipeline/retrieval_stage.py), [Search stage](../teams-agent/agent_service/src/agent_service/knowledge_pipeline/search_stage.py), [RAG implementation specification](../teams-agent/docs/agentic-rag-production-optimization-implementation-spec-20260921.md) | S04 的受限查詢管線與角色分層 | 投影使用概念化流程，不冒充完整呼叫圖 |

相對本機來源連結供規格審閱使用。最終分享版不能依賴這些本機路徑。已確認可公開的程式碼與報告以對應 repository 的永久 commit link 引用；其他來源只保留可公開書目與教學內容，不複製內部資料。

### 7.3 引用配置

- 投影頁：有數據時顯示來源短名、日期及關鍵測量範圍。
- 講者筆記：來源 URL／檔案、section／field、版本、主張類型與必要限制。
- 閱讀模式：每個 `[D1]` 和 source marker 可以跳到資料來源或完整示範定義。
- 外部來源更新不能默默改變歷史測量。採用新報告時，需同步更改所有分母、圖表、筆記與附錄。
- 現場口述不必讀出 commit/hash，但不能把歷史快照稱為目前線上表現。

## 8. 素材清單與交付狀態

以下素材皆已有確定內容或可在此 spec 內完整建構；不以未取得的內部素材作為改版前提。

| Asset ID | Slides | Definition | Status |
|---|---|---|---|
| ASSET-01 | S01, S03, S20 | 系統責任總圖與局部 | Specified; implementation pending |
| ASSET-02 | S02, S05, S16 | DEMO-01 對話與已知條件 | Fully authored in §3.1 |
| ASSET-03 | S04 | 受預算限制的查詢流程 | Specified; source available |
| ASSET-04 | S06, S07, A01 | 156 題資料組成與兩種分母 | Values verified from SRC-01 |
| ASSET-05 | S08, A02 | case 診斷追蹤 | IDs and diagnostic values verified |
| ASSET-06 | S10, S12 | 教學文件三層對照 | Fully specified; not a runtime screenshot |
| ASSET-07 | S11, S15 | Ingest 與兩種審查流程 | Source-backed; drawing pending |
| ASSET-08 | S13, A03 | schema 節錄與完整合成頁 | Fully authored |
| ASSET-09 | S14 | 四節點知識關係圖 | Fully specified |
| ASSET-10 | S17 | Workflow、interface、release 接軌圖 | Source-backed with proposed edge marked |
| ASSET-11 | S18, A04 | A/B latency 與 cost 圖表 | Values verified from SRC-02 |
| ASSET-12 | S19 | 企業與知識平台責任分工 | Specified; no integration claim |

可選升級為真實案例時，必須同時取得可公開的來源片段、query、回答、引用及執行環境。只有截圖而沒有上下文，不足以取代 DEMO-01。拿不到可公開執行紀錄時，維持本 spec 的教學案例，完整度仍成立。

## 9. 舊版頁面到新版的遷移

| Old slide | New destination | Content change |
|---:|---|---|
| 1 | S01 | 正式題目保留，改用可讀內容關係建立封面 |
| 2 | S02 | 四選一改為明確的未知條件 |
| 3 | S05 | 根因猜測改為資訊條件與下一步 |
| 4 | S04 | 擴充成有條件分支與預算邊界的查詢流程 |
| 5 | S07 | 加入評測前置 S06，清楚顯示分母 |
| 6 | S08–S09 | 加入真實 case 診斷；拆開失敗類別與工程動機 |
| 7 | S10 | 轉折大字改為可操作的知識單位定義 |
| 8 | S12 | 以同一教學文件對照三層產物 |
| 9 | S13 | 修正完整欄位語義，另提供 A03 |
| 10 | S11, S15 | 管線與審查分開說清楚 |
| 11 | S16 | 完整對話與來源支持對照 |
| 12 | S17 | 明確 interface 與接軌工作 |
| 13 | S18 | 補齊小樣本與代理計分限制 |
| 14 | S19 | 官方定位與接入條件，移除空泛名詞展示 |
| 15 | S17, S19 | 分工落在接口、資料映射與選型條件 |
| 16 | S09, S20 | 檢查方法放進診斷與收束 |
| 17 | S20 | 結語連到已知證據與下一次驗證 |

舊數字 hash 的相容跳轉採用上表第一個新目的頁。例如 `#6 → #s08`、`#10 → #s11`；新連結一律使用明確 `s`／`a` 前綴。

## 10. 驗收標準

### 10.1 內容

- [ ] 20 頁主簡報及 5 頁附錄皆存在，順序與本 spec 一致。
- [ ] 每頁具備完整投影文案、講者筆記、來源及主張類型。
- [ ] 主簡報預計講述時間相加為 28 分鐘，保留 2 分鐘緩衝。
- [ ] S02、S05、S10、S12–S14、S16、A03 的同一教學案例值一致。
- [ ] 合成案例未偽裝成內部工單、真實模型輸出或實測結果。
- [ ] EVAL-L3-01 與 AB-01 的資料集、分母及評分定義不混用。
- [ ] 圖片與主張沒有敏感原始資料；最終分享來源不依賴本機絕對路徑。
- [ ] 本文與講者稿沒有「Wiki 已提升準確率」「WeKnora 已接入」「正式雲端驗收完成」等無依據敘述。
- [ ] 讀者不看講者筆記也能看見影響結論的限制。
- [ ] 沒有空白頁、示意用 lorem ipsum 或未替換的模板文字。

### 10.2 視覺與閱讀

- [ ] 1920×1080、1600×900、1280×720 都檢查文字、圖表和控制列。
- [ ] 390×844 的閱讀模式正文可讀，頁面無不必要水平溢出。
- [ ] 每頁主要結論與證據在第一視覺層級；相同版型不連續重複超過三頁。
- [ ] 資料圖從正確零點／尺度開始；標籤、分母、單位與數據一致。
- [ ] 線條方向、圖例與節點語義一致；虛線代表設計或未驗證路徑。
- [ ] 所有素材實際載入；檢查封面、深色頁及大型內嵌圖片。
- [ ] 配色對比與中文斷行可讀，關鍵限制不以極小字隱藏。
- [ ] 字體 fallback 後不遮住圖表或截斷正式題目。

### 10.3 功能與分享

- [ ] 前進、後退、子步驟、總覽、筆記與全螢幕可使用。
- [ ] 深連結刷新後能回到正確頁；錯誤 hash 安全回封面。
- [ ] 附錄跳轉與返回主頁不影響主簡報頁數。
- [ ] reduced-motion 下沒有遺失內容。
- [ ] 離線單檔的圖片、正文、圖表與操作不依賴網路。
- [ ] 列印與閱讀模式呈現完整內容，不只顯示動畫第一步。
- [ ] 最終檔沒有未捕捉 JavaScript 錯誤或不存在的內部連結。

### 10.4 口述排練

- [ ] 以 28 分鐘講稿實際排練一次，記錄每頁時間；不只依字數估算。
- [ ] 在 S08 能解釋「證據存在但答案遺漏」而不越過報告支持範圍。
- [ ] 在 S12 能清楚區分 canonical 與 Wiki 摘要。
- [ ] 在 S15 能清楚區分來源准入、內容 review 與 runtime publication。
- [ ] 在 S16 能以一分鐘說清楚條件、來源與回答的連結，並保留示範標示。
- [ ] 在 S18 能解釋 30 題與 156 題報告為何不能直接比較準確率。

## 11. 實作順序與完成定義

1. 以本 spec 凍結頁面順序、文案與資料來源，先確認主張及教學案例一致。
2. 建立四種代表頁：S07 數據、S12 文件對照、S16 回答追蹤、S17 整合架構；確認資訊密度及閱讀距離。
3. 套用設計 token 完成其餘頁面，沿用相同節點與案例名稱。
4. 加入講者筆記、閱讀模式、來源跳轉及五頁附錄。
5. 完成功能、視覺與離線檢查，再進行一次計時排練。
6. 交付可離線開啟的 HTML、可編輯素材與來源索引；不自動部署或公開發布。

「完成」表示內容、證據與操作功能都符合本 spec，且經過視覺檢查與計時排練。技術系統的正式上線狀態、Wiki 效益實驗與外部平台整合，仍以各自的工程證據判定，不因簡報完成而改變。
