from fastapi import APIRouter

from app.services import movies_db_api
from app.models.schemas.movies import FullMovieData

router = APIRouter()


@router.get("/movies")
async def search_movies(query: str) -> list[FullMovieData]:
    movies: list[FullMovieData] = await movies_db_api.search(query)

    return movies
