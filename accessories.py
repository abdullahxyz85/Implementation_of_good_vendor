import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("AIML_API_KEY"),
)

def get_accessories():
    """Uses AI model API to generate a list of wireless accessories."""
    try:
        response = client.chat.completions.create(
            model="deepseek/deepseek-chat",
            messages=[
                {"role": "system", "content": "You are an AI assistant who provides a list of wireless accessories."},
                {"role": "user", "content": "Provide a list of wireless accessories with their prices."},
            ],
        )
        accessories = response.choices[0].message.content
        return accessories
    except Exception as e:
        return {"Router A": "$50", "WiFi Adapter B": "$20", "Mesh System C": "$100"}  # Fallback data

# Test
if __name__ == "__main__":
    print(get_accessories())