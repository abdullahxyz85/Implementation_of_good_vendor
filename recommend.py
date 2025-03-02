import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("AIML_API_KEY"),
)

def recommend_isp(speed, reliability, budget):
    """Uses AI model API to suggest the best ISP based on user preferences."""
    try:
        response = client.chat.completions.create(
            model="deepseek/deepseek-chat",
            messages=[
                {"role": "system", "content": "You are an AI assistant who recommends ISPs based on user preferences."},
                {"role": "user", "content": f"Recommend an ISP with speed={speed} Mbps, reliability={reliability}%, and budget=${budget}."},
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# Test
if __name__ == "__main__":
    print(recommend_isp(100, 90, 50))