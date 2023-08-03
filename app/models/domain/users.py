from sqlalchemy import Column, Integer, String

from .base import SqlBase


class User(SqlBase):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password_hash = Column(String)
