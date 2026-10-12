# v2 actual answers

Synthetic teaching run. These are the saved model answers, not reference answers or live llm-wiki service output.

## Baseline

### SYN-01 — Eligible confirmed lock

**Question:** 我是全職員工，使用公司管理筆電，已註冊自助復原，現在明確顯示帳戶鎖定，應該怎麼處理？

**Route:** `ANSWER` · **First action:** `SUBMIT_EXAMPLEDESK_RECOVERY_REQUEST` · **Missing fields:** `none`

依本合成資料截至 2030-02-01 的基準，請透過 ExampleDesk 提交帳戶復原請求，由 Example IT Service Desk 檢視。已註冊自助復原並不構成本資料另有自助解鎖流程的證據。[SRC-03] 請附識別與聯絡資訊、非機密完整錯訊及發生時間，並記錄已提供的公司管理筆電、已註冊自助復原及已確認鎖定狀態；不要附密碼、驗證碼或復原連結。提交不代表已解鎖，也不保證直接解除或特定處理時間；本回答未執行復原操作。[SRC-03]

**Cited sources:** SRC-03

### SYN-02 — Contractor confirmed lock

**Question:** 我是承包人員，使用公司管理筆電，也有註冊自助復原，帳戶已確認鎖定，可以使用同樣流程嗎？

**Route:** `ANSWER` · **First action:** `SUBMIT_EXAMPLEDESK_RECOVERY_REQUEST` · **Missing fields:** `none`

可以。此基準明確適用於全職員工與承包人員的已確認帳戶鎖定情境，因此請透過 ExampleDesk 提交帳戶復原請求，由 Example IT Service Desk 檢視。[SRC-03] 請附識別與聯絡資訊、非機密錯訊及發生時間，並記錄公司管理筆電、已註冊自助復原及已確認鎖定的既有狀態。不得附登入秘密；已註冊自助復原不代表本資料支持另一套解鎖程序。送出請求不代表已解鎖，也沒有直接解除或處理時間的保證。[SRC-03]

**Cited sources:** SRC-03

### SYN-03 — Managed device without recovery enrollment

**Question:** 我是全職員工，筆電受公司管理，但尚未註冊自助復原；帳戶已確認鎖定，該怎麼辦？

**Route:** `ANSWER` · **First action:** `SUBMIT_EXAMPLEDESK_RECOVERY_REQUEST` · **Missing fields:** `none`

請直接依已確認鎖定的基準，透過 ExampleDesk 提交帳戶復原請求。此流程沒有把完成自助復原註冊列為提交前提，因此不需要先註冊才能提出請求。[SRC-03] 附識別與聯絡資訊、非機密錯訊及發生時間，並如實記錄公司管理筆電、自助復原尚未註冊及已確認鎖定。不要提供密碼、驗證碼或復原連結。後續由服務台核實決定，不能保證直接解鎖；目前未執行任何解鎖操作。[SRC-03]

**Cited sources:** SRC-03

### SYN-04 — Historical lock before update

**Question:** 請說明我在 2030-01-20 帳戶已確認鎖定時應採用的處理流程。我是全職員工，用公司管理筆電，已註冊自助復原。

**Route:** `ANSWER` · **First action:** `SUBMIT_EXAMPLEDESK_RECOVERY_REQUEST` · **Missing fields:** `none`

應以事件日 2030-01-20 判斷。該日已在 2030-01-10 生效的鎖定復原基準期間內；本資料沒有收錄適用於該事件的取代規則，因此當時應透過 ExampleDesk 提交帳戶復原請求，由 Example IT Service Desk 檢視。[SRC-03] 請求應附識別與聯絡資訊、當時的非機密錯訊及發生時間，並記錄公司管理筆電、已註冊自助復原及已確認鎖定狀態。已註冊不能據此推導其他復原程序；提交也不代表已解鎖或保證直接解除。不得附密碼、驗證碼或復原連結。[SRC-03]

**Cited sources:** SRC-03

### SYN-05 — Ambiguous login rejection

**Question:** ExampleVPN 出現 DEMO-101，是帳號被鎖嗎？

**Route:** `CLARIFY` · **First action:** `CLARIFY_ACCOUNT_STATE` · **Missing fields:** `account_state, full_error_message, occurrence_time, device_management, company_network_available`

不能只憑 DEMO-101 判定帳戶被鎖。它可能與密碼輸入錯誤、鎖定、密碼到期或網路狀況有關，目前只能保留這些待查方向。[SRC-01][SRC-02] 請確認是否有明確的鎖定或到期通知，並補充不含機密的完整錯訊、發生時間、裝置管理狀態及當時公司網路是否可用；不要提供密碼或驗證碼。確認鎖定後才走帳戶復原請求，確認到期則走獨立的密碼更新程序。[SRC-01]

**Cited sources:** SRC-01, SRC-02

### SYN-06 — Confirmed expiry on managed laptop

**Question:** 公司管理筆電提示密碼已到期，我目前可連公司網路，ExampleVPN 登入失敗，怎麼更新密碼？

**Route:** `ANSWER` · **First action:** `CHANGE_PASSWORD_ON_COMPANY_NETWORK` · **Missing fields:** `none`

你已確認密碼到期、使用公司管理筆電且公司網路可用，符合本合成案例的更新條件。請先連上公司網路，按 Ctrl+Alt+Delete，選擇「變更密碼」，依畫面完成；變更後再依組織核准流程測試登入。[SRC-02] 若操作無法使用，停止自行嘗試並聯絡 Example IT Service Desk。不要用消費者入口網站同步密碼，也不要把帳戶解鎖當成重設或延長到期密碼；勿向支援人員提供密碼。這些步驟只適用本案例，並未替你執行更新。[SRC-02]

**Cited sources:** SRC-02

### SYN-07 — Branch remote resource restriction

**Question:** 我是 Branch Support，已透過 ExampleVPN 遠端連線，想用 TeamShare，可以直接申請資料夾權限嗎？

**Route:** `ANSWER` · **First action:** `RESPECT_REMOTE_ACCESS_RESTRICTION` · **Missing fields:** `none`

不能以一般資料夾權限申請取得此路徑下的 TeamShare 存取。已確認的 Branch Support 加上 ExampleVPN 遠端連線情境，政策範圍包含 ExampleCRM，但不包含 TeamShare；一般申請流程不能覆蓋這項遠端路徑限制，即使要求的角色是 reader 也不能據此開通。[SRC-05] VPN 連線成功只代表有遠端連線，不代表取得 TeamShare 授權。目前未提出申請或開通權限；本資料也沒有記錄可替代此限制的例外程序。[SRC-05]

**Cited sources:** SRC-05

### SYN-08 — Unknown resource scope

**Question:** 我想使用 TeamShare，可以幫我申請嗎？

**Route:** `CLARIFY` · **First action:** `CLARIFY_ACCESS_CONTEXT` · **Missing fields:** `support_group, network_path, requested_role`

請先提供你的群組、目前所在網路或連線路徑，以及需要的 TeamShare 角色；目前應保留未決狀態，不能假定你符合申請條件或替你選擇權限。[SRC-05] 若確認是 HQ Support 且在公司網路，可透過 ExampleDesk 申請，屆時需附使用者識別碼、邏輯資料夾名稱及所需角色。若是 Branch Support 透過 ExampleVPN 遠端連線，該範圍不含 TeamShare，一般申請不能覆蓋限制。此處尚未提交申請，也未授予權限。[SRC-05]

**Cited sources:** SRC-05

### SYN-09 — Incomplete overseas application

**Question:** 我要到 Example Region 出差辦理教學專案，需要海外連線，但還沒有確定起訖日期，也尚未送主管核准，接下來怎麼辦？

**Route:** `CLARIFY` · **First action:** `COMPLETE_OVERSEAS_APPLICATION_DETAILS` · **Missing fields:** `start_date, end_date, remote_work_scope`

請先補上預計開始日與結束日，並具體說明需要遠端連線的工作範圍。你已提供申請人識別碼、Example Region 目的地及教學專案出差目的，這些不需要重填；未知日期不能代填猜測。[SRC-06] 資料齊備後透過 ExampleDesk 提交，先由直屬主管審查。主管核准後才轉交 Network Operations 並納入 Security Review，所有相關審查完成且獲准後才能安排啟用；目前尚未請主管核准，不能先行啟用。[SRC-06] 核准只在申請所列日期範圍有效，到期停止臨時安排，延長須重新申請。成功連上 VPN 也不代表海外存取已獲准；此處未提交、核准或啟用任何安排。[SRC-06]

**Cited sources:** SRC-06

### SYN-10 — Undocumented error

**Question:** ExampleVPN 出現 DEMO-999，這是什麼原因、要怎麼修？

**Route:** `NO_ANSWER` · **First action:** `REFER_UNDOCUMENTED_ERROR_TO_SERVICE_DESK` · **Missing fields:** `none`

這份證據集沒有記錄 DEMO-999 的原因或專屬修復步驟，因此無法據此診斷或提供修法。已記錄的 DEMO-101、DEMO-202、DEMO-303 不能用來推導 DEMO-999 是密碼、網路或裝置授權問題。[SRC-02] 請保存不含機密的完整錯訊與發生情境，交由服務台判讀。這是本證據集的資訊邊界，並非宣稱其他資料來源也沒有相關資訊；目前未執行修復。[SRC-01][SRC-02]

**Cited sources:** SRC-02, SRC-01

### SYN-11 — Compare Branch remote restriction with HQ corporate-network application

**Question:** 我是 HQ Support，在公司網路想使用 TeamShare；這和 Branch Support 透過 ExampleVPN 遠端連線的情況有什麼不同？送出申請就能使用嗎？

**Route:** `ANSWER` · **First action:** `PREPARE_EXAMPLEDESK_ACCESS_REQUEST` · **Missing fields:** `none`

差別在於群組與網路條件：你是 HQ Support 且在公司網路，可以提出 TeamShare 權限申請；Branch Support 透過 ExampleVPN 遠端連線時，政策範圍包含 ExampleCRM，但不包含 TeamShare，一般申請不能覆蓋該限制。[SRC-05] 若要提出你的申請，請透過 ExampleDesk 提供使用者識別碼、邏輯資料夾名称及所需角色；角色或資料夾用途不清楚時先釐清，不自行選擇較高權限。[SRC-05] 送出申請不代表已核准或授權已生效，因此不能只憑送出就認定可以使用。群組名稱與 VPN 連線成功也不是權限核准證明；本回答未提交申請或開通資源。[SRC-05]

**Cited sources:** SRC-05

## Updated

### SYN-01 — Eligible confirmed lock

**Question:** 我是全職員工，使用公司管理筆電，已註冊自助復原，現在明確顯示帳戶鎖定，應該怎麼處理？

**Route:** `ANSWER` · **First action:** `TRY_SELF_SERVICE_RECOVERY` · **Missing fields:** `none`

以本次情境日期 2030-03-02 判斷，你已確認帳戶鎖定，且三項資格皆符合，第一步是嘗試自助復原：https://support.example.com/account-recovery。這是虛構教學入口，沒有實際服務，不能視為已完成復原；結果仍須由你確認。若流程失敗或狀態不明，轉由 Example IT Service Desk 處理。[SRC-07]

**Cited sources:** SRC-07

### SYN-02 — Contractor confirmed lock

**Question:** 我是承包人員，使用公司管理筆電，也有註冊自助復原，帳戶已確認鎖定，可以使用同樣流程嗎？

**Route:** `ANSWER` · **First action:** `SUBMIT_EXAMPLEDESK_REQUEST` · **Missing fields:** `none`

你是承包人員，因此即使使用公司管理筆電且已註冊自助復原，也不適用這次更新的自助第一步；應沿用 ExampleDesk 服務台路徑。[SRC-07] 提交帳戶復原請求時，附識別與聯絡資訊、非機密錯訊、發生時間，以及已知的裝置管理、復原註冊與鎖定狀態。不要附密碼、驗證碼或復原連結。服務台會檢視請求，但提交不代表已解鎖，也不保證直接解除或特定處理時間。[SRC-03]

**Cited sources:** SRC-07, SRC-03

### SYN-03 — Managed device without recovery enrollment

**Question:** 我是全職員工，筆電受公司管理，但尚未註冊自助復原；帳戶已確認鎖定，該怎麼辦？

**Route:** `ANSWER` · **First action:** `SUBMIT_EXAMPLEDESK_REQUEST` · **Missing fields:** `none`

因為你尚未註冊自助復原，第一步仍是透過 ExampleDesk 提交帳戶復原請求；全職身分與公司管理筆電不足以單獨取得自助流程資格。[SRC-07] 請附識別與聯絡資訊、非機密錯訊、發生時間，並註明裝置受公司管理、尚未註冊自助復原及已確認鎖定。不要提供密碼、驗證碼或復原連結。請求交由 Example IT Service Desk 檢視，提交不代表已解鎖，也沒有直接解鎖或處理時間的保證。[SRC-03]

**Cited sources:** SRC-07, SRC-03

### SYN-04 — Historical lock before update

**Question:** 請說明我在 2030-01-20 帳戶已確認鎖定時應採用的處理流程。我是全職員工，用公司管理筆電，已註冊自助復原。

**Route:** `ANSWER` · **First action:** `SUBMIT_EXAMPLEDESK_REQUEST` · **Missing fields:** `none`

應依事件日期 2030-01-20 判斷，採用當時已生效的 ExampleDesk 基準流程；2030-03-01 才生效的自助第一步不回溯適用，即使三項資格皆符合也一樣。[SRC-03][SRC-07] 當時應提交帳戶復原請求，由 Example IT Service Desk 檢視，附識別與聯絡資訊、非機密錯訊、發生時間及裝置管理、復原註冊、已確認鎖定等狀態；不得附登入秘密。這只說明當時應採用的程序，不能證明請求曾送出或帳戶已解鎖，也不保證處理時間。[SRC-03]

**Cited sources:** SRC-03, SRC-07

### SYN-05 — Ambiguous login rejection

**Question:** ExampleVPN 出現 DEMO-101，是帳號被鎖嗎？

**Route:** `CLARIFY` · **First action:** `CLARIFY_ACCOUNT_STATE` · **Missing fields:** `account_state, error_message, other_approved_login_available`

不能只憑 DEMO-101 判定帳戶鎖定；它也可能涉及密碼輸入錯誤、密碼到期或網路狀況。[SRC-02] 請確認是否收到明確的鎖定或到期通知，並提供不含機密的完整錯誤文字；也請說明能否在其他公司核准的工作流程中登入。不要提供密碼或驗證碼。釐清實際狀態後，才能選擇適用處理分支。[SRC-01]

**Cited sources:** SRC-02, SRC-01

### SYN-06 — Confirmed expiry on managed laptop

**Question:** 公司管理筆電提示密碼已到期，我目前可連公司網路，ExampleVPN 登入失敗，怎麼更新密碼？

**Route:** `ANSWER` · **First action:** `CONNECT_COMPANY_NETWORK` · **Missing fields:** `none`

你已確認密碼到期、使用公司管理筆電且公司網路可用，請先連上公司網路，再按 Ctrl+Alt+Delete，選擇「變更密碼」並依畫面完成；之後依組織核准流程測試登入，不要將密碼提供給支援人員。這是本合成教學案例的程序，不保證適用其他環境。[SRC-02] 若操作無法使用，停止自行嘗試並聯絡 Example IT Service Desk。不要用消費者入口網站同步密碼，也不要以帳戶解鎖替代更新到期密碼；SRC-07 未變更此程序。[SRC-02][SRC-07]

**Cited sources:** SRC-02, SRC-07

### SYN-07 — Branch remote resource restriction

**Question:** 我是 Branch Support，已透過 ExampleVPN 遠端連線，想用 TeamShare，可以直接申請資料夾權限嗎？

**Route:** `ANSWER` · **First action:** `RESPECT_REMOTE_ACCESS_RESTRICTION` · **Missing fields:** `none`

不能用一般資料夾權限申請取得這條遠端路徑上的 TeamShare 存取。Branch Support 經 ExampleVPN 遠端連線的政策範圍包含 ExampleCRM，但不包含 TeamShare；即使要求的角色只是 reader，申請流程也不會覆蓋此限制。VPN 連線成功不代表資源權限已核准。[SRC-05]

**Cited sources:** SRC-05

### SYN-08 — Unknown resource scope

**Question:** 我想使用 TeamShare，可以幫我申請嗎？

**Route:** `CLARIFY` · **First action:** `CLARIFY_ACCESS_CONTEXT` · **Missing fields:** `support_group, network_path, requested_role`

請先提供你的支援群組、目前所在網路／連線路徑，以及需要的角色；這些資訊尚未確認，不能先判定你適用哪個 TeamShare 分支。[SRC-05] 若是 HQ Support 且在公司網路，可透過 ExampleDesk 提出申請，屆時需附使用者識別碼、邏輯資料夾名稱及所需角色；若是 Branch Support 經 ExampleVPN 遠端連線，該申請流程不能覆蓋 TeamShare 路徑限制。目前未替你提交申請或授予權限。[SRC-05]

**Cited sources:** SRC-05

### SYN-09 — Incomplete overseas application

**Question:** 我要到 Example Region 出差辦理教學專案，需要海外連線，但還沒有確定起訖日期，也尚未送主管核准，接下來怎麼辦？

**Route:** `CLARIFY` · **First action:** `CLARIFY_TRAVEL_DATES` · **Missing fields:** `start_date, end_date`

請先確認預計開始日與結束日；申請人識別資訊、目的地與業務目的已提供，不需重填或猜測日期。[SRC-06] 日期齊備後，將現有資料與需要遠端連線的工作範圍整理成申請，透過 ExampleDesk 提交，由直屬主管先審查。主管核准後才轉交 Network Operations 並納入 Security Review；所有相關審查完成且獲准後，才安排啟用，待審或拒絕都不得先開通。核准僅在申請日期範圍內有效，延長須重新申請；目前未替你提交、核准或啟用。[SRC-06]

**Cited sources:** SRC-06

### SYN-10 — Undocumented error

**Question:** ExampleVPN 出現 DEMO-999，這是什麼原因、要怎麼修？

**Route:** `NO_ANSWER` · **First action:** `ESCALATE_UNDOCUMENTED_ERROR` · **Missing fields:** `none`

本次證據集未記錄 DEMO-999 的原因或修復方法，因此無法判定如何修復；不能借用其他代碼的描述，推論它是密碼、網路或裝置授權問題。請保存不含機密的完整錯誤原文與發生情境，交由服務台判讀。這是目前資料的證據邊界，不代表其他來源一定沒有相關資訊。[SRC-02]

**Cited sources:** SRC-02

### SYN-11 — Compare Branch remote restriction with HQ corporate-network application

**Question:** 我是 HQ Support，在公司網路想使用 TeamShare；這和 Branch Support 透過 ExampleVPN 遠端連線的情況有什麼不同？送出申請就能使用嗎？

**Route:** `ANSWER` · **First action:** `PREPARE_TEAMSHARE_REQUEST` · **Missing fields:** `none`

你是 HQ Support 且在公司網路，可準備使用者識別碼、邏輯資料夾名稱及所需角色，透過 ExampleDesk 提出 TeamShare 權限申請；角色或資料夾用途不清楚時須先釐清。[SRC-05] 相較之下，Branch Support 經 ExampleVPN 遠端連線的範圍包含 ExampleCRM，但不包含 TeamShare，一般申請不能覆蓋該路徑限制。你送出申請後仍須經核准流程檢視，不能把提交請求當成已核准、已生效或已可使用的證據。[SRC-05]

**Cited sources:** SRC-05
