import os
import openai
import networkx as nx
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
from geopy.geocoders import Nominatim
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("AIML_API_KEY")  # Using AI model API

def get_location_ai(address):
    """Uses AI model API for geolocation extraction."""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a geolocation AI. Return lat/lng for a location."},
            {"role": "user", "content": f"Find latitude and longitude of {address}."}
        ]
    )

    ai_result = response["choices"][0]["message"]["content"]
    
    try:
        lat, lng = map(float, ai_result.strip().split(","))
        return lat, lng
    except ValueError:
        return None

# Graph-Based Location Tracking
G = nx.Graph()

def add_location_to_graph(address):
    """Adds a location node to the graph."""
    geolocator = Nominatim(user_agent="geo_app")
    location = geolocator.geocode(address)
    
    if location:
        G.add_node(address, pos=(location.longitude, location.latitude))
        return location.latitude, location.longitude
    return None

def show_map():
    """Visualizes locations on a network graph & map."""
    pos = nx.get_node_attributes(G, "pos")
    df = pd.DataFrame(pos).T.reset_index()
    df.columns = ["Location", "Longitude", "Latitude"]

    fig = px.scatter_geo(df, lat="Latitude", lon="Longitude", text="Location",
                         title="AI-Based Geolocation Map", projection="natural earth")
    fig.show()

    # Matplotlib Graph
    plt.figure(figsize=(8, 5))
    nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray", node_size=1000, font_size=10)
    plt.title("📍 Location Graph Network")
    plt.show()
