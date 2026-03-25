import os
from langchain_core.documents import Document
from langchain_community.vectorstores.lancedb import LanceDB 
from langchain_community.embeddings import HuggingFaceEmbeddings

documents = []

# Load documents
docs_path = "../Tonton RAG Chatbot/rag_docs"

for file in os.listdir(docs_path):
    file_path = os.path.join(docs_path, file)
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
        documents.append(Document(page_content=text))

# Load local embedding model from Ollama
# embedding_model = OllamaEmbeddings(model="nomic-embed-text")
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"token": os.getenv("HF_TOKEN")}
)
# Create vector store
vectorstore = LanceDB.from_documents(
    documents=documents,
    embedding=embedding_model,
    uri="../Tonton RAG Chatbot/vector_store"
)

print("Vector database saved successfully using Ollama embeddings.")