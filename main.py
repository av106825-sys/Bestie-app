import streamlit as st

# --- 1. INITIALIZE GLOBAL STORAGE (SESSION STATE) ---
if "page" not in st.session_state:
    st.session_state.page = "login"

# This holds every single app created on your platform dynamically!
if "apps" not in st.session_state:
    st.session_state.apps = {
        "Dance queen": {
            "code": "import tkinter as tk\n# Dance Queen App Core Code\nprint('Welcome to the Dance Studio!')",
            "edit_requests": ["Make an app that could make messages", "It could make groups"]
        },
        "Yoga master": {
            "code": "import tkinter as tk\n# Yoga Master App Core Code\nprint('Time to stretch and relax!')",
            "edit_requests": ["Add a daily timer feature"]
        }
    }

if "current_app" not in st.session_state:
    st.session_state.current_app = "Dance queen"
if "selected_chat_option" not in st.session_state:
    st.session_state.selected_chat_option = "Both"


# --- 2. ADVANCED CSS STYLING TO MATCH MOCKUPS ---
st.markdown("""
    <style>
    /* Main Background color */
    .stApp {
        background-color: #E8A7F5 !important;
    }
    
    /* Typography & Branding Colors */
    h1, h2, h3, p, label, .stMarkdown {
        color: #FF2E93 !important;
        font-family: 'Arial Rounded MT Bold', sans-serif;
        font-weight: bold;
    }
    
    /* White Input Containers */
    div.stTextArea textarea, div.stTextInput input {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border-radius: 20px !important;
        border: none !important;
        padding: 15px !important;
    }
    
    /* Custom White Card Box style */
    .white-card {
        background-color: #FFFFFF !important;
        border-radius: 25px !important;
        padding: 30px !important;
        text-align: center !important;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    }
    
    /* Global Button Customization */
    div.stButton > button {
        background-color: #FFFFFF !important;
        color: #FF2E93 !important;
        border-radius: 25px !important;
        border: 2px solid #FF2E93 !important;
        font-weight: bold !important;
        padding: 10px 25px !important;
        font-size: 16px !important;
    }
    div.stButton > button:hover {
        background-color: #FF2E93 !important;
        color: #FFFFFF !important;
    }
    
    /* Speech Bubbles Setup */
    .chat-bubble {
        background-color: #FFFFFF;
        color: #000000 !important;
        padding: 12px;
        border-radius: 15px;
        margin-bottom: 8px;
        border: 2px solid #000000;
        font-family: sans-serif;
    }
    
    /* Code View Window Block Styling */
    .code-box {
        background-color: #222222 !important;
        color: #00FF00 !important;
        font-family: monospace !important;
        padding: 15px;
        border-radius: 10px;
        overflow-x: auto;
    }
    </style>
""", unsafe-allow_html=True)


# ==========================================================
# PAGE 1: LOGIN SCREEN (Matches Mockup 1)
# ==========================================================
if st.session_state.page == "login":
    st.markdown("<h1 style='text-align: center; font-size: 70px; margin-bottom:
