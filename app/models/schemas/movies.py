from pydantic import BaseModel


class MovieId(BaseModel):
    id: str


class FullMovieData(MovieId):
    title: str
    description: str
    image_url: str
