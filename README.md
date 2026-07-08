# 💀 Savage Sigma AI

> A cyberpunk-themed chatbot with persistent session isolation, dynamic user name detection, and a brutal AI persona. Powered by LangChain, Flask, and the Groq API (Llama 3.1 8B).

[![Live Demo](https://img.shields.io/badge/Live-Demo_Available-ff007f?style=for-the-badge)](https://genai-document-intelligence.onrender.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-Backend-green?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com)
[![Groq](https://img.shields.io/badge/Groq-LLM_API-orange?style=for-the-badge)](https://groq.com)

---

## 🌐 Live Deployment

Try the live production chatbot directly in your browser:

* **💀 Savage Sigma AI:** [**Launch Chatbot 🚀**](https://genai-document-intelligence.onrender.com/)
* **Hosting Platform:** Render.com (Free Tier)

> [!NOTE]
> *The Savage Sigma AI chatbot is hosted on a free Render tier. If the website has not been visited recently, the instance may sleep. Please allow **30–45 seconds** for the server to spin back up on your first visit.*

---

## 🛠️ Key Features

* **💀 Savage Persona (Sigma AI):** A highly sarcastic, dominant, and aggressive chatbot that demands your name before answering any question, roasting you dynamically.
* **🕵️‍♂️ Dynamic Name Extraction:** Leverages regex and pattern matching to extract the user's name from conversation starters. Name extraction guards prevent simple phrases from hijacking or resetting it once locked.
* **🔒 Session Isolation & Persistence:** Uses local storage browser UUIDs to ensure chat histories are safely isolated and preserved per browser tab or user session.
* **⚡ Premium Cyberpunk UI:** A responsive neon interface with glassmorphic panels, dynamic typing indicators, marked.js markdown rendering, and clean custom styling for code blocks.
* **🤖 CLI Version:** Includes a local command-line interface chatbot (`roast_bot.py`) for direct terminal interactions.

---

## 📂 Project Structure

```
SAVAGE-SIGMA-AI/
├── .devcontainer/
│   └── devcontainer.json   # VS Code remote container config
├── .gitignore              # Rules for files to exclude from Git
├── Procfile                # Startup configuration for Render.com
├── front.py                # Flask server serving API & index.html
├── index.html              # Cyberpunk user interface HTML/JS
├── roast_bot.py            # CLI version of the Sigma Chatbot
├── main.py                 # CLI basic Groq API chatbot
├── langchain_bot.py        # CLI basic LangChain API chatbot
└── requirements.txt        # Python package dependencies
```

---

## ⚙️ Local Installation & Setup

Follow these steps to run the Savage Sigma AI chatbot locally on your system:

### 1. Set Up a Virtual Environment
Initialize a clean Python environment to keep packages isolated:
```bash
python -m venv venv

# Activate (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Activate (macOS/Linux)
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Create a file named `.env` in the root folder of the project. Add your Groq API key:
```env
GROQ_API_KEY=your-groq-api-key-here
```

> [!TIP]
> **How to get a Groq API key (100% Free):**
> 1. Sign up at [console.groq.com](https://console.groq.com).
> 2. Navigate to **API Keys** on the sidebar.
> 3. Click **Create API Key**, copy it, and paste it into your `.env` file.

### 4. Run the Chatbot
Start the Flask server locally:
```bash
python front.py
```
Open `http://127.0.0.1:5000` in your web browser.

**Or run the CLI version in your terminal:**
```bash
python roast_bot.py
```

---

## 🛠️ Tech Stack

* **Flask:** Python web framework for backend endpoints.
* **OpenAI SDK:** Connects and sends queries to the Groq API.
* **Vanilla HTML5 & CSS3:** Responsive UI with custom cyberpunk styling.
* **Groq API / Llama 3.1 8B:** Instantly responds with a smart and funny roast persona.

---

<p align="center">
  Developed by <a href="https://github.com/bharathwajverse">@bharathwajverse</a>
</p>
