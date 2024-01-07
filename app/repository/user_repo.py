from ..schemas.user import CreateUser, UpdateUser
from fastapi import Depends
from ..core.db import get_async_session
from ..models.user import User
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete, update


class UserRepo:
    db: AsyncSession

    def __init__(self, db: AsyncSession = Depends(get_async_session)):
        self.db = db

    async def get_by_id(self, id: int):
        user = await self.db.execute(select(User).filter_by(id=id))
        return user.scalar()

    async def get_all(self):
        users = await self.db.execute(select(User))
        return list(users.scalars())

    async def create(self, user_in: CreateUser):
        user = User(**user_in.model_dump())

        self.db.add(user)

        await self.db.commit()
        await self.db.refresh(user)
        return user

    async def update(self, user_upd: UpdateUser):
        updated_user = await self.db.execute(
            update(User)
            .filter_by(id=user_upd.id)
            .values(user_upd.model_dump(exclude_unset=True))
        )
        await self.db.commit()
        return updated_user

    async def delete(self, id: int):
        deleted_user = await self.db.execute(delete(User).filter_by(id=id))
        await self.db.commit()
        return deleted_user
