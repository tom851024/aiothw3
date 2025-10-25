## Why
垃圾郵件（Spam）對於用戶體驗與安全性造成威脅，建立一個基於機器學習的垃圾郵件分類器能有效減少此問題。

## What Changes
- Phase1: 建立基礎機器學習模型（SVM）作為 baseline，並從指定的公開數據集下載資料。
- Phase2: 基於垃圾郵件分類模型建立一個 Streamlit 網站，並參考 https://2025spamemail.streamlit.app/ 的排版進行設計與實作。
- PhaseN: 保留空白以便未來擴展。

**BREAKING**: 無（非破壞性新增）。

## Impact
- 新增 capability: `spam-classifier`。
- 新增資料目錄：`dataset/`。
- 影響範圍：無現有功能影響，為新增功能。

## Risks / Mitigations
- 風險：數據集下載失敗或格式不符。→ 緩解：在任務中加入數據檢查與格式化步驟。
- 風險：基礎模型準確率不足。→ 緩解：後續階段（PhaseN）將進行優化。

## Migration
- 無需遷移，為新增功能。

---

提出者: （請填入作者）
日期: （2025-10-25）
