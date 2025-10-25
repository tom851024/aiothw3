import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report


def train_and_evaluate():
    train_path = "dataset/train_data.csv"
    test_path = "dataset/test_data.csv"

    print(f"Loading training data from {train_path}...")
    train_data = pd.read_csv(train_path)
    print(f"Loading testing data from {test_path}...")
    test_data = pd.read_csv(test_path)

    # Vectorize text data
    vectorizer = TfidfVectorizer()
    print("Vectorizing training data...")
    X_train = vectorizer.fit_transform(train_data["message"])
    y_train = train_data["label"]

    print("Vectorizing testing data...")
    X_test = vectorizer.transform(test_data["message"])
    y_test = test_data["label"]

    # Train SVM model
    print("Training SVM model...")
    model = SVC(kernel="linear", random_state=42)
    model.fit(X_train, y_train)

    # Evaluate model
    print("Evaluating model...")
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.2f}")
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

    print("Training and evaluation complete.")

if __name__ == "__main__":
    train_and_evaluate()