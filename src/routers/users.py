from typing import Annotated

from fastapi import APIRouter, Security
from fastapi.encoders import jsonable_encoder
from passlib import pwd
from src.database import fake_users_db
from src.models import User, UserInDB
from src.routers.security import get_current_user, get_password_hash

router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Security(get_current_user)],
    responses={404: {"description": "Not found"}},
)


@router.get("/me/", response_model=User)
async def read_users_me(current_user: Annotated[User, Security(get_current_user, scopes=["me"])]):
    return current_user


@router.post("/")
async def add_user(u: User, current_user: Annotated[User, Security(get_current_user, scopes=["admin"])]):
    password = pwd.genword()
    new_user_db = UserInDB(
        **jsonable_encoder(u.model_copy()), hashed_password=get_password_hash(password), created_by=current_user.username
    )

    # Insert user in database
    fake_users_db[new_user_db.username] = jsonable_encoder(new_user_db)

    # Returns to admin the clear password
    return {"username": new_user_db.username, "password": password}
