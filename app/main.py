from fastapi import FastAPI

from routers.index import index
from routers import login, users

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
