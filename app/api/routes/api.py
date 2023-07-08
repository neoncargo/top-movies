from fastapi import APIRouter

from . import index, users, movies, me

router = APIRouter()

router.include_router(index.router)
router.include_router(
    users.router,
    prefix="/users"
)
router.include_router(
    movies.router,
    prefix="/movies"
)
router.include_router(
    me.router,
    prefix="/me"
)
