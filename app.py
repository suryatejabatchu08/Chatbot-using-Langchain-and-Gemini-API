import streamlit as st # Import Streamlit for building the web UI
from chatbot import chat_chain # Import the chat_chain object from the chatbot module

st.title("Chatbot") # Set the title of the Streamlit app

# Initialize a session ID in Streamlit's session_state if it doesn't already exist
if "session_id" not in st.session_state:
    st.session_state.session_id = "user-session"

# Display a chat input box for the user to type their message
user_input = st.chat_input("Say something...")

# If the user has entered some input
if user_input:
    # Call the chat_chain's invoke method with the user's input and session ID
    response = chat_chain.invoke(
        {"input": user_input},
        config={"configurable": {"session_id": st.session_state.session_id}}
    )

    # Display the user's message in the chat UI (bubble)
    st.chat_message("user").write(user_input)
    # Display the chatbot's response in the chat UI (bubble)
    st.chat_message("ai").write(response.content)
