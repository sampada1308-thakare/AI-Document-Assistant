# AI Document Assistant

An AI-powered document assistant that allows users to ask questions about a PDF and get relevant answers using **RAG (Retrieval-Augmented Generation)** and an **AI Agent**.

## 🚀 Features

* 📄 Ask questions about a PDF document
* 🔍 Search relevant information using RAG
* 🤖 AI Agent that decides when to use tools
* 🧮 Calculator tool for basic calculations
* 💬 Conversation memory during the session
* 🧠 Local LLM using Ollama
* 📦 ChromaDB vector database
* 🔗 LangChain and LangGraph integration
* 🔐 No OpenAI API key required

## 🛠️ Technologies Used

* Python
* LangChain
* LangGraph
* RAG
* Ollama
* Llama 3.2
* Nomic Embed Text
* ChromaDB
* PyPDF
* Git & GitHub

## 🏗️ How It Works

```text
User Question
      ↓
AI Agent
      ↓
Decides whether a tool is needed
      ↓
 ┌───────────────┐
 │               │
 ↓               ↓
RAG Tool      Calculator
 │               │
 ↓               ↓
ChromaDB       Result
 │
 ↓
Relevant Document Content
      ↓
Local LLM (Llama 3.2)
      ↓
Final Answer
```

## 📁 Project Structure

```text
AI-Document-Assistant/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── documents/
│   └── sample.pdf
│
├── chroma_db/
│
└── src/
    ├── __init__.py
    ├── rag.py
    ├── agent.py
    └── tools.py
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/sampada1308-thakare/AI-Document-Assistant.git
```

### 2. Open the project

```bash
cd AI-Document-Assistant
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Ollama

Install Ollama on your computer and download the required models:

```bash
ollama pull llama3.2
ollama pull nomic-embed-text
```

### 5. Run the application

```bash
python app.py
```

## 💡 Example Questions

You can ask questions such as:

```text
Who is Harry Potter?

Where does he study?

Who appeared one day at the Dursleys' house?

What is 25 + 17?
```

The AI Agent determines whether it should search the document or use the calculator.

## 🔑 Why Ollama?

This project uses Ollama to run the LLM locally.

This means the project does not require an OpenAI API key or OpenAI API credits for the basic application.

## 📌 Future Improvements

* Web interface using Streamlit
* Support for multiple PDF documents
* Better conversation memory
* Cloud deployment
* Docker deployment
* Improved agent evaluation
* Authentication for users

## 👩‍💻 Author

**Sampada Vijay Thakare**

GitHub: https://github.com/sampada1308-thakare
