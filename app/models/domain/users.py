from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

SqlBase = declarative_base()


class User(SqlBase):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password_hash = Column(String)
