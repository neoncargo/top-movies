from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models import domain

SQLALCHEMY_DATABASE_URL = \
    "postgresql://myuser:sd$2j6Asd34@localhost/top_movies"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

domain.users.SqlBase.metadata.create_all(bind=engine)


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
