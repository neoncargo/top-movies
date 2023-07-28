from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# from app.services.img_url import ImgUrl, DEFAULT_FORMAT

from app.services import movies_db_api

TEMPLATES = Jinja2Templates(directory="../templates")

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    movies = await movies_db_api.get_popular()

    movies_template = []
    for i in range(100):
        if i >= len(movies):
            break

        movie = movies[i]

        movies_template.append({"id": movie.id,
                                "image_url": movie.image_url,
                                "title": movie.title})

    return TEMPLATES.TemplateResponse("index.html.jinja",
                                      {"request": request,
                                       "movies": movies_template})
