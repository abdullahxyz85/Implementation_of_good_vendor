import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("AIML_API_KEY"),
)

def get_isp_data(latitude, longitude):
    """Uses AI model API to fetch ISP data based on latitude and longitude."""
    try:
        response = client.chat.completions.create(
            model="deepseek/deepseek-chat",
            messages=[
                {"role": "system", "content": "You are an AI assistant who provides ISP data based on location."},
                {"role": "user", "content": f"Provide ISP data for latitude={latitude}, longitude={longitude}."},
            ],
        )
        isp_data = response.choices[0].message.content
        return isp_data
    except Exception as e:
        return {"error": f"Failed to fetch ISP data: {str(e)}"}

# Test
if __name__ == "__main__":
    print(get_isp_data(40.7128, -74.0060))  # Example for New York