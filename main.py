import logging

from fastapi import FastAPI

logger = logging.getLogger(__name__)

app = FastAPI(title= "Finance API")

@app.get("/health")
async def health_check():
    return {"status": "healthy!"}