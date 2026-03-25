import ssl
import os
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores.lancedb import LanceDB

ssl._create_default_https_context = ssl._create_unverified_context


def load_embedding_model():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"token": os.getenv("HF_TOKEN")}
    )


def load_vector_store():
    embedding_model = load_embedding_model()

    vectorstore = LanceDB(
        uri="../Tonton RAG Chatbot/vector_store",
        embedding=embedding_model
    )
    return vectorstore