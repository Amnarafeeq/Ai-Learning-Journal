from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from datetime import datetime, UTC
from uuid import uuid4

app = FastAPI(
    title="DACA Chatbot API",
    description="A FastAPI-based API for a chatbot in the DACA tutorial series",
    version="0.1.0",
)

class Metadata(BaseModel):
    timestamp: datetime = Field(default_factory=lambda: datetime.now(tz=UTC))
    session_id: str = Field(default_factory=lambda: str(uuid4()))

class Message(BaseModel):
    user_id: str
    text: str
    metadata: Metadata | None = None  
    tags: list[str] | None = None     

class Response(BaseModel):
    user_id: str
    reply: str
    metadata: Metadata

@app.get("/")
async def root():
    return {"message": "Welcome to the DACA Chatbot API! Access /docs for the API documentation."}

@app.get("/users/{user_id}")
async def get_user(user_id: str, role: str | None = None):
    user_info = {"user_id": user_id, "role": role if role else "guest"}
    return user_info

@app.post("/chat/", response_model=Response)
async def chat(message: Message):
    if not message.text.strip():
        raise HTTPException(status_code=400, detail="Message text cannot be empty")

    if message.metadata is None:
        message.metadata = Metadata()

    reply_text = f"Hi {message.user_id} 👋! Thanks for your message: '{message.text}'. Let me know how I can help!"

    return Response(
        user_id=message.user_id,
        reply=reply_text,
        metadata=message.metadata
    )
