from pydantic import BaseModel


class Movie(BaseModel):
    id: str
