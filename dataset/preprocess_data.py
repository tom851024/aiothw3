import pandas as pd
from sklearn.model_selection import train_test_split

def preprocess_data():
    input_path = "dataset/sms_spam_no_header.csv"
    output_train = "dataset/train_data.csv"
    output_test = "dataset/test_data.csv"

    print(f"Loading dataset from {input_path}...")
    data = pd.read_csv(input_path, names=["label", "message"], encoding="latin-1")

    # Map labels to binary values
    data["label"] = data["label"].map({"ham": 0, "spam": 1})

    print("Splitting dataset into training and testing sets...")
    train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

    print(f"Saving training data to {output_train}...")
    train_data.to_csv(output_train, index=False)

    print(f"Saving testing data to {output_test}...")
    test_data.to_csv(output_test, index=False)

    print("Preprocessing complete.")

if __name__ == "__main__":
    preprocess_data()