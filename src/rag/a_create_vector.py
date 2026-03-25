import os
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from langchain_core.documents import Document

documents = []

# Load documents
docs_path = "../Tonton RAG Chatbot/rag_docs"

for file in os.listdir(docs_path):
    file_path = os.path.join(docs_path, file)
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
        documents.append(Document(page_content=text))

# Load local embedding model from Ollama
embedding_model = OllamaEmbeddings(model="nomic-embed-text")

# Create vector store
vectorstore = FAISS.from_documents(
    documents,
    embedding_model
)

# Save vector store locally
vectorstore.save_local("../Tonton RAG Chatbot/vector_store")

print("Vector database saved successfully using Ollama embeddings.")