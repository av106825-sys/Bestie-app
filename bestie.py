import streamlit as st

# --- 1. INITIALIZE GLOBAL STORAGE (TEAM QUEUE) ---
if "page" not in st.session_state:
    st.session_state.page = "login"

if "current_dev" not in st.session_state:
    st.session_state.current_dev = None

if "current_client" not in st.session_state:
    st.session_state.current_client = "Sally 👤"

# The master database hosting different clients for different developers
if "clients_queue" not in st.session_state:
    st.session_state.clients_queue = {
        "Sally 👤": {
            "app_name": "Dance queen",
            "assigned_to": "Developer 1 🛠️",
            "code": "print('Dance Studio App Active!')",
            "messages": ["Sally 👤: Make an app that could make messages", "Bestie 🤖: Working on it!"]
        },
        "Jake 👟": {
            "app_name": "Sneaker Vault",
            "assigned_to": "Developer 2 🛠️",
            "code": "print('Vault Loaded')",
            "messages": ["Jake 👟: I need a store app to trade cool shoes."]
        }
    }


# --- 2. THEME STYLING (100% iPad-Safe Pink Theme) ---
# We put this all on one single line so the iPad keyboard cannot create syntax errors!
safe_css = "<style>.stApp { background-color: #E8A7F5 !important; } h1, h2, h3, p, label, .stMarkdown { color: #FF2E93 !important; font-family: sans-serif; font-weight: bold; } div.stTextArea textarea, div.stTextInput input { background-color: #FFFFFF !important; color: #000000 !important; border-radius: 20px !important; padding: 15px !important; } div.stButton > button { background-color: #FFFFFF !important; color: #FF2E93 !important; border-radius: 25px !important; border: 2px solid #FF2E93 !important; font-weight: bold !important; } div.stButton > button:hover { background-color: #FF2E93 !important; color: #FFFFFF !important; }</style>"
st.markdown(safe_css, unsafe_allow_html=True)


# --- PAGE 1: LOGIN SCREEN ---
if st.session_state.page == "login":
    st.title("Bestie 💖")
    email = st.text_input("Email Address", placeholder="Enter email...")
    password = st.text_input("Password", type="password", placeholder="Enter password...")
    
    if st.button("Sign In", use_container_width=True):
        if password == "77799123":
            st.session_state.page = "secret_list"
            st.rerun()
        elif email:
            st.session_state.current_client = "Sally 👤"
            st.session_state.page = "client_dashboard"
            st.rerun()
            
    st.write("or")
    if st.button("🔴 Sign in with google", use_container_width=True):
        st.session_state.current_client = "Sally 👤"
        st.session_state.page = "client_dashboard"
        st.rerun()


# --- PAGE 2: DEVELOPER PORTAL (TEAM SELECTOR) ---
elif st.session_state.page == "secret_list":
    st.title("Secret Portal 🤫")
    st.subheader("Select your developer identity:")
    
    dev_slots = ["Developer 1 🛠️", "Developer 2 🛠️"]
    
    for dev in dev_slots:
        assigned_person = "No one"
        for client_name, data in st.session_state.clients_queue.items():
            if data["assigned_to"] == dev:
                assigned_person = client_name
        
        if st.button(f"💻 {dev} (Assigned to: {assigned_person})", use_container_width=True):
            st.session_state.current_dev = dev
            st.session_state.current_client = assigned_person
            st.session_state.page = "dev_workspace"
            st.rerun()
            
    st.write("---")
    if st.button("⬅️ Logout"):
        st.session_state.page = "login"
        st.rerun()


# --- PAGE 3: DEVELOPER WORKSPACE ---
elif st.session_state.page == "dev_workspace":
    dev_id = st.session_state.current_dev
    client_id = st.session_state.current_client
    client_data = st.session_state.clients_queue[client_id]
    
    st.title(f"{dev_id} Workspace")
    st.subheader(f"Working on App for: {client_id}")
    st.write(f"📁 Target Project Name: **{client_data['app_name']}**")
    
    col_chat, col_code = st.columns(2)
    
    with col_chat:
        st.write("### 💬 Chat History")
        for msg in client_data["messages"]:
            st.info(msg)
            
        dev_reply = st.text_input("Reply to client:", placeholder="Type here...")
        if st.button("Send Message") and dev_reply:
            client_data["messages"].append(f"Bestie 🤖: {dev_reply}")
            st.rerun()
            
    with col_code:
        st.write("### 💻 Cloud Editor")
        updated_code = st.text_area("Edit Live Script:", value=client_data["code"], height=250)
        if st.button("🚀 Push Code Live"):
            client_data["code"] = updated_code
            st.success("Code deployed!")
            
    if st.button("⬅️ Back to Team List"):
        st.session_state.page = "secret_list"
        st.rerun()


# --- PAGE 4: CLIENT DASHBOARD ---
elif st.session_state.page == "client_dashboard":
    client_id = st.session_state.current_client
    client_data = st.session_state.clients_queue[client_id]
    
    st.title(f"Welcome back, {client_id}!")
    st.write(f"Your project **{client_data['app_name']}** is assigned to **{client_data['assigned_to']}**.")
    
    st.write("---")
    st.subheader("💬 Chat with your Developer")
    for msg in client_data["messages"]:
        st.warning(msg)
        
    client_msg = st.text_input("Message your developer:", placeholder="Type a request...")
    if st.button("Send Request") and client_msg:
        client_data["messages"].append(f"{client_id}: {client_msg}")
        st.rerun()
        
    st.write("---")
    st.subheader("🌐 Your Live App Preview")
    st.code(client_data["code"], language="python")
    
    if st.button("⬅️ Logout"):
        st.session_state.page = "login"
        st.rerun()
