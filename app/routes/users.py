from fastapi import APIRouter, Depends, Form, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from datetime import timedelta

from app.models import domain, schemas
import app.db as db
from app.services import jwt

domain.users.SqlBase.metadata.create_all(bind=db.database.engine)

router = APIRouter()


@router.post("/", response_model=schemas.token.Token)
async def register_user(
    user: db.schemas.UserCreate,
    session: Session = Depends(db.database.get_session)
):
    if db.users.get_user_by_username(session, user.username):
        raise HTTPException(status_code=409, detail="Username is taken")

    db.users.create_user(session, user)

    access_token_expires = timedelta(minutes=30)
    access_token = jwt.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
