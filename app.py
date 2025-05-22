import streamlit as st
from chatbot import chat_chain

st.title("Chatbot")

if "session_id" not in st.session_state:
    st.session_state.session_id = "user-session"

user_input = st.chat_input("Say something...")

if user_input:
    response = chat_chain.invoke(
        {"input": user_input},
        config={"configurable": {"session_id": st.session_state.session_id}}
    )

    st.chat_message("user").write(user_input)
    st.chat_message("ai").write(response.content)
