from typing import Annotated
import asyncio
from sqlalchemy.orm import Session

from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation

from fastapi import APIRouter, Depends, status, Response

from app.models import schemas
import app.db as db
from app.api.dependencies.authentication import get_current_user
from app.services import movies_db_api

router = APIRouter()


@router.put("/favorites/{movie_id}", status_code=status.HTTP_201_CREATED)
def add_favorite_movie(
    movie_id: str,
    user: Annotated[schemas.users.User, Depends(get_current_user)],
    session: Annotated[Session, Depends(db.database.get_session)],
    response: Response
):
    try:
        db.favorites.add_favorite_movie_to_user(
            session,
            user,
            schemas.movies.MovieId(id=movie_id)
        )
    except IntegrityError as e:
        if isinstance(e.orig, UniqueViolation):
            session.rollback()
            response.status_code = status.HTTP_200_OK
            return


@router.delete("/favorites/{movie_id}", status_code=status.HTTP_200_OK)
def delete_favorite_movie(
    movie_id: str,
    user: Annotated[schemas.users.User, Depends(get_current_user)],
    session: Annotated[Session, Depends(db.database.get_session)]
):
    db.favorites.delete_favorite_movie_from_user(
        session,
        user,
        schemas.movies.MovieId(id=movie_id)
    )


@router.get("/favorites")
async def get_favorite_movies(
    user: Annotated[schemas.users.User, Depends(get_current_user)],
    session: Annotated[Session, Depends(db.database.get_session)]
) -> list[schemas.movies.FullMovieData]:
    fav_movie_ids: list[schemas.movies.MovieId] = \
        db.favorites.get_favorites_movies_for_user(
            session,
            user
        )

    result = []
    for movie in fav_movie_ids:
        result.append(movies_db_api.get_movie(movie.id))

    result = await asyncio.gather(*result)

    return result
