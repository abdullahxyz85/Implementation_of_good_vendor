import requests
import os
from dotenv import load_dotenv

load_dotenv()

AIML_API_KEY = os.getenv("AIML_API_KEY")
BASE_URL = os.getenv("BASE_URL")

def ai_chatbot(user_query):
    """Uses AIML API to provide AI-powered answers for ISP-related queries."""
    url = f"{BASE_URL}/chatbot"
    headers = {"Authorization": f"Bearer {AIML_API_KEY}", "Content-Type": "application/json"}
    data = {"query": user_query}
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        answer = response.json().get("response", "Sorry, I couldn't find an answer.")
        return answer
    else:
        return f"Error: {response.json()}"

# Test
if __name__ == "__main__":
    print(ai_chatbot("Which ISP is best for gaming?"))
