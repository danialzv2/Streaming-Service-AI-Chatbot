from langchain_huggingface import HuggingFaceEmbeddings
import ssl
from langchain_community.vectorstores import FAISS
from langchain_community.vectorstores import Chroma

ssl._create_default_https_context = ssl._create_unverified_context

from langchain_ollama import OllamaEmbeddings

def load_embedding_model():

    # embedding_model = OllamaEmbeddings(model="nomic-embed-text")
    embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return embedding_model


def load_vector_store():

    embedding_model = load_embedding_model()

    vectorstore = Chroma(
        persist_directory="vector_store",
        embedding_function=embedding_model
    )

    return vectorstore
