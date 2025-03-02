import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load API keys from .env file

AIML_API_KEY = os.getenv("AIML_API_KEY")
BASE_URL = os.getenv("BASE_URL")

def analyze_review(review_text):
    """Uses AIML API to analyze the sentiment of an ISP review."""
    url = f"{BASE_URL}/sentiment"
    headers = {"Authorization": f"Bearer {AIML_API_KEY}", "Content-Type": "application/json"}
    data = {"text": review_text}
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        sentiment = response.json().get("sentiment", "Unknown")
        return sentiment
    else:
        return f"Error: {response.json()}"

# Test
if __name__ == "__main__":
    review = "The internet speed is terrible and unreliable!"
    print(analyze_review(review))
