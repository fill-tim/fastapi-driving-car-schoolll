from fastapi import Depends
from sqlalchemy import select
from app.repository.base_repo import BaseRepo
from app.core.db import get_async_session
from app.models.user import User
from sqlalchemy.ext.asyncio import AsyncSession


class AuthRepo(BaseRepo):
    def __init__(self, db: AsyncSession = Depends(get_async_session)):
        super().__init__(model=User, db=db)

    async def find_user_by_phone_number(self, phone_number):
        user = await self.db.execute(
            select(self.model).filter_by(phone_number=phone_number)
        )
        return user.scalar()
