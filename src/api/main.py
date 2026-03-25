from fastapi import FastAPI
from rag.e_explanation_service import ask_rag
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all origins (dev mode)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model output data
@app.post("/chat")
def chat(data: dict):

    question = data["message"]

    answer = ask_rag(question)

    return {
        "response": answer
    }

