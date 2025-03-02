import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load API keys from .env file

AIML_API_KEY = os.getenv("AIML_API_KEY")
BASE_URL = os.getenv("BASE_URL")

def recommend_isp(speed, reliability, budget):
    """Uses AIML API to suggest the best ISP based on user preferences."""
    url = f"{BASE_URL}/isp-recommendation"
    headers = {"Authorization": f"Bearer {AIML_API_KEY}", "Content-Type": "application/json"}
    data = {"speed": speed, "reliability": reliability, "budget": budget}
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        recommendation = response.json().get("recommended_isp", "No recommendation available")
        return recommendation
    else:
        return f"Error: {response.json()}"

# Test
if __name__ == "__main__":
    print(recommend_isp(100, 90, 50))
