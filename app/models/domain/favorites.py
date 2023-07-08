from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

SqlBase = declarative_base()


class Favorite(SqlBase):
    __tablename__ = "favorites"

    user_id = Column(Integer, primary_key=True)
    movie_id = Column(String, primary_key=True)
