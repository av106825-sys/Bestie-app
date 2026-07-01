import streamlit as st

# --- 1. INITIALIZE SYSTEM MEMORY (SESSION STATE) ---
if "page" not in st.session_state:
    st.session_state.page = "login"
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"sender": "client", "text": "Make an app that could make messages"},
        {"sender": "developer", "text": "Ok I'll make an app that could make messages"},
        {"sender": "client", "text": "It could make groups"}
    ]
if "selected_chat_option" not in st.session_state:
    st.session_state.selected_chat_option = "Both"
if "app_ideas" not in st.session_state:
    st.session_state.app_ideas = []
if "current_editing_app" not in st.session_state:
    st.session_state.current_editing_app = "Dance queen"
if "apps_list" not in st.session_state:
    st.session_state.apps_list = ["Dance queen", "Yoga master"]
if "app_code" not in st.session_state:
    st.session_state.app_code = """import tkinter as tk
from tkinter import filedialog

def open_file():
    \"\"\"Open a file for editing.\"\"\"
    filepath = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    text_edit.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
    text_edit.insert(tk.END, text)
    window.title(f"Simple Text App - {filepath}")"""

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
    .bubble-client {
        background-color: #FFFFFF;
        color: #000000 !important;
        padding: 12px;
        border-radius: 15px 15px 15px 0px;
        margin-bottom: 10px;
        border: 2px solid #000000;
        max-width: 80%;
    }
    .bubble-dev {
        background-color: #FFFFFF;
        color: #000000 !important;
        padding: 12px;
        border-radius: 15px 15px 0px 15px;
        margin-bottom: 10px;
        margin-left: auto;
        border: 1px solid #CCCCCC;
        max-width: 80%;
    }
    
    /* Code View Window Block Styling */
    .code-window {
        background-color: #000000 !important;
        color: #FFFFFF !important;
        font-family: 'Courier New', Courier, monospace !important;
        padding: 20px !important;
        border-radius: 10px !important;
        overflow-x: auto;
        white-space: pre;
    }
    </style>
""", unsafe-allow_html=True)


# ==========================================================
# PAGE 1: LOGIN SCREEN (Matches Mockup 1)
# ==========================================================
if st.session_state.page == "login":
    st.markdown("<h1 style='text-align: center; font-size: 70px; margin-bottom: 0;'>Bestie 💖</h1>", unsafe-allow_html=True)
    
    col_c, col_box, col_r = st.columns([1, 2, 1])
    with col_box:
        email_input = st.text_input("Email", placeholder="Enter your email...")
        password_input = st.text_input("Password", type="password", placeholder="Enter password...")
        
        # Checking logic condition: Email routing vs secret passcode
        if st.button("Sign In", use_container_width=True):
            if password_input == "77799123":
                st.session_state.page = "secret_list"
                st.rerun()
            elif email_input:
                st.session_state.page = "client_dashboard"
                st.rerun()
            else:
                st.error("Please enter your login email or developer passcode!")
                
        st.markdown("<p style='text-align: center; color: #FF2E93;'>or</p>", unsafe-allow_html=True)
        
        if st.button("🔴 Sign in with google", use_container_width=True):
            st.session_state.page = "client_dashboard"
            st.rerun()


# ==========================================================
# PAGE 2: DEVELOPER PORTAL - CHOOSE CLIENT (Matches Mockup 2)
# ==========================================================
elif st.session_state.page == "secret_list":
    st.markdown("<h1 style='text-align: center; font-size: 60px;'>Secret 🤫</h1>", unsafe-allow_html=True)
    st.markdown("<h3 style='text-align: center; color: black !important;'>People that need coding</h3>", unsafe-allow_html=True)
    
    st.write("")
    col_l, col_btn, col_r = st.columns([1, 2, 1])
    with col_btn:
        st.markdown("<div class='white-card'>", unsafe-allow_html=True)
        if st.button("👤 Sally", use_container_width=True):
            st.session_state.page = "dev_workspace"
            st.rerun()
        st.markdown("</div>", unsafe-allow_html=True)
        
        st.write("")
        if st.button("Logout"):
            st.session_state.page = "login"
            st.rerun()


# ==========================================================
# PAGE 3: DEVELOPER ENGINE STUDIO (Matches Mockup 3)
# ==========================================================
elif st.session_state.page == "dev_workspace":
    col_chat, col_code = st.columns([1, 1])
    
    with col_chat:
        st.markdown("<h2>Bestie ai (me)</h2>", unsafe-allow_html=True)
        
        # Render out chat log conversation logs dynamically
        for chat in st.session_state.chat_history:
            if chat["sender"] == "client":
                st.markdown(f"<div class='bubble-client'>{chat['text']}</div>", unsafe-allow_html=True)
            else:
                st.markdown(f"<div class='bubble-dev'>{chat['text']}</div>", unsafe-allow_html=True)
        
        st.markdown(f"**Selected Option:** {st.session_state.selected_chat_option}")
        
        st.write("---")
        dev_reply = st.text_input("Message sally", key="dev_msg_field", placeholder="Type response to Sally...")
        if st.button("Send message"):
            if dev_reply:
                st.session_state.chat_history.append({"sender": "developer", "text": dev_reply})
                st.rerun()
                
    with col_code:
        st.markdown("<h2>code that I have to do to make the web</h2>", unsafe-allow_html=True)
        st.session_state.app_code = st.text_area("Python Code Editor Terminal Namespace:", 
                                                 value=st.session_state.app_code, height=450)
        
        if st.button("✨ Push Live to Sally", use_container_width=True):
            st.toast("Code successfully compiled and published live to Sally's app frame!")
            
    st.write("")
    if st.button("⬅️ Back to Client List"):
        st.session_state.page = "secret_list"
        st.rerun()


# ==========================================================
# PAGE 4: CLIENT INTERFACE - MAIN WORKSPACE (Matches Mockup 4)
# ==========================================================
elif st.session_state.page == "client_dashboard":
    col_sidebar, col_main = st.columns([1, 3])
    
    with col_sidebar:
        st.markdown("<h2 style='font-size:32px;'>Bestie Ai</h2>", unsafe-allow_html=True)
        st.write("---")
        
        # Display existing apps list item components
        for existing_app in st.session_state.apps_list:
            if st.button(f"📱 {existing_app}", use_container_width=True):
                st.session_state.current_editing_app = existing_app
                st.session_state.page = "client_preview"
                st.rerun()
                
        st.write("---")
        st.markdown("<div style='margin-top:100px;'><b>👤 Sally Lennon</b></div>", unsafe-allow_html=True)
        if st.button("Sign Out"):
            st.session_state.page = "login"
            st.rerun()
            
    with col_main:
        st.markdown("<h1 style='font-size: 70px; margin-bottom:0;'>Bestie 💖</h1>", unsafe-allow_html=True)
        st.markdown("<h3>Create your Imagination</h3>", unsafe-allow_html=True)
        
        new_idea = st.text_area("The white box is where you type in your new app:", 
                                placeholder="Describe your dream app idea here in complete detail...", height=200)
        
        if st.button("Send to Bestie Team", use_container_width=True):
            if new_idea:
                st.session_state.chat_history.append({"sender": "client", "text": new_idea})
                st.session_state.page = "client_preview"
                st.rerun()


# ==========================================================
# PAGE 5: CLIENT APP PREVIEW INTERACTIVE PORTAL (Matches Mockup 5)
# ==========================================================
elif st.session_state.page == "client_preview":
    col_nav_chat, col_nav_preview = st.columns([1, 1.5])
    
    with col_nav_chat:
        st.markdown("<h3>Bestie AI Chat Assistant</h3>", unsafe-allow_html=True)
        
        # Render matching layout context items
        for chat in st.session_state.chat_history:
            if chat["sender"] == "client":
                st.markdown(f"<div class='bubble-client'>{chat['text']}</div>", unsafe-allow_html=True)
            else:
                st.markdown(f"<div class='bubble-dev'>{chat['text']}</div>", unsafe-allow_html=True)
                
        st.write("---")
        st.write("**Question: What kind of chats**")
        st.session_state.selected_chat_option = st.radio(
            "Select app options:", 
            ["only group chats", "Only chats", "Both"], 
            index=["only group chats", "Only chats", "Both"].index(st.session_state.selected_chat_option)
        )
        
        client_reply = st.text_input("message bestie Ai", placeholder="Ask a question or reply to Bestie...")
        if st.button("Send Reply"):
            if client_reply:
                st.session_state.chat_history.append({"sender": "client", "text": client_reply})
                st.rerun()
                
    with col_nav_preview:
        col_title, col_pub_btn = st.columns([2, 1])
        with col_title:
            st.markdown("<h1 style='margin:0;'>Preview</h1>", unsafe-allow_html=True)
        with col_pub_btn:
            if st.button("🚀 Publish", use_container_width=True):
                st.balloons()
                st.toast("App successfully deployed!")
                
        # Simulating domain namespace based on app assignment rules
        subdomain = st.session_state.current_editing_app.lower().replace(" ", "-")
        st.markdown(f"<p style='color:black !important; font-family:monospace;'>🌐 URL Namespace: <b>https://{subdomain}.bestie</b></p>", unsafe-allow_html=True)
        
        # Sandbox Rendering App Environment View Window Box
        st.markdown("<div class='code-window'>", unsafe-allow_html=True)
        st.text(st.session_state.app_code)
        st.markdown("</div>", unsafe-allow_html=True)
        
    st.write("---")
    if st.button("⬅️ Return to Dashboard"):
        st.session_state.page = "client_dashboard"
        st.rerun()
