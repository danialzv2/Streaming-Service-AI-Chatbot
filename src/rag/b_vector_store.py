from langchain_community.embeddings import HuggingFaceEmbeddings
import ssl
from langchain_community.vectorstores import LanceDB
import os

ssl._create_default_https_context = ssl._create_unverified_context

def load_embedding_model():

    # embedding_model = OllamaEmbeddings(model="nomic-embed-text")
    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"token": os.getenv("HF_TOKEN")}
    )

    return embedding_model

def load_vector_store():

    embedding_model = load_embedding_model()

    vectorstore = LanceDB.from_uri(
        uri="vector_store",
        embedding=embedding_model
    )

    return vectorstore
