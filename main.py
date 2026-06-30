# -------------------------------------------------------------------------
# SCREEN 2: CLIENT VIEW (The Normal Page)
# -------------------------------------------------------------------------
elif st.session_state.user_role == "client":
    email = st.session_state.logged_in_email
    client_data = st.session_state.database[email]

    # Shows their name and the Publish Button
    col_header, col_pub = st.columns([4, 1])
    with col_header:
        st.title(f"✨ Welcome to Bestie, {email}!")
        st.subheader(f"Project: {client_data['app_name']}")
    with col_pub:
        if st.button("🌐 Publish App", use_container_width=True):
            st.session_state.show_pub = True

    # Shows the Chat Box (Left) and Live Preview (Right)
    st.markdown("---")
    left_col, right_col = st.columns(2)

    with left_col:
        st.header("💬 Chat with your Coder")
        for msg in client_data["messages"]:
            st.write(f"**{msg['sender']}:** {msg['text']}")
        
        new_msg = st.text_input("Send a message:", key="client_msg_input")
        if st.button("Send"):
            if new_msg:
                client_data["messages"].append({"sender": "Client", "text": new_msg})
                st.rerun()

    with right_col:
        st.header("👀 Your App Preview")
        # This line actually draws the website on their screen!
        st.components.v1.html(client_data["code"], height=300, scrolling=True)
      elif st.session_state.user_role == "client":
# -------------------------------------------------------------------------
# SCREEN 3: DEVELOPER WORKSPACE (The Secret Page)
# -------------------------------------------------------------------------
elif st.session_state.user_role == "developer":
    target_client = st.session_state.assigned_client_email
    client_data = st.session_state.database[target_client]

    st.title("🛠️ Bestie Coder Workspace")
    st.markdown(f"### Running workspace for user: `{target_client}`")
    st.markdown("---")

    # Shows the Chat History (Left) and the Code Editor (Right)
    dev_left, dev_right = st.columns(2)

    with dev_left:
        st.header("💬 Chat History")
        for msg in client_data["messages"]:
            st.write(f"**{msg['sender']}:** {msg['text']}")
        
        # Where you send messages back to your friend
        dev_reply = st.text_input("Reply to client:", key="dev_msg_input")
        if st.button("Send Reply"):
            if dev_reply:
                client_data["messages"].append({"sender": "Developer", "text": dev_reply})
                st.rerun()

    with dev_right:
        st.header("💻 Live Code Workspace")
        # The box where you actually type the HTML/CSS edits
        new_code = st.text_area("Write HTML/CSS Here", value=client_data["code"], height=200)
        
        # This saves the code the second you change it!
        if new_code != client_data["code"]:
            client_data["code"] = new_code
            st.toast("Saved!")

        st.subheader("Preview")
        st.components.v1.html(client_data["code"], height=150, scrolling=True)
      
elif st.session_state.user_role == "developer":
