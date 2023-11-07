from typing import Annotated

from fastapi import APIRouter, Security
from fastapi.encoders import jsonable_encoder
from src.database import fake_items_db
from src.models import Item, ItemForm, User
from src.routers.security import get_current_user

router = APIRouter(
    prefix="/items",
    tags=["items"],
    dependencies=[Security(get_current_user)],
    responses={404: {"description": "Not found"}},
)


@router.get("/me/")
async def read_own_items(current_user: Annotated[User, Security(get_current_user, scopes=["reader"])]):
    # Select in database
    return [i for i in fake_items_db if i["owner"] == current_user.username]


@router.post("/me/", response_model=Item)
async def add_new_item(i: ItemForm, current_user: Annotated[User, Security(get_current_user, scopes=["writer"])]):
    created = Item(item_id=i.item_id, owner=current_user.username)
    # Insert item in database
    fake_items_db.append(jsonable_encoder(created))
    return created


@router.get("/")
async def read_all_items(_: Annotated[User, Security(get_current_user, scopes=["admin"])]):
    return fake_items_db
