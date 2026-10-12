# v2 合成實驗證據入口

這是一次隔離的合成教學演練，不是正式 Wiki 匯入、線上檢索或發布驗收。基準與更新階段各產生十一則新回答；v2 使用凍結的十一題契約，不能與 v1 十題的 8／10 分數直接比較。

## 從哪裡查

1. [凍結的十一題契約](../contracts/regression-cases-v2.json)：題目、情境、兩階段預期與逐項規則。SHA-256：`fb33ef8439a87f840bc2c690d80c2856625f963e4c8f08f47c3c0b8a5356b443`。
2. [22 則使用者可見回答](actual-answers-v2.md)：依階段與題號閱讀；這些是保存的模型輸出，不是參考答案。
3. [逐題與逐項判定](regression-results-v2.json)：路由、第一動作、內容條件、禁止事項及指定來源與引用片段檢查。
4. [執行摘要與限制](experiment-summary-v2.md)：10／11、9／11 的計算方式、三個未通過的階段／題目組合與尚未完成的驗收。
5. [v1 規則覆核與 v2 修訂理由](../contracts/V2_RUBRIC_REVIEW.md)：說明 SYN-07 舊規則與 Model Judge 覆核事件，以及新增 SYN-11 的原因。

契約內的 `execution_status: not-run` 保留了凍結當下的狀態；執行後的結果另存於逐題判定。兩階段使用的知識草稿分別保存在 [Baseline 快照](../baseline-v1/) 與 [Updated 快照](../updated-v2/)。

## 十一題結果

| 題號 | Baseline | Updated | 可核對的重點 |
| --- | --- | --- | --- |
| SYN-01 | PASS | FAIL | 更新後第一步正確，但回答正文未列出三項資格與 2030-03-01 生效門檻。 |
| SYN-02 | PASS | PASS | 承包人員維持服務台路徑。 |
| SYN-03 | PASS | PASS | 未註冊自助復原者維持服務台路徑。 |
| SYN-04 | PASS | PASS | 歷史事件維持當時的服務台基準。 |
| SYN-05 | PASS | PASS | DEMO-101 資訊不足時先釐清。 |
| SYN-06 | FAIL | FAIL | 兩階段回答都未明說無法連公司網路時的服務台退路。 |
| SYN-07 | PASS | PASS | Branch 遠端路徑限制。 |
| SYN-08 | PASS | PASS | 資源情境未知時先追問。 |
| SYN-09 | PASS | PASS | 海外申請補齊日期與核准。 |
| SYN-10 | PASS | PASS | 未記載錯誤碼不擅自推斷。 |
| SYN-11 | PASS | PASS | HQ 公司網路與 Branch 遠端路徑比較是獨立題目。 |

## 原始模型紀錄

| 階段 | 回答請求與結果 | 評審請求與結果 |
| --- | --- | --- |
| Baseline | [提示詞](model-runs-v2/baseline-query/prompt.txt) · [原始回答 JSON](model-runs-v2/baseline-query/response.json) · [收據](model-runs-v2/baseline-query/receipt.json) | [提示詞](model-runs-v2/baseline-judge/prompt.txt) · [逐項評審 JSON](model-runs-v2/baseline-judge/response.json) · [收據](model-runs-v2/baseline-judge/receipt.json) |
| Updated | [提示詞](model-runs-v2/updated-query/prompt.txt) · [原始回答 JSON](model-runs-v2/updated-query/response.json) · [收據](model-runs-v2/updated-query/receipt.json) | [提示詞](model-runs-v2/updated-judge/prompt.txt) · [逐項評審 JSON](model-runs-v2/updated-judge/response.json) · [收據](model-runs-v2/updated-judge/receipt.json) |

每個執行目錄另保存輸入、輸出 schema 與事件紀錄。收據中的本機絕對路徑為公開版改成倉庫相對路徑；提示詞、schema、回答的 SHA-256 與執行設定未更動。本機 shell 診斷訊息未公開，且不參與判分。

兩階段共 22 題的路由與第一動作檢查均通過；指定來源 ID、來源路徑、摘錄與正文引用檢查也均通過。這些檢查不能代替回答正文的完整性判定，因此 SYN-01 與 SYN-06 仍依契約未通過。人工內容負責人審查仍待辦，知識草稿未發布。
