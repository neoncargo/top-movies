from sqlalchemy import Column, Integer, String

from .base import SqlBase


class Favorite(SqlBase):
    __tablename__ = "favorites"

    user_id = Column(Integer, primary_key=True)
    movie_id = Column(String, primary_key=True)
