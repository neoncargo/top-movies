from typing import Annotated
from sqlalchemy.orm import Session

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

import app.db as db
from app.models import schemas
from app.services import jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/login")


def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    session: Annotated[Session, Depends(db.database.get_session)]
) -> schemas.users.User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    username = jwt.get_username_from_token(token)
    if username is None:
        raise credentials_exception

    user = db.users.get_user_by_username(session, username)
    if not user:
        raise credentials_exception

    return user
