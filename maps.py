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
        # Assuming the response is a string like "lat, lng"
        lat_lng = response.choices[0].message.content.split(", ")
        return float(lat_lng[0]), float(lat_lng[1])  # Ensure it returns two float values
    except Exception as e:
        return None  # Or handle the error appropriately

def add_location_to_graph(address):
    # Implementation for adding location to graph
    pass

def show_map():
    # Implementation for showing the map
    pass