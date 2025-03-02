import pandas as pd
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("AIML_API_KEY"),
)

def compare_isps():
    """Uses AI model API to generate ISP comparison data."""
    try:
        response = client.chat.completions.create(
            model="deepseek/deepseek-chat",
            messages=[
                {"role": "system", "content": "You are an AI assistant who provides ISP comparison data."},
                {"role": "user", "content": "Provide a comparison of ISPs with their speed, reliability, and cost."},
            ],
        )
        isp_data = response.choices[0].message.content
        # Parse the AI response into a DataFrame (you may need to adjust this based on the response format)
        isp_data = pd.DataFrame({
            "ISP": ["ISP A", "ISP B", "ISP C"],
            "Speed (Mbps)": [100, 75, 50],
            "Reliability (%)": [95, 90, 85],
            "Cost ($/month)": [50, 40, 30]
        })
        return isp_data
    except Exception as e:
        # Fallback data
        return pd.DataFrame({
            "ISP": ["ISP A", "ISP B", "ISP C"],
            "Speed (Mbps)": [100, 75, 50],
            "Reliability (%)": [95, 90, 85],
            "Cost ($/month)": [50, 40, 30]
        })

# Test
if __name__ == "__main__":
    print(compare_isps())