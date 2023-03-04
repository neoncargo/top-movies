from fastapi import FastAPI

from routes import index, login, users

app = FastAPI()


app.include_router(index.router)
app.include_router(
    login.router,
    prefix="/login",
)

app.include_router(
    users.router,
    prefix="/users",
)
