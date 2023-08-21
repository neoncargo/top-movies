from pytest_postgresql.factories import postgresql

from app.models.domain.users import User
from app.services import security
# from ..users_repository import UsersRepository



# def test_creation():
#     repo = UsersRepository()

#     user = User(
#         username="test_usernames",
#         password_hash=security.hash_password("test_password")
#     )

#     repo.add(user.username, user.password_hash)
