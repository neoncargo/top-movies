from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.services import movies_db_api
from app.models.schemas.movies import FullMovieData

TEMPLATES = Jinja2Templates(directory="../templates")

router = APIRouter()


@router.get("/{movie_id}", response_class=HTMLResponse)
async def read_movie(request: Request, movie_id: str):
    movie: FullMovieData = await movies_db_api.get_movie(movie_id)

    return TEMPLATES.TemplateResponse(
        "movie.html.jinja",
        {
            "request": request,
            "image_url": movie.image_url,
            "title": movie.title,
            "description": movie.description,
        }
    )
