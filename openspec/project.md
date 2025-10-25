# Project Context

## Purpose

## Tech Stack

## Project Conventions

### Code Style

### Architecture Patterns

### Testing Strategy

### Git Workflow

## Domain Context

## Important Constraints

## External Dependencies
# Project Context

## Purpose
本專案 (repo: `aiothw1`) 是為碩士物聯網作業而建立的一個範例與實作倉庫，目標是提供：
- 一個能模擬 IoT 裝置與後端通訊的參考實作
- 規範化的 OpenSpec 工作流程（提案、規格增量、實作與驗證）
- 可重複的測試與 CI 管線，方便教師與同學檢閱功能與變更

此文件描述專案的技術棧、程式與文件慣例、測試策略與重要限制，供開發者與 AI 助手（例如本專案的自動化代理）使用。

## Tech Stack (假設 & 建議)
- 語言：Python 3.10+（裝置模擬、測試腳本）
- 伺服器 / API：Node.js (Express) 或 Python (FastAPI)（視實作需求）
- 通訊：MQTT（mosquitto）或 HTTPS/REST（取決於實驗題目）
- 資料儲存：SQLite（本地測試）或簡單 JSON 檔案
- CI：GitHub Actions（或 GitLab CI）
- 測試：pytest（Python）或 jest（Node）
- 容器化（選用）：Docker

註：如果你的實際專案使用不同堆疊，請在此段落明確替換；我在不確定時採取寬鬆且常見的 IoT 教學堆疊。

## Project Conventions

### 檔案與字元編碼
- 所有原始檔與文件皆使用 UTF-8 編碼。
- 文件以繁體中文（zh-TW）為主，技術術語可採英文（例如 API 名稱、程式碼樣本）。

### Code Style
- Python：遵守 PEP8，使用 4 個空格縮排。建議安裝並使用 `black` 或 `ruff` 做統一格式化。
- JavaScript/TypeScript（若有）：遵守標準 ESLint 規則；使用 Prettier 做格式化。
- 變數與函式命名：採用 snake_case（Python）或 camelCase（JS/TS）。
- 範例提交訊息：遵循 Conventional Commits（例如 `feat: add ota update proposal`）。

### Architecture Patterns
- 單一儲存庫（monorepo-like）但以簡單模組劃分：`device/`（模擬器）、`server/`（API）、`tests/`（整合/單元測試）。
- 小型微服務或模組化：每個 capability 放在 `openspec/specs/<capability>/`。

### Testing Strategy
- 單元測試：每個函式/模組應該有對應的單元測試。
- 整合測試：模擬裝置與伺服器互動的整體流程測試（可以使用 pytest + asyncio 或 jest + supertest）。
- 規格驗證：每個 OpenSpec change 在合併前都應通過 `openspec validate <change-id> --strict`（手動或 CI）。

### Git Workflow
- Branching：feature 分支使用 `change/<change-id>` 或 `feature/<short-desc>`；修補分支使用 `fix/<short-desc>`。
- Pull Request：PR 標題請包含 change-id（若 PR 對應 OpenSpec 變更），並將 `openspec/changes/<change-id>/proposal.md` 加入 PR 描述或連結。
- Commit：使用 Conventional Commits 格式（`feat:`, `fix:`, `chore:` 等）。

## Domain Context
- 此倉庫聚焦 IoT 裝置與伺服端的通訊與管理，常見議題包括：裝置註冊、訊息上報 (telemetry)、指令下發、韌體更新 (OTA)、安全認證與錯誤復原。
- 優先解決教學與驗證易用性（清楚的 spec、可重現的測試），而非產業級可用性（例如多區容錯或超大量併發）。

## Important Constraints
- 作業限制：資源與時間有限，優先以簡潔、安全且易測試的設計為主。
- 隱私/資料：若處理真實使用者資料，遵守學校/實驗室的資料政策；示範資料建議使用合成資料。

## External Dependencies
- 典型外部系統：MQTT Broker（mosquitto）、公共套件註冊中心 (PyPI / npm)、CI Runner（GitHub Actions）。
- 若使用外部雲服務（AWS IoT, Azure IoT），在 `project.md` 明確列出並說明憑證/測試帳號管理方式。

## Contacts / Owners
- Repo owner: `tom851024` (GitHub)
- 作業聯絡人/教師: 請在此填入實際聯絡人 Email 或 Slack/Teams 頻道。

## Assumptions made by this file
- 我不確定實際程式語言與現有檔案結構，故採用一個常見的 IoT 教學堆疊（Python + Node.js + MQTT）與工具（pytest、GitHub Actions）。
- 若你的專案已有不同決定，請告訴我，我會根據實際堆疊調整本文件與後續 proposal。

---

若要我直接把這些慣例套入程式碼檢查、CI 範本或建立更詳細的實作任務（例如一個 CI workflow 或 `Dockerfile`），請告訴我你希望的技術選擇，我會在下一步為你建立。
