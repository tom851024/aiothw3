## ADDED Requirements

### Requirement: Spam Classifier Baseline
系統 SHALL 支援基於機器學習的垃圾郵件分類器，並提供基礎模型作為 baseline。

#### Scenario: Download and preprocess dataset
- **WHEN** 開發者執行數據下載腳本
- **THEN** 系統 SHALL 從指定的 URL 下載數據集，並將其存放於 `dataset/` 資料夾中。

#### Scenario: Train baseline SVM model
- **WHEN** 開發者執行模型訓練腳本
- **THEN** 系統 SHALL 使用 SVM 模型進行訓練，並輸出準確率與性能指標。

#### Scenario: Placeholder for PhaseN
- **WHEN** 未來擴展需求被定義
- **THEN** 系統 SHALL 支援新增的功能與場景。

### Requirement: Streamlit Web Interface
系統 SHALL 提供一個基於 Streamlit 的網站，允許用戶輸入郵件內容並查看分類結果。

#### Scenario: User inputs email content
- **WHEN** 用戶在網站的輸入框中輸入郵件內容
- **THEN** 系統 SHALL 使用垃圾郵件分類模型進行分類，並顯示結果（垃圾郵件/非垃圾郵件）。

#### Scenario: Display classification result
- **WHEN** 分類完成後
- **THEN** 系統 SHALL 在網站上顯示分類結果，並提供信心分數（confidence score）。
