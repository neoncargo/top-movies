from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import httpx

from app.services.img_url import ImgUrl, DEFAULT_FORMAT

TEMPLATES = Jinja2Templates(directory="../templates")
MOVIE_URL_BASE = "https://imdb-api.com/en/API/Title/k_ofriojs4/"

router = APIRouter()


@router.get("/{movie_id}", response_class=HTMLResponse)
async def read_movie(request: Request, movie_id: str):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(MOVIE_URL_BASE + movie_id)
        except httpx.RequestError as e:
            print(f"Can't get \"{MOVIE_URL_BASE}\": {e}")
            raise HTTPException(
                status_code=503,
                detail="IMDB API not available"
            )

        response = response.json()

    try:
        image_url = ImgUrl(response["image"]).serialize(DEFAULT_FORMAT)
    except ValueError as e:
        print(f"Can't build ImgUrl: {e}")
        image_url = ""

    return TEMPLATES.TemplateResponse(
        "movie.html.jinja",
        {
            "request": request,
            "image_url": image_url,
            "title": response["fullTitle"],
            "description": response["plot"],
        }
    )
