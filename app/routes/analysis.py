from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from openperplex import OpenperplexSync
import os
from dotenv import load_dotenv

router = APIRouter()

# Load environment variables
load_dotenv()
API_KEY = os.getenv("OPENPERPLEX_API_KEY")
if not API_KEY:
    raise ValueError("OPENPERPLEX_API_KEY not set")

client = OpenperplexSync(API_KEY)

class ContentInput(BaseModel):
    topic: str
    content_snippet: str

@router.post("/evaluate-accuracy")
async def evaluate_accuracy(input: ContentInput):
    try:
        result = client.search(
            query=f"Latest developments in {input.topic} to verify: {input.content_snippet}",
            date_context="Today is April 15, 2025",
            location="us",
            model="o3-mini-medium",
            response_language="en",
            answer_type="text",
            search_type="general",
            return_citations=True,
            return_sources=True,
            return_images=False,
            recency_filter="month"
        )
        llm_response = result.get("llm_response", "")
        accuracy = "likely_accurate" if input.content_snippet.lower() in llm_response.lower() else "needs_review"
        return {
            "accuracy": accuracy,
            "response": llm_response,
            "sources": result.get("sources", []),
            "relevant_questions": result.get("relevant_questions", [])
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Evaluation failed: {str(e)}")

@router.get("/test-api-key")
async def test_api_key():
    try:
        result = client.search(
            query="Test API key for EdTech",
            date_context="Today is April 15, 2025",
            location="us",
            model="o3-mini-medium",
            response_language="en",
            answer_type="text"
        )
        return {"status": "success", "response": result.get("llm_response", "No response")}
    except Exception as e:
        return {"status": "failed", "error": str(e)}