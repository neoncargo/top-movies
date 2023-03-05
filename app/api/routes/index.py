from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import httpx

from app.services.img_url import ImgUrl, DEFAULT_FORMAT

TEMPLATES = Jinja2Templates(directory="../templates")
MOST_POPULAR_URL = "https://imdb-api.com/en/API/MostPopularMovies/k_ofriojs4"

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    async with httpx.AsyncClient() as client:
        response = await client.get(MOST_POPULAR_URL)
        response = response.json()

        movies = []
        for i in range(100):
            movie = response["items"][i]
            image_url = ImgUrl(movie["image"]).serialize(DEFAULT_FORMAT)
            movies.append({"image_url": image_url, "title": movie["title"]})

    return TEMPLATES.TemplateResponse("index.html.jinja",
                                      {"request": request, "movies": movies})
