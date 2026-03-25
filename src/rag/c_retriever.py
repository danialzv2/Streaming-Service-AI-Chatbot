from rag.b_vector_store import load_vector_store

def get_retriever():

    vectorstore = load_vector_store()

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 2}
    )

    return retriever

