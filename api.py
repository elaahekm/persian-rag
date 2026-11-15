from fastapi import FastAPI
from pydantic import BaseModel

from ask import ask

app = FastAPI(title="persian-rag")


class Question(BaseModel):
    question: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/ask")
def ask_endpoint(body: Question):
    return {"answer": ask(body.question)}