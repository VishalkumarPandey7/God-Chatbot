# ✨God Chatbot

God Chatbot is a Streamlit-based AI chatbot powered by **Groq LLM** and **LangChain**.  
It provides a clean ChatGPT-like interface where users can ask anything — all at once.

---
## 🔗 Live & Related Links
- *Live Application:* https://god-chatbot-r854xfdlm6kns5kw5wqwpa.streamlit.app/

## 🚀 Features

- 🤖 AI Chatbot powered by Groq
- 💬 Chat-style interface using Streamlit
- 🧠 Conversation context support
- ⚡ Fast responses with LLaMA 3.1 model
- 🔐 Secure API key handling using Streamlit Secrets

---

## 🛠 Tech Stack

- **Python**
- **Streamlit**
- **LangChain**
- **Groq API**

---

## 📂 Project Structure


```text

God-Chatbot/
│── chatbot.py
│── requirements.txt
│── .gitignore
│── README.md

```

---

## ⚙️ Installation (Run Locally)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/VishalkumarPandey7/God-Chatbot.git
cd God-Chatbot

2️⃣ Create Virtual Environment
python -m venv venv


Activate:

Windows:

.\venv\Scripts\Activate.ps1


Mac/Linux:

source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

🔑 Setup Groq API Key

Create a .env file locally:

GROQ_API_KEY=your_groq_api_key_here


⚠️ Do not upload .env to GitHub.

▶️ Run the Chatbot
streamlit run chatbot.py


App will open in browser:

http://localhost:8501

🌍 Deployment on Streamlit Cloud

Push project to GitHub

Go to: https://share.streamlit.io

Click New App

Select repo + chatbot.py

Add API key in Secrets:

GROQ_API_KEY="your_key_here"






👤 Author

Vishal Pandey
B.Tech CSE (AI) Student
Project: Saviour – Ask anything, all at once ✨

⭐ Support

If you like this project, give it a ⭐ on GitHub!
