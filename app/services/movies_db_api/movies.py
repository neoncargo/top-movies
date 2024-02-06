import os
import logging as log

import aiohttp
from aiohttp.client_exceptions import ClientError

from fastapi import HTTPException

from app.models.schemas.movies import FullMovieData

MOVIES_API_TOKEN = os.environ["MOVIES_API_TOKEN"]


async def _get_json(session: aiohttp.ClientSession, url: str):
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer " + MOVIES_API_TOKEN
    }

    api_exception = HTTPException(
        status_code=503,
        detail="Movies API not available"
    )

    try:
        async with session.get(url, headers=headers) as response:
            if response.status != 200:
                raise api_exception

            return await response.json()
    except ClientError as e:
        log.warn(e)
        raise api_exception


async def get_popular() -> list[FullMovieData]:
    URL = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"

    response_json: dict
    async with aiohttp.ClientSession() as session:
        response_json = await _get_json(session, URL)

    result: list[FullMovieData] = []
    for movie in response_json["results"]:
        result.append(FullMovieData(
            id=movie["id"],
            title=movie["title"],
            description=movie["overview"],
            image_url=construct_image_url(movie["poster_path"])
        ))

    return result


def construct_image_url(poster_path: str | None):
    if poster_path is None:
        return None

    return "/images/t/p/w500" + poster_path


async def get_movie(id: str) -> FullMovieData:
    URL = "https://api.themoviedb.org/3/movie/" + id

    response_json: dict
    async with aiohttp.ClientSession() as session:
        response_json = await _get_json(session, URL)

    assert id == str(response_json["id"])

    result = FullMovieData(
        id=response_json["id"],
        title=response_json["title"],
        description=response_json["overview"],
        image_url=construct_image_url(response_json["poster_path"])
    )

    return result


async def search(query: str) -> list[FullMovieData]:
    URL = "https://api.themoviedb.org/3/search/movie?query=" + query

    response_json: dict
    async with aiohttp.ClientSession() as session:
        response_json = await _get_json(session, URL)

    result: list[FullMovieData] = []
    for movie in response_json["results"]:
        result.append(FullMovieData(
            id=movie["id"],
            title=movie["title"],
            description=movie["overview"],
            image_url=construct_image_url(movie["poster_path"])
        ))

    return result
