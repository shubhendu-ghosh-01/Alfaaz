from fastapi import FastAPI
from routes.shayri import router as shayri_router

app = FastAPI(
    title="Alfaaz - Shayri Generator",
    description="Generate emotional Shayri using Gemini API.",
    version="1.0.0"
)

app.include_router(shayri_router, prefix="/api/v1/shayri", tags=["Shayri"])
