from jose import jwt

ALGORITHM = "HS256"
SECRET_KEY = "8b796cf46e23c63c3db544ba897fc280680ae753d846a136cf00fb4054fa31c4"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire_timepoint = datetime.utcnow() + \
        timedelta(days=ACCESS_TOKEN_EXPIRE_DAYS)

    to_encode.update({"exp": expire_timepoint})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
