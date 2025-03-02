import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("AIML_API_KEY"),
)

def get_location_ai(address):
    """Uses AI model API for geolocation extraction."""
    try:
        response = client.chat.completions.create(
            model="deepseek/deepseek-chat",
            messages=[
                {"role": "system", "content": "You are an AI assistant who extracts latitude and longitude from addresses."},
                {"role": "user", "content": f"Find latitude and longitude of {address}."},
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

def add_location_to_graph(address):
    # Implementation for adding location to graph
    pass

def show_map():
    # Implementation for showing the map
    pass