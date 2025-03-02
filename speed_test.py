import speedtest
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("AIML_API_KEY"),
)

def check_speed():
    """Measures internet speed and provides AI-based insights."""
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1e6  # Convert to Mbps
    upload_speed = st.upload() / 1e6  # Convert to Mbps

    try:
        response = client.chat.completions.create(
            model="deepseek/deepseek-chat",
            messages=[
                {"role": "system", "content": "You are an AI assistant who provides insights on internet speed test results."},
                {"role": "user", "content": f"My download speed is {download_speed} Mbps, and my upload speed is {upload_speed} Mbps. Provide insights."},
            ],
        )
        insights = response.choices[0].message.content
        return download_speed, upload_speed, insights
    except Exception as e:
        return download_speed, upload_speed, "No insights available."

# Test
if __name__ == "__main__":
    download, upload, insights = check_speed()
    print(f"Download: {download} Mbps | Upload: {upload} Mbps")
    print(f"Insights: {insights}")