*This project is a Retrieval-Augmented Generation (RAG) chatbot built using:*

- Python 3.12
- FAISS as a vector database
- HuggingFace all-MiniLM-L6-v2 embeddings
- Gemini 2.5 Flash as the LLM
- A custom prompt for rewriting, friendliness, Bahasa Malaysia output, and structured formatting
- Basic security guardrails

The chatbot is designed to answer Tonton customer support questions using ONLY verified internal documents.

**1. Project Overview**

The RAG workflow using Langchain:
- a. PDF to Text 
    - PDF content was converted into a text file for easier embedding and chunking.
- b. Text Embedding 
    - HuggingFace model (all-MiniLM-L6-v2) is used to convert texts to vectors
- c. Vector Store Creation
    - FAISS (Facebook AI Similiarity Search) is used to create vector database containing index.faiss & index.pkl
- d. Retriever
    - search_kwargs={"k": 2} is used to return the top 2 most relevant document chunks for each query (Higher K, slower search but more context)
- e. LLM (Gemini 2.5 Flash)
    - temp = 2.5 for more stable and controlled answer  
    - max output tokens = 2048 to ensures the model can write long structured answers when needed.
- f. Custom Prompt Engineering
    - The prompt makes the model:
        - Rewrite unclear user questions
        - Fix spelling & slang
        - Interpret synonyms
        - Choose structured formatting automatically (steps, bullets, emojis)
        - Answer in Bahasa Malaysia
        - Stay polite
        - Avoid hallucination
        - Be friendly for greetings
        - Hide chain-of-thought reasoning
- g. Guardrails
    - Before sending queries to the model, the system blocks dangerous topics.

**2. Two Different Web Environment for Chatbot**
- a. HTML / CSS / JavaScript Frontend (Production‑Style UI with FastAPI Backend)
    - HTML - page layout
    - CSS - UI styling
    - JavaScript - handles user input, API requests, and displaying responses
    - FastAPI - the backend server that runs the RAG pipeline

- b. Streamlit App (app.py) — Demo & Showcase Version
    - Directly linked to python backend (src)
    - For portfolio presentation

**3. Security Notes**
    - .env is ignored → API key safe
    - Guardrails prevent harmful queries
    - RAG prevents hallucination
    - No external calls except to Gemini API