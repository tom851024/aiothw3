## ADDED Requirements

### Requirement: OTA Firmware Update
系統 SHALL 支援遠端韌體 (firmware) 的發布與裝置端更新機制。

#### Scenario: Upload new firmware to server
- **WHEN** 開發者（或運維）透過受控 API/管理介面上傳一個新的韌體版本（包含 metadata：version、signature、manifest）
- **THEN** 伺服器應驗證上傳內容的完整性與簽章，並將該版本標記為可供選擇的更新。

#### Scenario: Device checks for update and downloads
- **WHEN** 裝置定期或被觸發檢查是否有新版本可用（例如透過 MQTT topic 或 HTTP poll）
- **THEN** 若有新版本且符合更新條件（版本較新、簽章正確），裝置 SHALL 能下載韌體檔案（支援分段或 resumable 下載視實作而定）。

#### Scenario: Device verifies and applies update
- **WHEN** 裝置完成韌體下載
- **THEN** 裝置 SHALL 驗證簽章與完整性；驗證成功後，裝置 SHALL 在安全模式下應用更新並回報結果（成功/失敗與失敗原因）。

#### Scenario: Rollback on failure
- **WHEN** 更新失敗或驗證不通過
- **THEN** 裝置 SHALL 保持原有韌體或回滾到先前可用版本，並將失敗狀態回報至伺服器以便分析。

#### Scenario: Reporting update status
- **WHEN** 裝置完成下載/安裝/重啟流程
- **THEN** 裝置 SHALL 回報最終狀態（成功/失敗、版本、日誌片段）到指定 endpoint 或 topic，伺服器 SHALL 記錄該狀態。
