import pytest
from pytest_postgresql.factories import postgresql
from sqlalchemy import NullPool, create_engine
from sqlalchemy.orm import sessionmaker

from app.models.domain.base import SqlBase

from app.db.users import create_user
from app.models.schemas.users import UserAuthenticate

@pytest.fixture
def db_session(postgresql):
    """Session for SQLAlchemy."""

    connection = f'postgresql+psycopg2://{postgresql.info.user}:@{postgresql.info.host}:{postgresql.info.port}/{postgresql.info.dbname}'

    engine = create_engine(connection, echo=False, poolclass=NullPool)

    TestingSessionLocal = sessionmaker(
       bind=engine
    )

    SqlBase.metadata.create_all(bind=engine)

    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()
