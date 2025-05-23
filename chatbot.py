from langchain_core.runnables.history import RunnableWithMessageHistory # Imports a class to add message history to chains.
from langchain_google_genai import ChatGoogleGenerativeAI # Imports the Gemini API wrapper for LangChain.
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder # Imports prompt template utilities.
from langchain_community.chat_message_histories import StreamlitChatMessageHistory # Imports Streamlit-based message history.
from dotenv import load_dotenv # Imports dotenv to load environment variables from a .env file.
import os # Imports the os module for environment variable access.

load_dotenv() # Loads environment variables from a .env file.

# Initialize the Google Gemini LLM with model name, API key, and temperature.
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.7
)

# Defines the prompt template, including system, history, and user messages.
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."), # System message to set assistant behavior.
    MessagesPlaceholder(variable_name="history"), # Placeholder for conversation history.
    ("human", "{input}") # Placeholder for user's input.
])

# Chains the prompt and the LLM together.
chain = prompt | llm

# Wraps the chain with message history for conversational memory.
chat_chain = RunnableWithMessageHistory(
    chain,
    lambda session_id: StreamlitChatMessageHistory(), # Uses Streamlit-based message history per session.
    input_messages_key="input", # Key for current user input.
    history_messages_key="history" # Key for conversation history.
)
