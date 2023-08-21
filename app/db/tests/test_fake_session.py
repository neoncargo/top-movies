import pytest
from pytest_postgresql.factories import postgresql
from sqlalchemy import NullPool, create_engine
from sqlalchemy.orm import sessionmaker

from app.models.domain.base import SqlBase

from app.db.users import create_user, get_user_by_username
from app.models.schemas.users import UserAuthenticate

from .fake_session import db_session


def test_db_session(db_session):
    user = UserAuthenticate(
        username="test_username",
        password="test_password",
    )

    create_user(db_session, user)

    got_user = get_user_by_username(db_session, user.username)

    print(got_user.username, got_user.password_hash, sep=' ')

    assert got_user is not None
