from fastapi import FastAPI

from routers import index, login

app = FastAPI()


app.include_router(index.router)
app.include_router(
    login.router,
    prefix="/login",
)
