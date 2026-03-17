from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://yashasvi0403.github.io",
        "https://yashasvi0403.github.io/Ai-Stock-News-Analyzer",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class NewsRequest(BaseModel):
    query: str

@app.get("/")
def root():
    return {"message": "Backend is running"}

@app.post("/analyze")
def analyze(data: NewsRequest):
    return {
        "query": data.query,
        "summary": f"Analysis result for: {data.query}"
    }