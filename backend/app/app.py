import uvicorn
from fastapi import FastAPI
from app.chat import chat_route
from config.config import settings

app = FastAPI()

app.include_router(chat_route)


if __name__ == '__main__':

    uvicorn.run(app, host=settings.app_host, port=settings.app_port)