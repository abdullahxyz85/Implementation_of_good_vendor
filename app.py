import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
from isp_data import get_isp_data
from reviews import analyze_review
from compare import compare_isps
from speed_test import check_speed
from accessories import get_accessories
from recommend import recommend_isp
from chatbot import ai_chatbot
from maps import get_location_ai, add_location_to_graph, show_map

# Set page configuration as the first command
st.set_page_config(page_title="AI-Powered ISP Analyzer", layout="wide")

def load_css():
    """Load custom CSS for styling."""
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# App Title and Description
st.title("🚀 AI-Powered ISP Analyzer Platform")
st.markdown("Welcome to the AI-Powered ISP Analyzer! Here you can find ISPs, compare them, run speed tests, analyze reviews, and more.")

# Sidebar Menu
menu = [
    "Find ISPs", "Compare ISPs", "Speed Test", "AI Reviews", 
    "AI ISP Recommendation", "AI Chatbot", "Accessories Store", "AI Map", "ISP Analytics"
]
choice = st.sidebar.selectbox("📌 Select Feature", menu)

# Feature: Find ISPs
if choice == "Find ISPs":
    st.subheader("📍 Find Available ISPs Near You")
    address = st.text_input("Enter Address", placeholder="e.g., 123 Main St, City, Country")
    
    if st.button("Search ISP"):
        lat_lng = get_location_ai(address)
        if lat_lng:
            lat, lng = lat_lng
            st.success(f"✅ AI Found: {address} → Latitude: {lat}, Longitude: {lng}")
            add_location_to_graph(address)
            show_map()
        else:
            st.error("❌ AI could not determine the location.")

# Feature: Compare ISPs
elif choice == "Compare ISPs":
    st.subheader("📊 ISP Comparison")
    isp_data = compare_isps()
    st.dataframe(isp_data)

# Feature: Speed Test
elif choice == "Speed Test":
    st.subheader("🚀 Run Speed Test")
    if st.button("Start Speed Test"):
        download, upload, insights = check_speed()
        st.success(f"📡 Download: {download} Mbps | Upload: {upload} Mbps")
        st.info(f"💡 Insights: {insights}")

# Feature: AI Reviews
elif choice == "AI Reviews":
    st.subheader("💬 AI-Powered Review Sentiment Analysis")
    review_text = st.text_area("Enter your review", placeholder="Type your review here...")
    if st.button("Analyze Review"):
        sentiment = analyze_review(review_text)
        st.success(f"📝 Sentiment Analysis Result: {sentiment}")

# Feature: AI ISP Recommendation
elif choice == "AI ISP Recommendation":
    st.subheader("🤖 AI-Generated ISP Recommendation")
    speed = st.slider("Preferred Speed (Mbps)", 10, 1000, 100)
    reliability = st.slider("Reliability (%)", 50, 100, 90)
    budget = st.slider("Budget ($)", 10, 200, 50)
    if st.button("Get Recommendation"):
        recommendation = recommend_isp(speed, reliability, budget)
        st.success(f"🔍 Recommended ISP: {recommendation}")

# Feature: AI Chatbot
elif choice == "AI Chatbot":
    st.subheader("🤖 AI-Powered Chatbot")
    user_query = st.text_area("Ask the AI Chatbot", placeholder="Type your question here...")
    if st.button("Ask"):
        response = ai_chatbot(user_query)
        st.success(f"🗨 Chatbot Response: {response}")

# Feature: Accessories Store
elif choice == "Accessories Store":
    st.subheader("🛍 Wireless Accessories Store")
    accessories = get_accessories()
    for item, price in accessories.items():
        st.write(f"📌 {item} - ${price}")

# Feature: AI Map
elif choice == "AI Map":
    st.subheader("🌍 AI-Powered Geolocation Map")
    show_map()

# Feature: ISP Analytics
elif choice == "ISP Analytics":
    st.subheader("📈 ISP Performance Analytics")
    # Sample Data for ISP Speeds
    isp_names = ["ISP A", "ISP B", "ISP C", "ISP D"]
    download_speeds = [150, 200, 170, 220]  # Mbps
    upload_speeds = [50, 60, 55, 65]  # Mbps

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(isp_names, download_speeds, color='skyblue', label='Download Speed')
    ax.bar(isp_names, upload_speeds, color='orange', label='Upload Speed', alpha=0.7)
    ax.set_ylabel("Speed (Mbps)")
    ax.set_title("ISP Download vs Upload Speeds")
    ax.legend()
    
    st.pyplot(fig)

# Sidebar Footer
st.sidebar.markdown("📢 **Advanced AI & ML Integration Enabled!** 🚀")
st.sidebar.markdown("### 📊 Project Overview")
st.sidebar.markdown("""
This project is designed to help users find and compare Internet Service Providers (ISPs) using AI and machine learning techniques. 
You can also run speed tests, analyze reviews, and get recommendations based on your preferences.
""")
st.sidebar.markdown("### 🚀 Features")
st.sidebar.markdown("""
- **Find ISPs**: Search for available ISPs in your area.
- **Compare ISPs**: Compare different ISPs based on various metrics.
- **Speed Test**: Check your internet speed.
- **AI Reviews**: Analyze reviews using AI.
- **AI ISP Recommendation**: Get personalized ISP recommendations.
- **AI Chatbot**: Interact with an AI-powered chatbot for assistance.
- **Accessories Store**: Browse wireless accessories.
- **AI Map**: Visualize geolocation data.
- **ISP Analytics**: Analyze ISP performance metrics.
""")