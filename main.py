import streamlit as st

# 1. SETUP THE MEMORY
if "user_role" not in st.session_state:
    st.session_state.user_role = None

# 2. THE LOGIN SCREEN (This is the first "if" that was missing!)
if st.session_state.user_role == None:
    st.title("Welcome to Bestie AI 💖")
    email = st.text_input("Email:")
    password = st.text_input("Password (or Secret Passcode):", type="password")
    
    if st.button("Log In"):
        # Client Login
        if email == "sarah@email.com" and password == "password123":
            st.session_state.user_role = "client"
            st.rerun()
        # Secret Developer Login
        elif password == "77799123":
            st.session_state.user_role = "developer"
            st.rerun()
        else:
            st.error("Incorrect email or password!")

# 3. THE CLIENT SCREEN
elif st.session_state.user_role == "client":
    st.title("💖 Bestie App Workspace")
    st.write("Hello! I am Bestie AI. What can I build for you today?")
    user_msg = st.text_input("Tell Bestie what you want:")
    if st.button("Send to Bestie"):
        st.success("Message magically sent to Bestie AI!")

# 4. THE SECRET SCREEN
elif st.session_state.user_role == "developer":
    st.title("🤫 Secret Wizard Terminal")
    st.write("You are behind the curtain! You are acting as Bestie AI.")
    reply = st.text_area("Type the code for your friend here:")
    if st.button("Push Code to Client Screen"):
        st.success("Code successfully sent!")
