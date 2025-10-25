## Why
目前系統缺乏集中或遠端更新裝置韌體（OTA）的能力。為了支援教學與真實場景測試，我們需要一個清晰、可測試且安全的 OTA 流程。

## What Changes
- 新增 OTA 能力的規格增量（`specs/firmware/spec.md`），描述韌體上傳、驗證、下發與回報行為。
- 在實作層面新增伺服端 API（或 MQTT topic）以支持上傳、分發與裝置回報。
- 新增 tasks.md 詳列實作步驟與測試案例。

**BREAKING**: 無（非破壞性新增）

## Impact
- 受影響的 capability: `firmware`（新增）
- 受影響的代碼區域: 可能在 `server/`、`device/` 與 `tests/` 中增加新檔案或 endpoint。
- 對現有行為的影響: 主要為新增功能，已存在的 telemetry 與控制流程不變。

## Risks / Mitigations
- 風險：不當的簽章或驗證導致惡意韌體下發。 → 緩解：在 spec 中要求韌體簽章與版本檢查。
- 風險：大量裝置同時更新可能造成伺服器負載。 → 緩解：在實作 tasks 中建議採用分批更新策略（rolling update）。

## Migration
- 無需既有資料遷移。測試環境可直接部署新端點並透過模擬器驗證更新流程。

---

提出者: （請填入作者）
日期: （YYYY-MM-DD）