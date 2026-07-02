import random
import streamlit as st

# 1. Set up the page title and icon
st.set_page_config(page_title="Bestie AI", page_icon="💖", layout="centered")

# 2. Inject custom CSS for the Orange, Purple, and Pink theme
st.markdown("""
    <style>
    /* Gradient background for the whole app */
    .stApp {
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 50%, #a29bfe 100%);
    }
    
    /* Header styling */
    .main-title {
        color: #ff6b6b !important; /* Vibrant Orange-Pink */
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        text-align: center;
        font-size: 3rem;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 0px;
    }
    
    .subtitle {
        color: #6c5ce7 !important; /* Deep Purple */
        text-align: center;
        font-size: 1.2rem;
        margin-bottom: 30px;
    }
    
    /* User Chat Bubble (Orange) */
    .user-bubble {
        background-color: #ff8c00; 
        color: white;
        padding: 12px 18px;
        border-radius: 20px 20px 0px 20px;
        margin: 8px 0;
        text-align: right;
        max-width: 75%;
        float: right;
        clear: both;
        font-family: sans-serif;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
    }
    
    /* Bestie AI Chat Bubble (Pink/Purple) */
    .ai-bubble {
        background: linear-gradient(45deg, #d4418e, #6c5ce7);
        color: white;
        padding: 12px 18px;
        border-radius: 20px 20px 20px 0px;
        margin: 8px 0;
        text-align: left;
        max-width: 75%;
        float: left;
        clear: both;
        font-family: sans-serif;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
    }
    
    /* Custom Styling for the input box and button */
    .stButton>button {
        background: linear-gradient(45deg, #ff8c00, #d4418e, #6c5ce7) !important;
        color: white !important;
        border: none !important;
        padding: 10px 25px !important;
        border-radius: 15px !important;
        font-weight: bold !important;
        width: 100%;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.15);
    }
    
    .stButton>button:hover {
        transform: scale(1.02);
        transition: 0.2s;
    }
    </style>
""", unsafe_allow_html=True)

# 3. App Title UI
st.markdown('<p class="main-title">🌟 Bestie AI 🌟</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Your AI best friend, always here to hype you up!</p>', unsafe_allow_html=True)

# 4. Initialize chat history in session memory
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "ai", "content": "Hey bestie! 💕 How was your day? Tell me absolutely everything!"}
    ]

# 5. Display chat history with the custom themed bubbles
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="user-bubble">{msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="ai-bubble">{msg["content"]}</div>', unsafe_allow_html=True)

# Tiny spacer to prevent overlapping layout
st.write("<div style='clear: both; height: 20px;'></div>", unsafe_allow_html=True)

# 6. Chat Input Box Form
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Talk to your bestie...", placeholder="Omg you will not believe what just happened...")
    submit_button = st.form_submit_button(label="Send ✨")

# 7. Handle sending a message
if submit_button and user_input.strip() != "":
    # Save user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Fun, hype-filled "Bestie" responses
    bestie_responses = [
        "Omg NO WAY!! Tell me more right now! 😲🍿",
        "Literal icon behavior. We absolutely love to see it! 👑💖",
        "I am completely obsessed with that for you! ✨",
        "Don't even worry bestie, you've totally got this. I'm always in your corner! 🫂",
        "That is highly relatable honestly. What are we doing next? 💅🔥"
    ]
    
    # Pick a random bestie response
    ai_reply = random.choice(bestie_responses)
    st.session_state.messages.append({"role": "ai", "content": ai_reply})
    
    # Refresh the page instantly to show the new messages
    st.refresh() if hasattr(st, "refresh") else st.rerun()

