from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session

from app.models import schemas
import app.db as db
from app.services import jwt, security

router = APIRouter()


RESPONSE_401 = {
    "content": {
        "application/json": {
            "example": {"detail": "Incorrect username or password"},
        }
    },
}
RESPONSE_409 = {
    "content": {
        "application/json": {
            "example": {"detail": "Username is taken"},
        }
    },
}


@router.post(
    "/login",
    response_model=schemas.token.Token,
    responses={
        401: RESPONSE_401,
    },
)
def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: Session = Depends(db.database.get_session)
):
    wrong_login_error = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"},
    )

    user = db.users.get_user_by_username(session, form_data.username)
    if not user:
        raise wrong_login_error

    if not security.verify_password(
        form_data.password,
        str(user.password_hash)
    ):
        raise wrong_login_error

    access_token = jwt.create_access_token(data={"sub": user.username})
    return {"access_token": access_token}


@router.post(
    "",
    response_model=schemas.token.Token,
    responses={
        409: RESPONSE_409,
    },
)
async def register_user(
    user: schemas.users.UserAuthenticate,
    session: Session = Depends(db.database.get_session)
):
    if db.users.get_user_by_username(session, user.username):
        raise HTTPException(status_code=409, detail="Username is taken")

    db.users.create_user(session, user)

    access_token = jwt.create_access_token(data={"sub": user.username})
    return {"access_token": access_token}
