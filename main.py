import logging
from routers.accounts_router import router

from fastapi import FastAPI

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

app = FastAPI(title= "Finance API")
app.include_router(router)

@app.get("/health")
async def health_check():
    return {"status": "healthy!"}