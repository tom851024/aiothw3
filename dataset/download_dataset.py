import os
import requests

def download_dataset():
    url = "https://raw.githubusercontent.com/PacktPublishing/Hands-On-Artificial-Intelligence-for-Cybersecurity/refs/heads/master/Chapter03/datasets/sms_spam_no_header.csv"
    save_path = "dataset/sms_spam_no_header.csv"

    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    print(f"Downloading dataset from {url}...")
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, "wb") as file:
            file.write(response.content)
        print(f"Dataset saved to {save_path}")
    else:
        print(f"Failed to download dataset. HTTP Status Code: {response.status_code}")

if __name__ == "__main__":
    download_dataset()