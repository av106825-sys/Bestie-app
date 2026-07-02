import streamlit as st

# --- 1. INITIALIZE MASTER DATABASE (SESSION STATE) ---
if "page" not in st.session_state:
    st.session_state.page = "login"

if "user_email" not in st.session_state:
    st.session_state.user_email = ""

if "user_name" not in st.session_state:
    st.session_state.user_name = ""

if "selected_client_email" not in st.session_state:
    st.session_state.selected_client_email = ""

if "active_preview_app" not in st.session_state:
    st.session_state.active_preview_app = None

# Central database indexed by email addresses
if "clients_db" not in st.session_state:
    st.session_state.clients_db = {
        "sally@gmail.com": {
            "name": "Sally Lennon",
            "apps": {
                "Dance queen": {"code": "print('Dance Studio App Active!')", "messages": ["Sally Lennon 👤: Make an app that could make messages"]},
                "Yoga master": {"code": "print('Yoga App Active!')", "messages": ["Sally Lennon 👤: I want a relaxing yoga app"]}
            }
        }
    }


# --- 2. THEME STYLING (100% iPad-Safe Pink Theme Layout) ---
safe_css = "<style>.stApp { background-color: #E8A7F5 !important; } [data-testid='stSidebar'] { background-color: #E8A7F5 !important; border-right: 3px solid #FF2E93 !important; } h1, h2, h3, p, label, .stMarkdown { color: #FF2E93 !important; font-family: sans-serif; font-weight: bold; } div.stTextArea textarea, div.stTextInput input { background-color: #FFFFFF !important; color: #000000 !important; border-radius: 20px !important; padding: 15px !important; border: none !important; } div.stButton > button { background-color: #FFFFFF !important; color: #FF2E93 !important; border-radius: 25px !important; border: 2px solid #FF2E93 !important; font-weight: bold !important; } div.stButton > button:hover { background-color: #FF2E93 !important; color: #FFFFFF !important; }</style>"
st.markdown(safe_css, unsafe_allow_html=True)


# --- PAGE 1: LOGIN SCREEN ---
if st.session_state.page == "login":
    st.title("Bestie 💖")
    email_input = st.text_input("Gmail Address", placeholder="Enter your email...")
    name_input = st.text_input("First & Last Name (For Clients)", placeholder="e.g., Sally Lennon")
    pass_input = st.text_input("Password (Optional)", type="password", placeholder="Enter secret code if developer...")
    
    if st.button("Sign In", use_container_width=True):
        if pass_input == "77799123":
            st.session_state.page = "secret_list"
            st.rerun()
        elif email_input:
            clean_email = email_input.lower().strip()
            st.session_state.user_email = clean_email
            
            # Check if this person already has a profile registered
            if clean_email in st.session_state.clients_db:
                st.session_state.user_name = st.session_state.clients_db[clean_email]["name"]
            else:
                # If first time logging in, record their name and establish an empty app space
                st.session_state.user_name = name_input if name_input else "Guest User"
                st.session_state.clients_db[clean_email] = {
                    "name": st.session_state.user_name,
                    "apps": {}  # Completely empty sidebar app dictionary for new accounts
                }
            
            st.session_state.page = "client_dashboard"
            st.rerun()


# --- PAGE 2: CLIENT DASHBOARD ---
elif st.session_state.page == "client_dashboard":
    current_user_data = st.session_state.clients_db[st.session_state.user_email]
    my_apps = current_user_data["apps"]
    
    # --- SIDEBAR INTERFACE IMPLEMENTATION ---
    with st.sidebar:
        st.title("Bestie Ai")
        st.write("---")
        
        # Lists active apps dynamically on the side panel menu
        if not my_apps:
            st.write("✨ No apps created yet!")
        else:
            for app_name in list(my_apps.keys()):
                if st.button(f"📱 {app_name}", use_container_width=True):
                    st.session_state.active_preview_app = app_name
                    
        st.write("---")
        # Profile display module mapping directly to your bottom badge layout
        st.subheader(f"💖 {st.session_state.user_name}")
        if st.button("Log Out"):
            st.session_state.page = "login"
            st.session_state.active_preview_app = None
            st.rerun()
            
    # --- MAIN CONTENT STREAM ---
    st.title("Bestie 💖")
    st.subheader("Create your Imagination")
    
    # The dedicated container matching your layout diagram
    user_prompt = st.text_area("Describe your app vision:", placeholder="Type what app you want me to build...", height=150, label_visibility="collapsed")
    
    if st.button("Submit App Request 🚀", use_container_width=True):
        if user_prompt.strip():
            # Automatically title the assignment depending on their database queue volume
            assigned_title = f"Project App {len(my_apps) + 1}"
            
            # Formulate the project schema inside their storage space
            my_apps[assigned_title] = {
                "code": "# Code assignment pending developer synchronization...",
                "messages": [f"{st.session_state.user_name} 👤: {user_prompt}"]
            }
            st.success(f"Deployed assignment '{assigned_title}' to your sidebar menu list!")
            st.rerun()
            
    # App live display matrix container 
    if st.session_state.active_preview_app and st.session_state.active_preview_app in my_apps:
        st.write("---")
        st.subheader(f"Live Simulation Window: {st.session_state.active_preview_app}")
        st.code(my_apps[st.session_state.active_preview_app]["code"], language="python")


# --- PAGE 3: DEVELOPER PORTAL ---
elif st.session_state.page == "secret_list":
    st.title("Secret Portal 🤫")
    st.subheader("Developer Task Queues:")
    
    for client_mail, data in st.session_state.clients_db.items():
        if st.button(f"💼 Open file for: {data['name']} ({len(data['apps'])} Active Apps)", use_container_width=True):
            st.session_state.selected_client_email = client_mail
            st.session_state.page = "dev_workspace"
            st.rerun()
            
    st.write("---")
    if st.button("⬅️ Return to Main Screen"):
        st.session_state.page = "login"
        st.rerun()


# --- PAGE 4: DEVELOPER WORKSPACE ---
elif st.session_state.page == "dev_workspace":
    target_mail = st.session_state.selected_client_email
    target_data = st.session_state.clients_db[target_mail]
    
    st.title(f"Editor Mode: {target_data['name']}")
    
    if not target_data["apps"]:
        st.warning("This user has no created projects in their queue.")
        if st.button("⬅️ Back to Queues"):
            st.session_state.page = "secret_list"
            st.rerun()
    else:
        chosen_app = st.selectbox("Select App Container:", list(target_data["apps"].keys()))
        app_profile = target_data["apps"][chosen_app]
        
        chat_col, code_col = st.columns(2)
        with chat_col:
            st.write("### 💬 Chat Log")
            for msg in app_profile["messages"]:
                st.info(msg)
            dev_input = st.text_input("Reply back to user:")
            if st.button("Send Message") and dev_input:
                app_profile["messages"].append(f"Bestie 🤖: {dev_input}")
                st.rerun()
                
        with code_col:
            st.write("### 💻 Cloud Editor Terminal")
            pushed_code = st.text_area("Edit Python Scripts Live:", value=app_profile["code"], height=250)
            if st.button("🚀 Push Code Update"):
                app_profile["code"] = pushed_code
                st.success("Changes deployed!")
                
        if st.button("⬅️ Back to Queues"):
            st.session_state.page = "secret_list"
            st.rerun()
