from ..schemas.user import CreateUser
from fastapi import Depends
from ..core.db import get_async_session
from ..models.user import User
from sqlalchemy.ext.asyncio import AsyncSession


class UserRepo:
    db: AsyncSession

    def __init__(self, db: AsyncSession = Depends(get_async_session)):
        self.db = db

    async def get_one_user_by_id(self):
        pass

    async def get_all_user(self):
        pass

    async def create_user(self, user_in: CreateUser):
        user = User(**user_in.model_dump())
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user
