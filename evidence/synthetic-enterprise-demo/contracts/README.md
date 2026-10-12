# v1 十題測試契約

這份契約使用合成教學來源，包含十題固定問題、結構化情境、基準／更新後預期、必要引用、必須保留的內容與禁止推論。參考答案是驗收標準，不是模型實際輸出；契約建立時尚未執行；現已完成兩階段實際回答，結果見 [實驗紀錄](../records/experiment-summary.md)。JSON 的原始 `execution_status: not-run` 是建立時狀態，契約本身未改寫；目前狀態以另存結果為準。

v2 十一題契約與重新執行的結果見 [v2 證據入口](../records/v2-evidence-index.md)。兩版題數、規則與實際回答不同，分數不能直接比較。

- [完整 JSON 契約](regression-cases.json)
- 基準：`SRC-01` 至 `SRC-06`，情境日期 `2030-02-01`。
- 更新後：加入 `SRC-07`，情境日期 `2030-03-02`；已另完成更新草稿與同題回歸，原始預期保持凍結。
- `context` 中的 `null` 表示未知，不能推定為符合資格。`event_date: null` 則使用該階段情境日期。
- 歷史事件使用事件當時生效的政策；不能因回答當日較晚而套用後來規則。

## 題目與分支

| ID | 問題 | 基準預期 | 更新後預期 |
|---|---|---|---|
| `SYN-01` | 我是全職員工，使用公司管理筆電，已註冊自助復原，現在明確顯示帳戶鎖定，應該怎麼處理？ | `ANSWER` / `SERVICE_DESK_REQUEST` | `ANSWER` / `SELF_SERVICE_RECOVERY` |
| `SYN-02` | 我是承包人員，使用公司管理筆電，也有註冊自助復原，帳戶已確認鎖定，可以使用同樣流程嗎？ | `ANSWER` / `SERVICE_DESK_REQUEST` | `ANSWER` / `SERVICE_DESK_REQUEST` |
| `SYN-03` | 我是全職員工，筆電受公司管理，但尚未註冊自助復原；帳戶已確認鎖定，該怎麼辦？ | `ANSWER` / `SERVICE_DESK_REQUEST` | `ANSWER` / `SERVICE_DESK_REQUEST` |
| `SYN-04` | 請說明我在 2030-01-20 帳戶已確認鎖定時應採用的處理流程。我是全職員工，用公司管理筆電，已註冊自助復原。 | `ANSWER` / `SERVICE_DESK_REQUEST` | `ANSWER` / `SERVICE_DESK_REQUEST` |
| `SYN-05` | ExampleVPN 出現 DEMO-101，是帳號被鎖嗎？ | `CLARIFY` / `ASK_ACCOUNT_STATE` | `CLARIFY` / `ASK_ACCOUNT_STATE` |
| `SYN-06` | 公司管理筆電提示密碼已到期，我目前可連公司網路，ExampleVPN 登入失敗，怎麼更新密碼？ | `ANSWER` / `CHANGE_PASSWORD_ON_COMPANY_NETWORK` | `ANSWER` / `CHANGE_PASSWORD_ON_COMPANY_NETWORK` |
| `SYN-07` | 我是 Branch Support，已透過 ExampleVPN 遠端連線，想用 TeamShare，可以直接申請資料夾權限嗎？ | `ANSWER` / `EXPLAIN_RESOURCE_RESTRICTION` | `ANSWER` / `EXPLAIN_RESOURCE_RESTRICTION` |
| `SYN-08` | 我想使用 TeamShare，可以幫我申請嗎？ | `CLARIFY` / `ASK_RESOURCE_CONTEXT` | `CLARIFY` / `ASK_RESOURCE_CONTEXT` |
| `SYN-09` | 我要到 Example Region 出差辦理教學專案，需要海外連線，但還沒有確定起訖日期，也尚未送主管核准，接下來怎麼辦？ | `CLARIFY` / `COMPLETE_OVERSEAS_APPLICATION` | `CLARIFY` / `COMPLETE_OVERSEAS_APPLICATION` |
| `SYN-10` | ExampleVPN 出現 DEMO-999，這是什麼原因、要怎麼修？ | `NO_ANSWER` / `ACKNOWLEDGE_UNDOCUMENTED_ERROR` | `NO_ANSWER` / `ACKNOWLEDGE_UNDOCUMENTED_ERROR` |

## 判讀方式

每題必須檢查 route、第一步、全部 `must_include`、未違反任何 `must_not`、引用及追問欄位。只有取得實際回答且逐項保存審查判定後，才可標示該題 PASS；頁面存在、引用標題相符或結構 lint 通過都不能代替答案正確性。

- `ANSWER`：來源足以支持有界的回答；不代表執行了操作。
- `CLARIFY`：必須先補齊情境；可交代已知限制，但不得推定分支。
- `NO_ANSWER`：這份來源未記載原因，仍可說明如何提供非機密資訊並轉服務台。

本輪 `SYN-01` 是預期變動的正向案例；其餘題目用來守住不該改變的分支、歷史情境、未知與禁止推論。這十題不是完整覆蓋：尚未另設個人裝置、日期未知、自助失敗、公司網路不可用、審批拒絕及 DEMO-303 的獨立題目；相關邊界仍須保留在知識頁中。

## 執行結果欄位

未來每次執行至少保存 `run_id`、phase、來源 digest、情境日期、模型與提示詞版本、題目 ID、實際回答、實際 route／引用、各條判定、審查者與時間。模型、tokens、成本未取得時記為 `null` 或 `not-measured`，不得填成零。產生答案與評判答案的方式也必須明確記錄。
