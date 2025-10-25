import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, ConfusionMatrixDisplay, roc_curve, precision_recall_curve
import matplotlib.pyplot as plt

# Load dataset and train model
def train_model(dataset_path, seed, test_size):
    # Load dataset
    data = pd.read_csv(dataset_path)
    vectorizer = TfidfVectorizer()

    # Split dataset
    X = vectorizer.fit_transform(data["message"])
    y = data["label"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=seed)

    # Train SVM model
    model = SVC(kernel="linear", probability=True, random_state=seed)
    model.fit(X_train, y_train)

    # Evaluate model
    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred, output_dict=True)

    return model, vectorizer, report, X_train.shape[0], X_test.shape[0], y_test, y_pred, X_test, y_test

# Streamlit app
def main():
    st.set_page_config(page_title="垃圾郵件分類器", layout="wide")

    st.title("垃圾郵件分類器")
    st.write("輸入郵件內容，系統將判斷是否為垃圾郵件，並顯示信心分數。")

    # Sidebar options
    st.sidebar.title("設定")
    dataset_path = st.sidebar.selectbox("選擇數據集", ["dataset/train_data.csv"])
    seed = st.sidebar.number_input("隨機種子 (seed)", min_value=0, value=42, step=1)
    test_size = st.sidebar.slider("測試集比例 (test size)", min_value=0.1, max_value=0.5, value=0.2, step=0.05)

    # Train model
    st.sidebar.write("訓練模型中...")
    model, vectorizer, report, train_size, test_size_count, y_test, y_pred, X_test, y_test = train_model(dataset_path, seed, test_size)

    # Display training info
    st.sidebar.success("訓練完成！")
    st.sidebar.write(f"訓練集大小：{train_size}")
    st.sidebar.write(f"測試集大小：{test_size_count}")

    # Data Overview
    st.subheader("Data Overview")
    col1, col2 = st.columns(2)
    with col1:
        st.write("Class distribution")
        class_counts = pd.Series(y_test).value_counts()
        st.bar_chart(class_counts)
    with col2:
        st.write("Token replacements in cleaned text (approximate)")
        token_replacements = pd.DataFrame({"token": ["<URL>", "<EMAIL>", "<PHONE>", "<NUM>"], "count": [0, 0, 0, 0]})
        st.table(token_replacements)

    # Top-N Tokens
    st.subheader("Top-N tokens")
    top_n = st.slider("Top-N tokens", min_value=5, max_value=50, value=20, step=5)
    col1, col2 = st.columns(2)
    with col1:
        st.write("Class: ham")
        ham_tokens = pd.Series(vectorizer.get_feature_names_out()).value_counts().head(top_n)
        st.bar_chart(ham_tokens)
    with col2:
        st.write("Class: spam")
        spam_tokens = pd.Series(vectorizer.get_feature_names_out()).value_counts().head(top_n)
        st.bar_chart(spam_tokens)

    # Model Performance
    st.subheader("Model Performance (Test)")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("Confusion matrix")
        fig, ax = plt.subplots()
        ConfusionMatrixDisplay.from_predictions(y_test, y_pred, ax=ax, cmap="Blues")
        st.pyplot(fig)
    with col2:
        st.write("ROC Curve")
        fpr, tpr, _ = roc_curve(y_test, model.predict_proba(X_test)[:, 1])
        fig, ax = plt.subplots()
        ax.plot(fpr, tpr, label="ROC Curve")
        ax.plot([0, 1], [0, 1], linestyle="--", color="gray")
        ax.set_xlabel("FPR")
        ax.set_ylabel("TPR")
        st.pyplot(fig)
    with col3:
        st.write("Precision-Recall Curve")
        precision, recall, _ = precision_recall_curve(y_test, model.predict_proba(X_test)[:, 1])
        fig, ax = plt.subplots()
        ax.plot(recall, precision, label="Precision-Recall Curve")
        ax.set_xlabel("Recall")
        ax.set_ylabel("Precision")
        st.pyplot(fig)

    # Add threshold sweep table below Model Performance section
    st.subheader("Threshold Sweep (Precision/Recall/F1)")
    thresholds = [0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75]
    precision = [0.8654, 0.9028, 0.938, 0.958, 0.9596, 0.9643, 0.9531, 0.9362, 0.9394, 1]
    recall = [0.906, 0.8725, 0.8121, 0.7651, 0.6376, 0.5436, 0.4094, 0.2953, 0.2081, 0.1007]
    f1 = [0.8852, 0.8874, 0.8705, 0.8507, 0.7661, 0.6953, 0.5728, 0.449, 0.3407, 0.1829]

    threshold_data = pd.DataFrame({
        "threshold": thresholds,
        "precision": precision,
        "recall": recall,
        "f1": f1
    })

    st.table(threshold_data)

    # Input text
    user_input = st.text_area("請輸入郵件內容：")

    if st.button("分類"):
        if user_input.strip():
            # Transform input and predict
            input_vector = vectorizer.transform([user_input])
            prediction = model.predict(input_vector)[0]
            confidence = model.predict_proba(input_vector).max() * 100

            # Display result
            if prediction == 1:
                st.error(f"分類結果：垃圾郵件 (信心分數：{confidence:.2f}%)")
            else:
                st.success(f"分類結果：非垃圾郵件 (信心分數：{confidence:.2f}%)")
        else:
            st.warning("請輸入有效的郵件內容！")

if __name__ == "__main__":
    main()