from fastapi import APIRouter, Form

from pydantic import BaseModel
from datetime import timedelta
from passlib.context import CryptContext

from .login import fake_users_db, create_access_token


class Token(BaseModel):
    access_token: str
    token_type: str


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter()


@router.post("/", response_model=Token)
async def register_user(username: str = Form(), password: str = Form()):
    fake_users_db[username] = {"username": username, "hashed_password": pwd_context.hash(password)}
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
