from fastapi import FastAPI, Request
from pydantic import BaseModel
from transformers import pipeline, set_seed

app = FastAPI()
chat = pipeline("text-generation", model="gpt2")
set_seed(42)

class ChatRequest(BaseModel):
    prompt: str

@app.post("/chat")
async def converse(req: ChatRequest):
    result = chat(req.prompt, max_length=150, do_sample=True, top_p=0.95, top_k=50)
    return {"response": result[0]["generated_text"]}
