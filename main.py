import logging
from controller.accounts_controller import router

from fastapi import FastAPI

logger = logging.getLogger(__name__)

app = FastAPI(title= "Finance API")
app.include_router(router)

@app.get("/health")
async def health_check():
    return {"status": "healthy!"}