from fastapi import APIRouter

from . import index, users

router = APIRouter()

router.include_router(index.router)
router.include_router(
    users.router,
    prefix="/users"
)
