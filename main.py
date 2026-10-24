from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
import uvicorn

app = FastAPI(
    title="AI Feature API",
    description="Clean backend API exposing AI capabilities for easy integration",
    version="1.0.0"
)

class TextRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=5000)
    language: Optional[str] = "en"

class SummarizeResponse(BaseModel):
    summary: str
    original_length: int
    summary_length: int

class ClassifyResponse(BaseModel):
    label: str
    confidence: float
    categories: list[str]

class AskResponse(BaseModel):
    answer: str
    model: str = "demo-llm"

@app.get("/health")
def health():
    return {"status": "healthy", "service": "ai-feature-api"}

@app.post("/summarize", response_model=SummarizeResponse)
def summarize(req: TextRequest):
    # In production → call LLM here
    words = req.text.split()
    summary = " ".join(words[: max(1, len(words)//4) ]) + "..."
    
    return SummarizeResponse(
        summary=summary,
        original_length=len(req.text),
        summary_length=len(summary)
    )

@app.post("/classify", response_model=ClassifyResponse)
def classify(req: TextRequest):
    # Simple rule-based demo. Replace with real model.
    text_lower = req.text.lower()
    if any(w in text_lower for w in ["claim", "insurance", "policy"]):
        label = "insurance"
    elif any(w in text_lower for w in ["loan", "emi", "interest"]):
        label = "loan"
    else:
        label = "general"

    return ClassifyResponse(
        label=label,
        confidence=0.82,
        categories=["insurance", "loan", "general", "support"]
    )

@app.post("/ask", response_model=AskResponse)
def ask(req: TextRequest):
    # Production: call your LLM + RAG here
    return AskResponse(
        answer=f"This is a placeholder answer for: '{req.text[:80]}...'. Connect a real LLM for production use.",
        model="demo-llm"
    )

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
