import streamlit as st
import pandas as pd
import random
import time
import requests

# Function to load Lottie animations (optional, if you still want to use JSON data in future)
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Set page config
st.set_page_config(page_title="EdgeWise Content Moderation", page_icon="🤖", layout="wide")

# Custom CSS for black background text area with white text
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stTextInput > div > div > input {
        background-color: #ffffff;
    }
    .stTextArea > div > div > textarea {
        background-color: #000000;
        color: #ffffff;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("EdgeWise")
    # Optional: Add a static image or remove the animation
    st.image("https://via.placeholder.com/200", caption="Content Moderation Bot")
    st.write("---")
    st.write("This application is designed for content moderation and works best with local deployment.")
    st.write("[GitHub Repository](https://github.com/Ashar086/EdgeWise)")

# Main content
st.title("Edge Device Content Moderation Bot 🤖")

# Load the CSV to get the sentiment classes
@st.cache_data
def load_data():
    filename = "synData.csv"
    df = pd.read_csv(filename, names=["sentiment", "text"], encoding="utf-8", encoding_errors="replace")
    return df

df = load_data()

# Get unique sentiments from the CSV file
sentiments = sorted(df.sentiment.unique())

# Display sentiment categories
st.write("### Detectable Text Categories:")
cols = st.columns(4)
for i, sentiment in enumerate(sentiments):
    cols[i % 4].write(f"- {sentiment}")

st.write("---")

# User input with black background and white text
user_input = st.text_area("Enter text to analyze:", height=150)

if st.button("Analyze Sentiment"):
    if user_input:
        with st.spinner("Analyzing sentiment..."):
            # Simulate analysis with a progress bar
            progress_bar = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                progress_bar.progress(i + 1)
            
            # Simulate a random response
            sentiment_detected = random.choice(sentiments)
            
            # Display the result
            st.write("---")
            col1, col2 = st.columns([1, 2])
            with col1:
                # Optional: Add a static image instead of animation
                st.image("https://via.placeholder.com/200", caption="Analysis in Progress")
            with col2:
                st.write("## Analysis Result")
                st.write(f"Detected text category: **{sentiment_detected}**")
                st.info("This is a simulated response. The actual analysis is best performed locally for privacy and efficiency.")
    else:
        st.warning("Please enter some text to analyze.")

# Footer
st.write("---")
st.write("EdgeWise Content Moderation Bot - Powered by AI")

