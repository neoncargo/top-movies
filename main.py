from fastapi import FastAPI, Request, Depends, HTTPException, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import httpx

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

app = FastAPI()

TEMPLATES = Jinja2Templates(directory="templates")

MOST_POPULAR_URL = "https://imdb-api.com/en/API/MostPopularMovies/k_ofriojs4"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

USERS_DB = {
    "johndoe": {
        "username": "johndoe",
        "hashed_password": "fakehashedsecret",
    },
    "alice": {
        "username": "alice",
        "hashed_password": "fakehashedsecret2",
    },
}


def fake_hash_password(password: str):
    return "fakehashed" + password


class User(BaseModel):
    username: str
    hashed_password: str


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return User(**user_dict)


def fake_decode_token(token):
    # This doesn't provide any security at all
    # Check the next version
    user = get_user(USERS_DB, token)
    return user


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = USERS_DB.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = User(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}


@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user


# --------------------------------------------
def insert_quality(url: str) -> str:
    i = url.find("_V1_")
    if i == -1:
        raise ValueError("Didn't found in: " + url)

    return url[:(i + 4)] + "QL60_" + url[(i + 4):]


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    async with httpx.AsyncClient() as client:
        response = await client.get(MOST_POPULAR_URL)
        response = response.json()

        movies = []
        for i in range(100):
            movie = response["items"][i]
            image_url = movie["image"]
            movies.append({"image_url": image_url, "title": movie["title"]})

    return TEMPLATES.TemplateResponse("index.html.jinja", {"request": request, "movies": movies})
# --------------------------------------------
