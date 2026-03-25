import os
from langchain_ollama import OllamaEmbeddings
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

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
# embedding_model = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/all-MiniLM-L6-v2"
# )

# Create vector store

vectorstore = Chroma.from_documents(
    documents=documents,
    embedding=embedding_model,
    persist_directory="../Tonton RAG Chatbot/vector_store"
)

# Save vector store locally
vectorstore.persist()

print("Vector database saved successfully using Ollama embeddings.")