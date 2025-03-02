import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Debug: Print environment variables
print("BASE_URL:", os.getenv("BASE_URL"))
print("AIML_API_KEY:", os.getenv("AIML_API_KEY"))

# Initialize the OpenAI client
client = OpenAI(
    base_url=os.getenv("BASE_URL"),  # Ensure this includes the schema (e.g., https://)
    api_key=os.getenv("AIML_API_KEY"),
)

def ai_chatbot(user_query):
    """Uses AI model API to provide AI-powered answers for ISP-related queries."""
    try:
        response = client.chat.completions.create(
            model="deepseek/deepseek-chat",  # Replace with your model name
            messages=[
                {"role": "system", "content": "You are an AI assistant who knows everything about ISPs."},
                {"role": "user", "content": user_query},
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# Test
if __name__ == "__main__":
    print(ai_chatbot("Which ISP is best for gaming?"))