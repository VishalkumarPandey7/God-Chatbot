import streamlit as st
from dotenv import load_dotenv
import os

from langchain_groq import ChatGroq

# Load API key
load_dotenv()

if not os.getenv("GROQ_API_KEY"):
    st.error("❌ GROQ_API_KEY not found in .env file")
    st.stop()

# Initialize Groq model
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

# ✅ Page Config
st.set_page_config(page_title="GOD", page_icon="✨")

# ✅ Main Title + Subtitle
st.title("✨ GOD")
st.subheader("Ask anything — all at once")

st.markdown("---")

# Session state for storing chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display old chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input box
user_input = st.chat_input("Type your message...")

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    # Build conversation context
    conversation_text = ""
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            conversation_text += f"Human: {msg['content']}\n"
        else:
            conversation_text += f"AI: {msg['content']}\n"

    conversation_text += "AI:"

    # Get Groq response
    response = llm.invoke(conversation_text).content

    # Show AI response
    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
        st.markdown(response)
