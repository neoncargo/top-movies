import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv

from app.api.routes import api

app = FastAPI(
    swagger_ui_parameters={
        "displayRequestDuration": True,
    },
    root_path="/api/v1",
    redirect_slashes=False
)

app.include_router(api.router)

if __name__ == "__main__":
    load_dotenv()
    uvicorn.run(app)
