from fastapi.testclient import TestClient

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.models.schemas.users import UserAuthenticate

from app.main import app
from app.db.database import get_session
from app.models.domain.base import SqlBase
from app.services import jwt

SQLALCHEMY_DATABASE_URL = "sqlite://"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

SqlBase.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_session] = override_get_db

client = TestClient(app)


def test_register_user():
    user = UserAuthenticate(
        username="test_username",
        password="test_password",
    )

    response = client.post(
        "/users",
        json=user.dict()
    )

    assert response.status_code == 200

    response = response.json()

    assert \
        jwt.get_username_from_token(response["access_token"]) == \
        user.username
