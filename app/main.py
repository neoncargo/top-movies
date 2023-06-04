from fastapi import FastAPI

from app.api.routes import api

app = FastAPI()

app.include_router(api.router)
