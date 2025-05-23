from fastapi import FastAPI
import uvicorn

from api.v1 import health
from core.settings import settings


app = FastAPI()
app.include_router(health.router)


if __name__ == "__main__":
    uvicorn.run(app, host=settings.APP_HOST, port=settings.APP_PORT)
