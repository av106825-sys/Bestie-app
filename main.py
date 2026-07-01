import streamlit as st

# --- 1. INITIALIZE GLOBAL STORAGE (SESSION STATE) ---
if "page" not in st.session_state:
    st.session_state.page = "login"

# This holds every single app created on your platform dynamically!
if "apps" not in st.session_state:
    st.session_state.apps = {
        "Dance queen": {
            "code": "import tkinter as tk\n# Dance Queen Core Code\nprint('Dance Studio App Active!')",
            "messages": [
                {"sender": "client", "type": "text", "content": "Make an app that could make messages"},
                {"sender": "developer", "type": "text", "content": "Ok I'll make an app that could make messages"},
                {"sender": "client", "type": "text", "content": "It could make groups"}
            ],
            "active_question": {
                "text": "What kind of chats do you want?",
                "options": ["only group chats", "Only chats", "Both"]
            }
        },
        "Yoga master": {
            "code": "import tkinter as tk\n# Yoga Master Core Code\nprint('Yoga App Active!')",
            "messages": [
                {"sender": "client", "type": "text", "content": "I want a relaxing yoga app"}
            ],
            "active_question": None
        }
    }

if "current_app" not in st.session_state:
    st.session_state.current_app = "Dance queen"


# --- 2. THEME STYLING (iPad-Safe Pink & Purple) ---
st.markdown("""
    <style>
    .stApp { background-color: #E8A7F5 !important; }
    h1, h2, h3, p, label, .stMarkdown { color: #FF2E93 !important; font-family: sans-serif; font-weight: bold; }
    div.stTextArea textarea, div.stTextInput input { background-color: #FFFFFF !important; color: #000000 !important; border-radius: 20px !important; padding: 15px !important; }
    div.stButton > button { background-color: #FFFFFF !important; color: #FF2E93 !important; border-radius: 25px !important; border: 2px solid #FF2E93 !important; font-weight: bold !important; }
    div.stButton > button:hover { background-color: #FF2E93 !important; color: #FFFFFF !important; }
    </style>
""", unsafe-allow_html=True)


# ==========================================================
# PAGE 1: LOGIN SCREEN
# ==========================================================
if st.session_state.page == "login":
    st.title("Bestie 💖")
    
    email = st.text_input("Email", placeholder="Enter your email...")
    password = st.text_input("Password", type="password", placeholder="Enter password...")
    
    if st.button("Sign In", use_container_width=True):
        if password == "77799123":
            st.session_state.page = "secret_list"
            st.rerun()
        elif email:
            st.session_state.page = "client_dashboard"
            st.rerun()
        else:
            st.error("Please enter your login email or developer passcode!")
            
    st.write("or")
    if st.button("🔴 Sign in with google", use_container_width=True):
        st.session_state.page = "client_dashboard"
        st.rerun()


# ==========================================================
# PAGE 2: DEVELOPER PORTAL - CHOOSE CLIENT
# ==========================================================
elif st.session_state.page == "secret_list":
    st.title("Secret 🤫")
    st.subheader("People that need coding")
    
    if st.button("👤 Sally", use_container_width=True):
        st.session_state.page = "dev_workspace"
        st.rerun()
        
    st.write("---")
    if st.button("Logout"):
        st.session_state.page = "login"
        st.rerun()


# ==========================================================
# PAGE 3: DEVELOPER PORTAL - APP MODIFIER
# ==========================================================
elif st.session_state.page == "dev_workspace":
    st.title("Bestie ai (me) 🛠️")
    
    selected_app = st.selectbox("Select client app project to edit:", list(st.session_state.apps.keys()))
    col_chat_view, col_code_editor = st.columns(2)
    
    with col_chat_view:
        st.subheader("💬 Chat Log & Question Creator")
        
        for msg in st.session_state.apps[selected_app]["messages"]:
            prefix = "Sally 👤: " if msg["sender"] == "client" else "Me 🤖: "
            if msg["type"] == "text":
                st.info(f"{prefix}{msg['content']}")
            elif msg["type"] == "answer":
                st.warning(f"{prefix}Selected dot: {msg['content']}")

        st.write("---")
        
        dev_text = st.text_input("Type a regular message:", placeholder="Type anything here...")
        if st.button("Send Message"):
            if dev_text:
                st.session_state.apps[selected_app]["messages"].append({"sender": "developer", "type": "text", "content": dev_text})
                st.rerun()
                
        st.write("---")
        q_text = st.text_input("Create a multiple-choice question:")
        options_text = st.text_input("Comma-separated options (ex: Yes, No, Both):")
        if st.button("Send Question with Dots"):
            if q_text and options_text:
                opts = [opt.strip() for opt in options_text.split(",")]
                st.session_state.apps[selected_app]["active_question"] = {"text": q_text, "options": opts}
                st.session_state.apps[selected_app]["messages"].append({"sender": "developer", "type": "text", "content": f"New Question Sent: {q_text}"})
                st.rerun()
                
    with col_code_editor:
        st.subheader("💻 Code Window")
        current_code = st.text_area("Edit Python/Tkinter code script:", value=st.session_state.apps[selected_app]["code"], height=300)
        
        if st.button("🚀 Push Code Update Live", use_container_width=True):
            st.session_state.apps[selected_app]["code"] = current_code
            st.balloons()
            st.success("App code updated instantly inside client container!")
            
    if st.button("⬅️ Back to Secret List"):
        st.session_state.page = "secret_list"
        st.rerun()


# ==========================================================
# PAGE 4: CLIENT INTERFACE - MAIN HUB
# ==========================================================
elif st.session_state.page == "client_dashboard":
    col_sidebar, col_main = st.columns([1, 2.5])
    
    with col_sidebar:
        st.subheader("Bestie Ai")
        st.write("---")
        st.write("### Your Apps:")
        
        for app_name in st.session_state.apps.keys():
            if st.button(f"📱 {app_name}", use_container_width=True):
                st.session_state.current_app = app_name
                st.session_state.page = "client_preview"
                st.rerun()
                
        st.write("---")
        st.write("👤 **Sally Lennon**")
        if st.button("Sign Out"):
            st.session_state.page = "login"
            st.rerun()
            
    with col_main:
        st.title("Bestie 💖")
        st.subheader("Create your Imagination")
        
        new_app_name = st.text_input("Name your new app:")
        new_idea = st.text_area("The white box is where you type in your new app:", placeholder="Describe what you want your new app to do...", height=150)
        
        if st.button("Submit App Idea to Bestie Team", use_container_width=True):
            if new_app_name and new_idea:
                st.session_state.apps[new_app_name] = {
                    "code": "# Custom code template initialized by developer team",
                    "messages": [{"sender": "client", "type": "text", "content": new_idea}],
                    "active_question": None
                }
                st.session_state.current_app = new_app_name
                st.session_state.page = "client_preview"
                st.rerun()


# ==========================================================
# PAGE 5: CLIENT PORTAL - APP RUNNER & PREVIEW
# ==========================================================
elif st.session_state.page == "client_preview":
    active_app = st.session_state.current_app
    col_interaction, col_live_frame = st.columns(2)
    
    with col_interaction:
        st.subheader("Bestie AI Chat")
        st.write(f"App Target: **{active_app}**")
        
        for msg in st.session_state.apps[active_app]["messages"]:
            prefix = "Sally 👤: " if msg["sender"] == "client" else "Bestie 🤖: "
            if msg["type"] == "text":
                st.info(f"{prefix}{msg['content']}")
            elif msg["type"] == "answer":
                st.warning(f"{prefix}Picked dot: {msg['content']}")
                
        st.write("---")
        
        q_data = st.session_state.apps[active_app]["active_question"]
        if q_data:
            st.write(f"❓ **Question: {q_data['text']}**")
            chosen_dot = st.radio("Pick a dot:", q_data["options"], key="client_dots")
            if st.button("Submit Chosen Dot"):
                st.session_state.apps[active_app]["messages"].append({"sender": "client", "type": "answer", "content": chosen_dot})
                st.session_state.apps[active_app]["active_question"] = None
                st.rerun()
        else:
            st.write("✨ No pending questions from Bestie Team!")
            
        st.write("---")
        client_msg = st.text_input("Send anything to Bestie Ai:", placeholder="Type a message or new request...")
        if st.button("Send Text"):
            if client_msg:
                st.session_state.apps[active_app]["messages"].append({"sender": "client", "type": "text", "content": client_msg})
                st.rerun()
                
    with col_live_frame:
        st.title("Preview")
        if st.button("Publish", use_container_width=True):
            st.balloons()
            st.toast("App updated live on custom domain namespace!")
                
        subdomain = active_app.lower().replace(" ", "-")
        st.write(f"🌐 Running on: `https://{subdomain}.bestie`")
        
        st.code(st.session_state.apps[active_app]["code"], language="python")
        
    st.write("---")
    if st.button("⬅️ Return to Dashboard"):
        st.session_state.page = "client_dashboard"
        st.rerun()
