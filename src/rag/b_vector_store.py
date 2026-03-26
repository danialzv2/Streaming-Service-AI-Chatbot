import ssl
import os
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

ssl._create_default_https_context = ssl._create_unverified_context


def load_embedding_model():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


def load_vector_store():

    embedding_model = load_embedding_model()

    vectorstore = FAISS.load_local(
        folder_path="vector_store",
        embeddings=embedding_model,
        allow_dangerous_deserialization=True
    )
    return vectorstore

