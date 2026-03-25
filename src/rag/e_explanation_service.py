from src.rag.d_rag_chain import build_rag_chain

chain, retriever = build_rag_chain()

def ask_rag(question):

    docs = retriever.invoke(question)

    context = "\n".join([doc.page_content for doc in docs])

    return chain.invoke({
        "context": context,
        "question": question
    })



def ask_tonton(question):

    # --- GUARDRAILS ---
    blocked_keywords = [
        "hack", "bypass", "curi", "seks", "porn",
        "kad kredit", "kad bank", "maklumat sensitif"
    ]

    lower_q = question.lower()
    if any(word in lower_q for word in blocked_keywords):
        return "Maaf, permintaan ini tidak dibenarkan."

    # --- SAFE → Continue to RAG ---
    return ask_rag(question)