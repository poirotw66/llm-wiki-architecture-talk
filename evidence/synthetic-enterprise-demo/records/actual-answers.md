# 十題實際回答

以下保留模型原始回答與來源摘錄，不以參考答案補寫。模型 first_action 原始標籤保留，語意對照與判定見 [回歸結果](regression-results.json)。每階段十題同批生成，各使用新的 inference 工作階段。

更新後 SYN-05 含一處繁簡混用，屬原始模型格式缺陷；本檔保留輸出以便審查。

## SYN-01

問題：我是全職員工，使用公司管理筆電，已註冊自助復原，現在明確顯示帳戶鎖定，應該怎麼處理？

### 基準

`route: ANSWER` · `first_action: SUBMIT_RECOVERY_REQUEST`

依截至 2030-02-01 的合成基準，請透過 ExampleDesk 提交帳戶復原請求，由 Example IT Service Desk 檢視。您已確認鎖定，適用此流程；已註冊自助復原並不支持改用資料集未記錄的其他處理方式。[SRC-03] 請附識別與聯絡資訊、非機密錯訊及發生時間，並填入已知的公司管理筆電、自助復原已註冊及已確認鎖定狀態。不要提供密碼、驗證碼或復原連結。此回答未提交請求或解鎖；服務台檢視也不保證直接解除鎖定或特定處理時間。[SRC-03]

來源摘錄：

- [SRC-03: account-recovery-v1.md](../baseline-v1/raw/sources/account-recovery-v1.md)

```text
已確認鎖定時，使用者透過 ExampleDesk 提交帳戶復原請求，交由 Example IT Service Desk 檢視。此基準流程不表示服務台人員一定會直接解除鎖定，也不承諾特定處理時間。後續操作須依核實結果與支援流程決定。
```

- [SRC-03: account-recovery-v1.md](../baseline-v1/raw/sources/account-recovery-v1.md)

```text
請求應包含：

1. 使用者識別資訊與聯絡方式。
2. 不含秘密的錯誤文字或代碼，以及發生時間。
3. 裝置是否由公司管理；若不清楚，填「未知」。
4. 自助復原是否已註冊；若不清楚，填「未知」。
5. 使用者已確認的狀態，例如「收到鎖定提示」或「尚未確認」。

不得在請求中放入密碼、驗證碼、復原連結或其他登入秘密。
```

- [SRC-03: account-recovery-v1.md](../baseline-v1/raw/sources/account-recovery-v1.md)

```text
此版本適用於全職員工與承包人員的已確認帳戶鎖定情境，直到有明確範圍的變更生效。
```

### 更新後

`route: ANSWER` · `first_action: TRY_SELF_SERVICE_RECOVERY`

以目前情境日期 2030-03-02 判斷，你已確認鎖定，且三項資格皆符合，第一步是前往 https://support.example.com/account-recovery 嘗試自助復原。這是合成教學用的虛構入口，沒有實際服務或交易，不能當成已完成復原的證據；結果仍須由使用者確認。若流程失敗或結果不明，轉由 Example IT Service Desk 處理。[SRC-07] 此回答依尚待人工審查的知識草稿整理，未執行復原。

來源摘錄：

- [SRC-07: account-recovery-update-v2.md](../updated-v2/raw/sources/account-recovery-update-v2.md)

```text
自 2030-03-01 起，本通知只變更「已確認帳戶鎖定」時的第一步，而且必須同時符合下列三項條件：

1. 使用者是全職員工。
2. 使用者正在使用公司管理筆電。
3. 使用者已註冊自助帳戶復原。
```

- [SRC-07: account-recovery-update-v2.md](../updated-v2/raw/sources/account-recovery-update-v2.md)

```text
三項都確認為符合時，請使用者前往虛構入口網站 <https://support.example.com/account-recovery> 嘗試自助復原。此連結僅供教學示例，不能執行真實交易，也不可視為已完成復原的證據。完成後仍須由使用者確認結果；若流程失敗或狀態不明，轉由 Example IT Service Desk 處理。
```

## SYN-02

問題：我是承包人員，使用公司管理筆電，也有註冊自助復原，帳戶已確認鎖定，可以使用同樣流程嗎？

### 基準

`route: ANSWER` · `first_action: SUBMIT_RECOVERY_REQUEST`

可以。依截至 2030-02-01 的合成基準，承包人員的已確認帳戶鎖定也適用同一服務台流程：透過 ExampleDesk 提交帳戶復原請求，由 Example IT Service Desk 檢視。[SRC-03] 附上識別與聯絡資訊、非機密錯訊及發生時間，並記錄公司管理筆電、自助復原已註冊及已確認鎖定狀態；不要提供密碼、驗證碼或復原連結。已註冊自助復原不代表此資料集另有自助解鎖程序。此回答未提交或解鎖，服務台也不保證直接解除鎖定或特定處理時間。[SRC-03]

來源摘錄：

- [SRC-03: account-recovery-v1.md](../baseline-v1/raw/sources/account-recovery-v1.md)

```text
此版本適用於全職員工與承包人員的已確認帳戶鎖定情境，直到有明確範圍的變更生效。
```

- [SRC-03: account-recovery-v1.md](../baseline-v1/raw/sources/account-recovery-v1.md)

```text
已確認鎖定時，使用者透過 ExampleDesk 提交帳戶復原請求，交由 Example IT Service Desk 檢視。此基準流程不表示服務台人員一定會直接解除鎖定，也不承諾特定處理時間。後續操作須依核實結果與支援流程決定。
```

- [SRC-03: account-recovery-v1.md](../baseline-v1/raw/sources/account-recovery-v1.md)

```text
請求應包含：

1. 使用者識別資訊與聯絡方式。
2. 不含秘密的錯誤文字或代碼，以及發生時間。
3. 裝置是否由公司管理；若不清楚，填「未知」。
4. 自助復原是否已註冊；若不清楚，填「未知」。
5. 使用者已確認的狀態，例如「收到鎖定提示」或「尚未確認」。

不得在請求中放入密碼、驗證碼、復原連結或其他登入秘密。
```

### 更新後

`route: ANSWER` · `first_action: SUBMIT_RECOVERY_REQUEST`

不能套用相同的自助第一步。以 2030-03-02 判斷，承包人員即使使用公司管理筆電且已註冊自助復原，仍沿用 ExampleDesk 服務台路徑。[SRC-07] 請提交帳戶復原請求，附識別與聯絡資訊、非機密錯訊及發生時間、裝置管理狀態、自助復原註冊狀態與已確認鎖定的訊息；不得附密碼、驗證碼或復原連結。由 Example IT Service Desk 檢視，提交不代表已解鎖，也不保證處理時間。[SRC-03] 這是合成教學草稿的流程建議，未替你提交請求。

來源摘錄：

- [SRC-07: account-recovery-update-v2.md](../updated-v2/raw/sources/account-recovery-update-v2.md)

```text
已確認為承包人員、不受公司管理的裝置，或尚未註冊自助復原時，沿用 [SRC-03](account-recovery-v1.md) 的 ExampleDesk 服務台路徑。
```

- [SRC-03: account-recovery-v1.md](../updated-v2/raw/sources/account-recovery-v1.md)

```text
已確認鎖定時，使用者透過 ExampleDesk 提交帳戶復原請求，交由 Example IT Service Desk 檢視。此基準流程不表示服務台人員一定會直接解除鎖定，也不承諾特定處理時間。後續操作須依核實結果與支援流程決定。
```

- [SRC-03: account-recovery-v1.md](../updated-v2/raw/sources/account-recovery-v1.md)

```text
請求應包含：

1. 使用者識別資訊與聯絡方式。
2. 不含秘密的錯誤文字或代碼，以及發生時間。
3. 裝置是否由公司管理；若不清楚，填「未知」。
4. 自助復原是否已註冊；若不清楚，填「未知」。
5. 使用者已確認的狀態，例如「收到鎖定提示」或「尚未確認」。

不得在請求中放入密碼、驗證碼、復原連結或其他登入秘密。
```

## SYN-03

問題：我是全職員工，筆電受公司管理，但尚未註冊自助復原；帳戶已確認鎖定，該怎麼辦？

### 基準

`route: ANSWER` · `first_action: SUBMIT_RECOVERY_REQUEST`

請透過 ExampleDesk 提交帳戶復原請求。依截至 2030-02-01 的合成基準，您已確認鎖定且為全職員工，適用此流程；文件未把自助復原註冊列為提交請求的必要前提。[SRC-03] 附上識別與聯絡資訊、非機密錯訊及發生時間，將裝置填為公司管理、自助復原填為未註冊、帳戶填為已確認鎖定。不要提供密碼、驗證碼或復原連結。此回答未提交或解鎖，後續由服務台核實決定，不保證直接解除或特定處理時間。[SRC-03]

來源摘錄：

- [SRC-03: account-recovery-v1.md](../baseline-v1/raw/sources/account-recovery-v1.md)

```text
已確認鎖定時，使用者透過 ExampleDesk 提交帳戶復原請求，交由 Example IT Service Desk 檢視。此基準流程不表示服務台人員一定會直接解除鎖定，也不承諾特定處理時間。後續操作須依核實結果與支援流程決定。
```

- [SRC-03: account-recovery-v1.md](../baseline-v1/raw/sources/account-recovery-v1.md)

```text
請求應包含：

1. 使用者識別資訊與聯絡方式。
2. 不含秘密的錯誤文字或代碼，以及發生時間。
3. 裝置是否由公司管理；若不清楚，填「未知」。
4. 自助復原是否已註冊；若不清楚，填「未知」。
5. 使用者已確認的狀態，例如「收到鎖定提示」或「尚未確認」。

不得在請求中放入密碼、驗證碼、復原連結或其他登入秘密。
```

- [SRC-03: account-recovery-v1.md](../baseline-v1/raw/sources/account-recovery-v1.md)

```text
此版本適用於全職員工與承包人員的已確認帳戶鎖定情境，直到有明確範圍的變更生效。
```

### 更新後

`route: ANSWER` · `first_action: SUBMIT_RECOVERY_REQUEST`

以 2030-03-02 判斷，尚未註冊自助復原就不符合自助第一步的完整資格，應透過 ExampleDesk 提交帳戶復原請求。[SRC-07] 請附識別與聯絡資訊、非機密錯訊及發生時間，註明筆電受公司管理、自助復原尚未註冊，以及已確認鎖定。不要附密碼、驗證碼或復原連結；服務台檢視不代表已解除鎖定，也沒有特定處理時間保證。[SRC-03] 這是合成教學草稿的流程建議，未執行提交或解鎖。

來源摘錄：

- [SRC-07: account-recovery-update-v2.md](../updated-v2/raw/sources/account-recovery-update-v2.md)

```text
已確認為承包人員、不受公司管理的裝置，或尚未註冊自助復原時，沿用 [SRC-03](account-recovery-v1.md) 的 ExampleDesk 服務台路徑。
```

- [SRC-03: account-recovery-v1.md](../updated-v2/raw/sources/account-recovery-v1.md)

```text
已確認鎖定時，使用者透過 ExampleDesk 提交帳戶復原請求，交由 Example IT Service Desk 檢視。此基準流程不表示服務台人員一定會直接解除鎖定，也不承諾特定處理時間。後續操作須依核實結果與支援流程決定。
```

- [SRC-03: account-recovery-v1.md](../updated-v2/raw/sources/account-recovery-v1.md)

```text
請求應包含：

1. 使用者識別資訊與聯絡方式。
2. 不含秘密的錯誤文字或代碼，以及發生時間。
3. 裝置是否由公司管理；若不清楚，填「未知」。
4. 自助復原是否已註冊；若不清楚，填「未知」。
5. 使用者已確認的狀態，例如「收到鎖定提示」或「尚未確認」。

不得在請求中放入密碼、驗證碼、復原連結或其他登入秘密。
```

## SYN-04

問題：請說明我在 2030-01-20 帳戶已確認鎖定時應採用的處理流程。我是全職員工，用公司管理筆電，已註冊自助復原。

### 基準

`route: ANSWER` · `first_action: SUBMIT_RECOVERY_REQUEST`

以事件日期 2030-01-20 判斷，當時已在 2030-01-10 起生效的鎖定復原基準期間內，應透過 ExampleDesk 提交帳戶復原請求，由 Example IT Service Desk 檢視。您的全職員工身分與已確認鎖定符合適用範圍；自助復原已註冊不支持另行推定其他程序。[SRC-03] 請求應記錄識別與聯絡資訊、當時的非機密錯訊及發生時間，以及公司管理筆電、自助復原已註冊、已確認鎖定狀態。不要提供登入秘密。這是歷史流程說明，未提交請求，也不證明當時已解鎖。[SRC-03]

來源摘錄：

- [SRC-03: account-recovery-v1.md](../baseline-v1/raw/sources/account-recovery-v1.md)

```text
本文件記錄 2030-01-10 起使用的鎖定復原基準。
```

- [SRC-03: account-recovery-v1.md](../baseline-v1/raw/sources/account-recovery-v1.md)

```text
此版本適用於全職員工與承包人員的已確認帳戶鎖定情境，直到有明確範圍的變更生效。後續變更須明示取代的段落、條件與生效日；不可只按文件日期採取「較新文件全面取代較舊文件」的規則。
```

- [SRC-03: account-recovery-v1.md](../baseline-v1/raw/sources/account-recovery-v1.md)

```text
已確認鎖定時，使用者透過 ExampleDesk 提交帳戶復原請求，交由 Example IT Service Desk 檢視。此基準流程不表示服務台人員一定會直接解除鎖定，也不承諾特定處理時間。後續操作須依核實結果與支援流程決定。
```

- [SRC-03: account-recovery-v1.md](../baseline-v1/raw/sources/account-recovery-v1.md)

```text
請求應包含：

1. 使用者識別資訊與聯絡方式。
2. 不含秘密的錯誤文字或代碼，以及發生時間。
3. 裝置是否由公司管理；若不清楚，填「未知」。
4. 自助復原是否已註冊；若不清楚，填「未知」。
5. 使用者已確認的狀態，例如「收到鎖定提示」或「尚未確認」。

不得在請求中放入密碼、驗證碼、復原連結或其他登入秘密。
```

### 更新後

`route: ANSWER` · `first_action: SUBMIT_RECOVERY_REQUEST`

應以事件日期 2030-01-20 判斷，採用當時已生效的 ExampleDesk 基準流程；2030-03-01 才生效的自助第一步不能回溯套用，即使三項資格都符合也一樣。[SRC-03][SRC-07] 當時應提交帳戶復原請求，由 Example IT Service Desk 檢視，附識別與聯絡資訊、非機密錯訊及發生時間、裝置管理與自助復原註冊狀態、明確鎖定訊息。不得附登入秘密，且提交不代表已解鎖或保證處理時間。[SRC-03] 這是合成教學草稿對歷史流程的說明，沒有證明當時已提交或完成復原。

來源摘錄：

- [SRC-03: account-recovery-v1.md](../updated-v2/raw/sources/account-recovery-v1.md)

```text
本文件記錄 2030-01-10 起使用的鎖定復原基準。
```

- [SRC-07: account-recovery-update-v2.md](../updated-v2/raw/sources/account-recovery-update-v2.md)

```text
2030-03-01 之前發生的情境依當時基準處理；自生效日起才依本通知的完整資格條件套用新第一步。這是局部更新，不代表所有舊文件失效。
```

- [SRC-03: account-recovery-v1.md](../updated-v2/raw/sources/account-recovery-v1.md)

```text
已確認鎖定時，使用者透過 ExampleDesk 提交帳戶復原請求，交由 Example IT Service Desk 檢視。此基準流程不表示服務台人員一定會直接解除鎖定，也不承諾特定處理時間。後續操作須依核實結果與支援流程決定。
```

- [SRC-03: account-recovery-v1.md](../updated-v2/raw/sources/account-recovery-v1.md)

```text
請求應包含：

1. 使用者識別資訊與聯絡方式。
2. 不含秘密的錯誤文字或代碼，以及發生時間。
3. 裝置是否由公司管理；若不清楚，填「未知」。
4. 自助復原是否已註冊；若不清楚，填「未知」。
5. 使用者已確認的狀態，例如「收到鎖定提示」或「尚未確認」。

不得在請求中放入密碼、驗證碼、復原連結或其他登入秘密。
```

## SYN-05

問題：ExampleVPN 出現 DEMO-101，是帳號被鎖嗎？

### 基準

`route: CLARIFY` · `first_action: CLARIFY_ACCOUNT_STATE`

不能只憑 DEMO-101 判定帳戶被鎖；它也可能與密碼輸入錯誤、密碼到期或網路狀況有關，這些都只是待查方向。[SRC-01][SRC-02] 請確認是否收到明確的鎖定或到期通知，並提供不含機密的完整錯訊、發生時間、裝置管理狀態及當時公司網路是否可用；也請說明能否在其他公司核准的工作流程中登入。不要提供密碼或驗證碼。確認狀態後才能選擇鎖定復原、到期處理或其他支援分支，目前尚未確認原因。[SRC-01]

來源摘錄：

- [SRC-01: vpn-common-qa.md](../baseline-v1/raw/sources/vpn-common-qa.md)

```text
先記錄使用者看到的完整訊息、發生時間、裝置管理狀態，以及當時是否可連公司網路。錯誤代碼只協助判斷方向，不能單獨證明帳戶、密碼或授權的狀態。
```

- [SRC-01: vpn-common-qa.md](../baseline-v1/raw/sources/vpn-common-qa.md)

```text
DEMO-101 可能與密碼輸入錯誤、已確認的帳戶鎖定、密碼到期或當下網路狀況有關。這些是待查原因；不可只因代碼出現就判定帳戶已鎖定。先確認使用者能否在其他公司核准的工作流程中登入，並詢問是否收到明確的到期或鎖定通知。不要索取密碼或驗證碼。
```

- [SRC-02: examplevpn-error-reference.md](../baseline-v1/raw/sources/examplevpn-error-reference.md)

```text
| DEMO-101 | 密碼輸入錯誤、已確認鎖定、密碼到期或網路狀況 | 先釐清狀態；代碼本身不代表帳戶鎖定。 |
```

- [SRC-01: vpn-common-qa.md](../baseline-v1/raw/sources/vpn-common-qa.md)

```text
若已有明確訊息確認帳戶鎖定，依基準帳戶復原流程建立 ExampleDesk 請求；所需資訊與邊界見 [SRC-03](account-recovery-v1.md)。若確認密碼已到期，請改走 [SRC-02](examplevpn-error-reference.md) 的到期處理程序。
```

追問欄位：`account_state, error_message, occurrence_time, device_management, company_network_available, approved_workflow_login_available`

### 更新後

`route: CLARIFY` · `first_action: CLARIFY_ACCOUNT_STATE`

不能只憑 DEMO-101 判定帳戶鎖定；它也可能涉及密碼輸入錯誤、密碼到期或網路狀況，目前原因仍未確認。[SRC-01][SRC-02] 你是否收到明確的鎖定或到期通知？請補充不含秘密的完整錯訊、發生時間、装置是否受公司管理，以及當時是否可連公司網路。也可說明是否能在其他公司核准的工作流程中登入；不要提供密碼或驗證碼。確認狀態後才能選擇適用分支。[SRC-01] 此判斷依合成教學草稿，尚未完成診斷。

來源摘錄：

- [SRC-01: vpn-common-qa.md](../updated-v2/raw/sources/vpn-common-qa.md)

```text
先記錄使用者看到的完整訊息、發生時間、裝置管理狀態，以及當時是否可連公司網路。錯誤代碼只協助判斷方向，不能單獨證明帳戶、密碼或授權的狀態。
```

- [SRC-01: vpn-common-qa.md](../updated-v2/raw/sources/vpn-common-qa.md)

```text
DEMO-101 可能與密碼輸入錯誤、已確認的帳戶鎖定、密碼到期或當下網路狀況有關。這些是待查原因；不可只因代碼出現就判定帳戶已鎖定。先確認使用者能否在其他公司核准的工作流程中登入，並詢問是否收到明確的到期或鎖定通知。不要索取密碼或驗證碼。
```

- [SRC-02: examplevpn-error-reference.md](../updated-v2/raw/sources/examplevpn-error-reference.md)

```text
| DEMO-101 | 密碼輸入錯誤、已確認鎖定、密碼到期或網路狀況 | 先釐清狀態；代碼本身不代表帳戶鎖定。 |
```

追問欄位：`account_state, error_message, event_time, device_management, company_network_available`

## SYN-06

問題：公司管理筆電提示密碼已到期，我目前可連公司網路，ExampleVPN 登入失敗，怎麼更新密碼？

### 基準

`route: ANSWER` · `first_action: CHANGE_PASSWORD`

您已確認密碼到期、使用公司管理筆電，且公司網路可用：請先連上公司網路，再按 Ctrl+Alt+Delete，選擇「變更密碼」，依畫面完成。完成後依組織核准流程測試登入，不要把密碼提供給支援人員。[SRC-02] 若操作無法使用，或實際無法連公司網路，請停止自行嘗試並聯絡 Example IT Service Desk。不要改用消費者入口網站同步密碼；解除鎖定也不會重設或延長到期密碼。這是合成案例的步驟，此回答未替您變更密碼。[SRC-02]

來源摘錄：

- [SRC-02: examplevpn-error-reference.md](../baseline-v1/raw/sources/examplevpn-error-reference.md)

```text
若已確認密碼到期，且使用者正在使用公司管理筆電，先連上公司網路，再按 Ctrl+Alt+Delete 並選擇變更密碼，依畫面完成變更。這是本虛構案例的明確步驟，不保證適用於其他環境。變更後再依組織核准流程測試登入，不要把密碼提供給支援人員。
```

- [SRC-02: examplevpn-error-reference.md](../baseline-v1/raw/sources/examplevpn-error-reference.md)

```text
若人在遠端而無法連公司網路，或上述步驟無法使用，請停止自行嘗試並聯絡 Example IT Service Desk。不要改用消費者入口網站同步密碼，也不可聲稱解除帳戶鎖定就會重設或延長已到期密碼。
```

### 更新後

`route: ANSWER` · `first_action: CONNECT_COMPANY_NETWORK`

你已確認密碼到期、使用公司管理筆電且公司網路可用，請先連上公司網路，再按 Ctrl+Alt+Delete，選擇「變更密碼」並依畫面完成；變更後依組織核准流程測試登入，不要把密碼提供給支援人員。[SRC-02] 若操作無法使用，停止自行嘗試並聯絡 Example IT Service Desk。不能改用消費者入口網站同步密碼，也不能以帳戶解鎖重設或延長到期密碼。[SRC-02] SRC-07 沒有變更這項到期程序；以上僅為合成教學草稿的操作建議，未執行密碼變更。[SRC-07]

來源摘錄：

- [SRC-02: examplevpn-error-reference.md](../updated-v2/raw/sources/examplevpn-error-reference.md)

```text
若已確認密碼到期，且使用者正在使用公司管理筆電，先連上公司網路，再按 Ctrl+Alt+Delete 並選擇變更密碼，依畫面完成變更。這是本虛構案例的明確步驟，不保證適用於其他環境。變更後再依組織核准流程測試登入，不要把密碼提供給支援人員。
```

- [SRC-02: examplevpn-error-reference.md](../updated-v2/raw/sources/examplevpn-error-reference.md)

```text
若人在遠端而無法連公司網路，或上述步驟無法使用，請停止自行嘗試並聯絡 Example IT Service Desk。不要改用消費者入口網站同步密碼，也不可聲稱解除帳戶鎖定就會重設或延長已到期密碼。
```

- [SRC-07: account-recovery-update-v2.md](../updated-v2/raw/sources/account-recovery-update-v2.md)

```text
本通知不變更 [SRC-02](examplevpn-error-reference.md) 的密碼到期程序、DEMO-202 網路診斷、DEMO-303 裝置註冊或授權檢查、[SRC-05](shared-resource-access-policy.md) 資源規則，亦不變更 [SRC-06](overseas-access-request.md) 海外核准流程。
```

## SYN-07

問題：我是 Branch Support，已透過 ExampleVPN 遠端連線，想用 TeamShare，可以直接申請資料夾權限嗎？

### 基準

`route: ANSWER` · `first_action: RESPECT_ACCESS_LIMIT`

依本合成政策，Branch Support 經 ExampleVPN 遠端連線的範圍包含 ExampleCRM，但不包含 TeamShare；一般資料夾權限申請不能覆蓋此遠端路徑限制，即使要求的是讀取角色也不能據此取得 TeamShare 存取。[SRC-05] 因此不能直接套用 HQ Support 在公司網路上的申請流程。VPN 連線成功只表示建立了連線，不是資源授權證明；此回答未提出申請或開通權限。[SRC-05]

來源摘錄：

- [SRC-05: shared-resource-access-policy.md](../baseline-v1/raw/sources/shared-resource-access-policy.md)

```text
- **Branch Support 群組：**經 ExampleVPN 遠端連線時，可以使用 ExampleCRM；此情境不包含 TeamShare。
- **HQ Support 群組：**在公司網路上可提出 TeamShare 權限申請。申請不代表已核准或已生效。
```

- [SRC-05: shared-resource-access-policy.md](../baseline-v1/raw/sources/shared-resource-access-policy.md)

```text
Branch Support 即使已連上 ExampleVPN，也不能據此要求 TeamShare 存取。此申請流程不會覆蓋該遠端路徑限制。HQ Support 在公司網路上提出申請，也不表示系統已完成授權。不得把連線成功、群組名稱或已送出請求當成權限核准證明。
```

### 更新後

`route: ANSWER` · `first_action: RESPECT_RESOURCE_RESTRICTION`

依本合成教學草稿，Branch Support 經 ExampleVPN 遠端連線的範圍包含 ExampleCRM，但不包含 TeamShare；不能透過一般資料夾權限申請覆蓋這項路徑限制，即使只要求 reader 角色也沒有例外依據。[SRC-05] VPN 連線成功不等於資源授權，這裡未申請或開通 TeamShare，也不能據此推論檢索系統已實作群組存取控制。[SRC-05]

來源摘錄：

- [SRC-05: shared-resource-access-policy.md](../updated-v2/raw/sources/shared-resource-access-policy.md)

```text
- **Branch Support 群組：**經 ExampleVPN 遠端連線時，可以使用 ExampleCRM；此情境不包含 TeamShare。
```

- [SRC-05: shared-resource-access-policy.md](../updated-v2/raw/sources/shared-resource-access-policy.md)

```text
Branch Support 即使已連上 ExampleVPN，也不能據此要求 TeamShare 存取。此申請流程不會覆蓋該遠端路徑限制。HQ Support 在公司網路上提出申請，也不表示系統已完成授權。不得把連線成功、群組名稱或已送出請求當成權限核准證明。
```

- [SRC-05: shared-resource-access-policy.md](../updated-v2/raw/sources/shared-resource-access-policy.md)

```text
此文件沒有說明任何檢索系統的受眾中繼資料、資料列過濾或存取控制實作；不可從本文推論系統已按群組限制檢索結果。
```

## SYN-08

問題：我想使用 TeamShare，可以幫我申請嗎？

### 基準

`route: CLARIFY` · `first_action: CLARIFY_ACCESS_CONTEXT`

請先提供您的支援群組、目前所在網路或連線路徑，以及需要的角色；目前資料不足以判定適用哪個分支，也不能替您選擇角色。[SRC-05] 若確認是 HQ Support 且在公司網路，可透過 ExampleDesk 提出申請，屆時需附使用者識別碼、邏輯資料夾名稱及所需角色。若是 Branch Support 經 ExampleVPN 遠端連線，該範圍不含 TeamShare，一般申請也不能覆蓋限制。此回答尚未提交申請；申請本身不代表核准或授權生效。[SRC-05]

來源摘錄：

- [SRC-05: shared-resource-access-policy.md](../baseline-v1/raw/sources/shared-resource-access-policy.md)

```text
若使用者的群組、所在網路或要求角色未知，先向使用者釐清並保留未決狀態。
```

- [SRC-05: shared-resource-access-policy.md](../baseline-v1/raw/sources/shared-resource-access-policy.md)

```text
HQ Support 申請時，請透過 ExampleDesk 提供申請人的使用者識別碼（虛構示例：`EMP-DEMO-001`）、邏輯資料夾名稱及所需角色。服務台會依既有核准流程檢視；若角色或資料夾用途不清楚，應先詢問，不可自行授予較高權限。
```

- [SRC-05: shared-resource-access-policy.md](../baseline-v1/raw/sources/shared-resource-access-policy.md)

```text
Branch Support 即使已連上 ExampleVPN，也不能據此要求 TeamShare 存取。此申請流程不會覆蓋該遠端路徑限制。HQ Support 在公司網路上提出申請，也不表示系統已完成授權。
```

追問欄位：`support_group, network_path, requested_role`

### 更新後

`route: CLARIFY` · `first_action: CLARIFY_ACCESS_CONTEXT`

請先提供所屬群組、目前所在網路或連線路徑，以及需要的角色；目前保留未決狀態，不能假定你符合 TeamShare 申請條件。[SRC-05] 若確認是 HQ Support 且在公司網路，可透過 ExampleDesk 申請，屆時需附使用者識別碼、邏輯資料夾名稱與所需角色；申請不代表核准或生效。若是 Branch Support 經 ExampleVPN 遠端連線，則不能用此申請流程覆蓋 TeamShare 限制。[SRC-05] 以上依合成教學草稿說明，尚未替你提交申請。

來源摘錄：

- [SRC-05: shared-resource-access-policy.md](../updated-v2/raw/sources/shared-resource-access-policy.md)

```text
若使用者的群組、所在網路或要求角色未知，先向使用者釐清並保留未決狀態。
```

- [SRC-05: shared-resource-access-policy.md](../updated-v2/raw/sources/shared-resource-access-policy.md)

```text
- **HQ Support 群組：**在公司網路上可提出 TeamShare 權限申請。申請不代表已核准或已生效。

HQ Support 申請時，請透過 ExampleDesk 提供申請人的使用者識別碼（虛構示例：`EMP-DEMO-001`）、邏輯資料夾名稱及所需角色。
```

- [SRC-05: shared-resource-access-policy.md](../updated-v2/raw/sources/shared-resource-access-policy.md)

```text
Branch Support 即使已連上 ExampleVPN，也不能據此要求 TeamShare 存取。此申請流程不會覆蓋該遠端路徑限制。
```

追問欄位：`support_group, network_path, requested_role`

## SYN-09

問題：我要到 Example Region 出差辦理教學專案，需要海外連線，但還沒有確定起訖日期，也尚未送主管核准，接下來怎麼辦？

### 基準

`route: CLARIFY` · `first_action: CLARIFY_TRAVEL_DATES`

請先確認預計開始日與結束日；這兩項是必要資料，不能代填猜測。您已提供申請人識別碼、Example Region 目的地及教學專案業務目的，無需重問。[SRC-06] 日期確定後，透過 ExampleDesk 提交完整資料，先由直屬主管審查；主管核准後，再轉交 Network Operations 並納入 Security Review。只有相關審查完成且獲准後才能安排啟用，待審或拒絕時不得先啟用。核准僅在申請日期範圍內有效，延長須重新申請。此回答未提交、核准或啟用海外存取。[SRC-06]

來源摘錄：

- [SRC-06: overseas-access-request.md](../baseline-v1/raw/sources/overseas-access-request.md)

```text
- 申請人識別資訊。
- 目的地國家或地區。
- 預計開始日與結束日。
- 業務目的及需要遠端連線的工作範圍。

資料缺漏或日期不明時，服務台應退回補充或請申請人釐清，不應代填猜測。
```

- [SRC-06: overseas-access-request.md](../baseline-v1/raw/sources/overseas-access-request.md)

```text
1. 申請人透過 ExampleDesk 提交資料。
2. 直屬主管檢視業務目的與日期並作出核准或拒絕。
3. 主管核准後，ExampleDesk 將申請轉交 Network Operations，並納入 Security Review。
4. 只有相關審查完成且獲准後，才可安排啟用；拒絕或待審時不得先行啟用。
5. 核准僅在申請所列日期範圍內有效，結束日到期後停止該次臨時安排；需要延長時須重新提出申請。
```

追問欄位：`start_date, end_date`

### 更新後

`route: CLARIFY` · `first_action: CLARIFY_TRAVEL_DATES`

下一步先確認預計開始日與結束日；請提供這兩個日期，不應代填或猜測。你已提供申請人識別碼、目的地與業務目的，無須重填；申請內容也要列明教學專案需要遠端連線的工作範圍。[SRC-06] 資料齊備後透過 ExampleDesk 提交，由直屬主管先審查；主管核准後才轉交 Network Operations 並納入 Security Review，相關審查完成且獲准後才安排啟用。尚未送主管核准，不能視為已獲准或先行開通。核准僅於申請日期範圍有效，延長須重新申請。[SRC-06] 這是合成教學草稿的流程說明，未提交、核准或啟用海外存取。

來源摘錄：

- [SRC-06: overseas-access-request.md](../updated-v2/raw/sources/overseas-access-request.md)

```text
- 申請人識別資訊。
- 目的地國家或地區。
- 預計開始日與結束日。
- 業務目的及需要遠端連線的工作範圍。

資料缺漏或日期不明時，服務台應退回補充或請申請人釐清，不應代填猜測。
```

- [SRC-06: overseas-access-request.md](../updated-v2/raw/sources/overseas-access-request.md)

```text
1. 申請人透過 ExampleDesk 提交資料。
2. 直屬主管檢視業務目的與日期並作出核准或拒絕。
3. 主管核准後，ExampleDesk 將申請轉交 Network Operations，並納入 Security Review。
4. 只有相關審查完成且獲准後，才可安排啟用；拒絕或待審時不得先行啟用。
5. 核准僅在申請所列日期範圍內有效，結束日到期後停止該次臨時安排；需要延長時須重新提出申請。
```

追問欄位：`start_date, end_date`

## SYN-10

問題：ExampleVPN 出現 DEMO-999，這是什麼原因、要怎麼修？

### 基準

`route: NO_ANSWER` · `first_action: RECORD_ERROR_AND_CONTACT_SERVICE_DESK`

本資料集未記錄 DEMO-999 的原因或修復步驟，因此無法據此診斷，也不能從其他代碼推定是密碼、網路或裝置授權問題。[SRC-02] 請保存不含機密的完整錯訊，記錄發生時間、裝置管理狀態及當時公司網路是否可用，交由服務台判讀；不要提供密碼或驗證碼。[SRC-01][SRC-02] 這表示目前證據不足，不表示其他資料來源必然沒有資訊；此回答未執行修復。

來源摘錄：

- [SRC-02: examplevpn-error-reference.md](../baseline-v1/raw/sources/examplevpn-error-reference.md)

```text
本表只涵蓋本教學案例已記錄的代碼。代碼描述是分流線索；須由使用者資訊或支援流程確認實際狀態。未列出的代碼沒有在此定義原因，請記錄原文並交由服務台判讀，不要自行推測。
```

- [SRC-01: vpn-common-qa.md](../baseline-v1/raw/sources/vpn-common-qa.md)

```text
先記錄使用者看到的完整訊息、發生時間、裝置管理狀態，以及當時是否可連公司網路。錯誤代碼只協助判斷方向，不能單獨證明帳戶、密碼或授權的狀態。
```

- [SRC-01: vpn-common-qa.md](../baseline-v1/raw/sources/vpn-common-qa.md)

```text
不要索取密碼或驗證碼。
```

### 更新後

`route: NO_ANSWER` · `first_action: ESCALATE_UNDOCUMENTED_ERROR`

本合成教學資料只記錄 DEMO-101、DEMO-202 與 DEMO-303，沒有記載 DEMO-999 的原因或修復方式，因此無法提供有依據的診斷或修復步驟，也不能從相鄰代碼推測是密碼、網路或裝置授權問題。[SRC-02] 建議保存不含機密的完整錯訊與發生情境，交由服務台判讀；目前未診斷或修復。這項限制只針對本次提供的證據，不表示其他資料來源也沒有相關資訊。[SRC-02]

來源摘錄：

- [SRC-02: examplevpn-error-reference.md](../updated-v2/raw/sources/examplevpn-error-reference.md)

```text
本表只涵蓋本教學案例已記錄的代碼。代碼描述是分流線索；須由使用者資訊或支援流程確認實際狀態。未列出的代碼沒有在此定義原因，請記錄原文並交由服務台判讀，不要自行推測。
```

- [SRC-02: examplevpn-error-reference.md](../updated-v2/raw/sources/examplevpn-error-reference.md)

```text
| DEMO-101 | 密碼輸入錯誤、已確認鎖定、密碼到期或網路狀況 | 先釐清狀態；代碼本身不代表帳戶鎖定。 |
| DEMO-202 | 裝置目前無法建立網路連線 | 確認一般網路可用，記錄所在網路與完整訊息；無法排除時交服務台。 |
| DEMO-303 | 裝置註冊或授權設定可能尚未完成 | 依 [SRC-04](managed-laptop-remote-access.md) 檢查公司管理裝置狀態；不可把所有登入失敗都視為授權問題。 |
```
