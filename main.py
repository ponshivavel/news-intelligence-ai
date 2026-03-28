from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from agents.data_agent import get_news
from agents.summary_agent import summarize_news
from agents.chat_agent import chat_with_news
from agents.timeline_agent import generate_timeline

app = FastAPI(title="AI News Brain", version="2.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    query: str


@app.get("/news")
def fetch_news():
    """Returns AI-generated summary + raw articles."""
    try:
        news = get_news()
        summary = summarize_news(news)
        return {"summary": summary, "articles": news}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/chat")
def chat(request: ChatRequest):
    """Accepts a user question and returns an AI-generated response."""
    try:
        response = chat_with_news(request.query)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/timeline")
def get_timeline():
    """Returns an AI-generated chronological market event timeline."""
    try:
        news = get_news()
        timeline = generate_timeline(news)
        return {"timeline": timeline}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
