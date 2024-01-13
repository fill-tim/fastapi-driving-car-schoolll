from pydantic import BaseModel
from fastapi_filter.contrib.sqlalchemy import Filter


class User(BaseModel):
    first_name: str
    last_name: str
    age: int
    # photo: ??
    telegram_user_id: int | None = None
    school_id: int | None = None
    role_id: int | None = None


class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    age: int
    # photo: ??
    telegram_user_id: int | None = None
    school_id: int | None = None
    role_id: int | None = None


class CreateUser(User):
    pass


class UpdateUser(User):
    id: int
    first_name: str | None = None
    last_name: str | None = None
    age: int | None = None
    # photo: ??


class UserFilter(Filter):
    first_name: str | None = None
    age: int | None = None
