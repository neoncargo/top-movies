from app.models import schemas, domain
from sqlalchemy.orm import Session


def add_favorite_movie_to_user(
    db: Session,
    user: schemas.users.User,
    movie: schemas.movies.MovieId
):
    favorite_entry = domain.favorites.Favorite(
        user_id=user.id,
        movie_id=movie.id
    )

    db.add(favorite_entry)
    db.commit()
    db.refresh(favorite_entry)


def delete_favorite_movie_from_user(
    db: Session,
    user: schemas.users.User,
    movie: schemas.movies.MovieId
):
    db.query(domain.favorites.Favorite) \
        .filter(
            domain.favorites.Favorite.user_id == user.id,
            domain.favorites.Favorite.movie_id == movie.id
        ) \
        .delete()

    db.commit()


def get_favorites_movies_for_user(
    db: Session,
    user: schemas.users.User
) -> list[schemas.movies.MovieId]:
    favorites = db.query(domain.favorites.Favorite) \
        .filter(
            domain.favorites.Favorite.user_id == user.id
        ) \
        .all()

    result: list[schemas.movies.MovieId] = []
    for favorite in favorites:
        result.append(schemas.movies.MovieId(id=str(favorite.movie_id)))

    return result
