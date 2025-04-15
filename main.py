from fastapi import FastAPI
from app.routes.analysis import router

app = FastAPI(
    title="AI-Powered Content Updates",
    description="Hybrid AI and human review system for EdTech content",
    version="0.1.0"
)

app.include_router(router, prefix="/api")

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
