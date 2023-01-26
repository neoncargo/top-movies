from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import httpx

app = FastAPI()

TEMPLATES = Jinja2Templates(directory="templates")

MOST_POPULAR_URL = "https://imdb-api.com/en/API/MostPopularMovies/k_ofriojs4"


def insert_quality(url: str) -> str:
    i = url.find("_V1_")
    if i == -1:
        raise ValueError("Didn't found in: " + url)

    return url[:(i + 4)] + "QL10_" + url[(i + 4):]


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    async with httpx.AsyncClient() as client:
        response = await client.get(most_popular_url)
        response = response.json()

        movies = []
        for i in range(100):
            movie = response["items"][i]
            image_url = insert_quality(movie["image"])
            movies.append({"image_url": image_url, "title": movie["title"]})

    return templates.TemplateResponse("index.html.jinja", {"request": request, "movies": movies})
