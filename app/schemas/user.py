from pydantic import BaseModel
from typing import List


class User(BaseModel):
    first_name: str
    last_name: str
    age: int


class ListUsers(BaseModel):
    items: List[User]


class CreateUser(User):
    pass
