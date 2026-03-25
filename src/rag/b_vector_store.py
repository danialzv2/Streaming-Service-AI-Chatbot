from langchain_huggingface import HuggingFaceEmbeddings
import ssl
from langchain_community.vectorstores import FAISS

ssl._create_default_https_context = ssl._create_unverified_context

from langchain_ollama import OllamaEmbeddings

def load_embedding_model():
    """
    Load local embedding model using Ollama.
    """
    embedding_model = OllamaEmbeddings(model="nomic-embed-text")
    return embedding_model


def load_vector_store():

    embedding_model = load_embedding_model()

    vectorstore = FAISS.load_local(
        r"../vector_store",
        embedding_model,
        allow_dangerous_deserialization=True
    )

    return vectorstore