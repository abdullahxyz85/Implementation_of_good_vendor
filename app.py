import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
from reviews import analyze_review
from compare import compare_isps
from accessories import get_accessories
from recommend import recommend_isp
from chatbot import ai_chatbot
from maps import get_location_ai, add_location_to_graph, show_map

# Set page configuration as the first command
st.set_page_config(page_title="AI-Powered Vendor", layout="wide")

def load_css():
    """Load custom CSS for styling."""
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# App Title and Description
st.title("🚀 Internet Service Provider Analyzer Pro")
st.markdown("Welcome to the Internet Service Provider Analyzer! Here you can find ISPs, compare them, run speed tests, analyze reviews, and more.")

# Sidebar content

# Back to Home Button at the top of the sidebar
st.sidebar.markdown("[Back to Home](https://quiet-bombolone-790733.netlify.app/)", unsafe_allow_html=True)
# Advanced AI & ML Integration message at the top
st.sidebar.markdown("### 📢 Advanced AI & ML Integration Enabled! 🚀")

# Select Feature Section
st.sidebar.markdown("### 🔧 Select Feature")
menu = [
    "Compare ISPs", 
    "AI Reviews", 
    "AI ISP Recommendation", 
    "AI Chatbot", 
    "Accessories Store", 
    "ISP Analytics"
]
choice = st.sidebar.selectbox("", menu)

# Sidebar content
# Advanced AI & ML Integration message at the top
st.sidebar.markdown("### 📊 Project Overview")
st.sidebar.markdown("""
This project is designed to help users find and compare Internet Service Providers (ISPs) using AI and machine learning techniques. 
You can also run speed tests, analyze reviews, and get recommendations based on your preferences.
""")

# Add icons (you can use any icon library or images)
st.sidebar.markdown("### 🚀 Features")
st.sidebar.markdown("""
- **Compare ISPs**: Compare different ISPs based on various metrics.
- **AI Reviews**: Analyze reviews using AI.
- **AI ISP Recommendation**: Get personalized ISP recommendations.
- **AI Chatbot**: Interact with an AI-powered chatbot for assistance.
- **Accessories Store**: Browse wireless accessories.
- **ISP Analytics**: Analyze ISP performance metrics.
""")
# Feature: AI Chatbot
if choice == "AI Chatbot":
    st.subheader("🤖 AI-Powered Chatbot")
    user_query = st.text_area("Ask the AI Chatbot", placeholder="Type your question here...")
    if st.button("Ask"):
        response = ai_chatbot(user_query)
        st.success(f"🗨 Chatbot Response: {response}")



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


elif choice == "Compare ISPs":
    st.subheader("📊 ISP Comparison")
    isp_data = compare_isps()
    st.dataframe(isp_data)

# Feature: Accessories Store
elif choice == "Accessories Store":
    st.subheader("🛍 Wireless Accessories Store")
    accessories = get_accessories()
    for item, details in accessories.items():
        st.write(f"📌 **{item}**")
        st.write(f"  - **Price**: {details['price']}")
        st.write(f"  - **Brand**: {details['brand']}")
        st.write(f"  - **Description**: {details['description']}")
        st.write(f"  - **Rating**: {details['rating']} ⭐")
        st.write(f"  - **Availability**: {details['availability']}")
        st.write("  - **Specifications**:")
        for key, value in details['specifications'].items():
            st.write(f"    - **{key}**: {value}")
        st.write("  - **Features**:")
        for feature in details['features']:
            st.write(f"    - {feature}")
        st.write(f"  - **Warranty**: {details['warranty']}")
        st.write("  - **Customer Reviews**:")
        for review in details['customer_reviews']:
            st.write(f"    - **User**: {review['user']}, **Rating**: {review['rating']}, **Comment**: {review['comment']}")
        st.write(f"  - **Image**: [View Image]({details['image_url']})")
        st.write("---")


# Feature: ISP Analytics
elif choice == "ISP Analytics":
    st.subheader("📈 ISP Performance Analytics")

    # Sample Data for ISP Speeds
    isp_names = ["ISP A", "ISP B", "ISP C", "ISP D"]
    download_speeds = [150, 200, 170, 220]  # Mbps
    upload_speeds = [50, 60, 55, 65]  # Mbps
    customer_satisfaction = {
        "ISP A": [4.5, 4.7, 4.6, 4.8],
        "ISP B": [4.0, 4.1, 4.2, 4.0],
        "ISP C": [4.2, 4.3, 4.1, 4.4],
        "ISP D": [4.8, 4.9, 4.7, 5.0],
    }
    latency = [20, 30, 25, 15]  # ms

    # Bar Chart for Download vs Upload Speeds
    st.subheader("Download vs Upload Speeds")
    fig1, ax1 = plt.subplots()
    ax1.bar(isp_names, download_speeds, color='skyblue', label='Download Speed')
    ax1.bar(isp_names, upload_speeds, color='orange', label='Upload Speed', alpha=0.7)
    ax1.set_ylabel("Speed (Mbps)")
    ax1.set_title("ISP Download vs Upload Speeds")
    ax1.legend()
    st.pyplot(fig1)

    # Pie Chart for Customer Satisfaction
    st.subheader("Customer Satisfaction Ratings")
    fig2, ax2 = plt.subplots()
    ax2.pie([sum(ratings) / len(ratings) for ratings in customer_satisfaction.values()], labels=isp_names, autopct='%1.1f%%', startangle=90)
    ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig2)

    # Line Chart for Latency
    st.subheader("ISP Latency Over Time")
    time_period = ["Week 1", "Week 2", "Week 3", "Week 4"]
    fig3, ax3 = plt.subplots()
    ax3.plot(time_period, latency, marker='o', color='purple', label='Latency (ms)')
    ax3.set_ylabel("Latency (ms)")
    ax3.set_title("ISP Latency Over Time")
    ax3.legend()
    st.pyplot(fig3)

    # Scatter Plot for Download vs Customer Satisfaction
    st.subheader("Download Speed vs Customer Satisfaction")
    fig4, ax4 = plt.subplots()
    ax4.scatter(download_speeds, [sum(ratings) / len(ratings) for ratings in customer_satisfaction.values()], color='green')
    ax4.set_xlabel("Download Speed (Mbps)")
    ax4.set_ylabel("Customer Satisfaction (Rating)")
    ax4.set_title("Download Speed vs Customer Satisfaction")
    st.pyplot(fig4)

    # Box Plot for ISP Ratings
    st.subheader("Box Plot of Customer Ratings")
    fig5, ax5 = plt.subplots()
    ax5.boxplot(list(customer_satisfaction.values()), labels=isp_names)
    ax5.set_ylabel("Customer Satisfaction (Rating)")
    ax5.set_title("Box Plot of Customer Ratings")
    st.pyplot(fig5)

    # Add some styling
    st.markdown("""
    <style>
    .stSubheader {
        color: #1E90FF;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)