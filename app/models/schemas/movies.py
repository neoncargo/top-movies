from pydantic import BaseModel


class Movie(BaseModel):
    id: str


class FullMovieData(Movie):
    title: str
    description: str
    image_url: str
