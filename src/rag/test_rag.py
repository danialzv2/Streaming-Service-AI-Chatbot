from src.rag.e_explanation_service import ask_tonton

while True:
    question = input("\nAsk Tonton Support > ")

    if question.lower() in ["exit", "quit"]:
        break

    answer = ask_tonton(question)
    print("\nAnswer:", answer)