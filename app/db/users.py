from sqlalchemy.orm import Session

from app.models import domain, schemas
import app.services.security as security


def get_user_by_id(db: Session, user_id: int):
    return db.query(domain.users.User) \
        .filter(domain.users.User.id == user_id).first()


def get_user_by_username(db: Session, username: str) -> domain.users.User:
    return db.query(domain.users.User) \
        .filter(domain.users.User.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(domain.users.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.users.UserAuthenticate):
    hash = security.hash_password(user.password)
    db_user = domain.users.User(username=user.username, password_hash=hash)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
