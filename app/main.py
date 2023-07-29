import uvicorn
from fastapi import FastAPI

from app.api.routes import api

app = FastAPI(
    swagger_ui_parameters={
        "displayRequestDuration": True,
    }
)

app.include_router(api.router)

if __name__ == "__main__":
    uvicorn.run(app, root_path="/api/v1")
