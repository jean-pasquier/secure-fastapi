from typing import List, Union

from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    type: str


class UserInDB(User):
    hashed_password: str
    created_by: str = "unknown"


class ItemForm(BaseModel):
    item_id: str


class Item(ItemForm):
    owner: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None
    scopes: List[str] = []
