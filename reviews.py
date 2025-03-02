import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("AIML_API_KEY"),
)

def analyze_review(review_text):
    """Uses AI model API to analyze the sentiment of an ISP review."""
    try:
        response = client.chat.completions.create(
            model="deepseek/deepseek-chat",
            messages=[
                {"role": "system", "content": "You are an AI assistant who analyzes the sentiment of reviews."},
                {"role": "user", "content": f"Analyze the sentiment of this review: {review_text}"},
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# Test
if __name__ == "__main__":
    review = "The internet speed is terrible and unreliable!"
    print(analyze_review(review))