from fastapi import Depends
from ..core.db import get_async_session
from ..models.user import User
from sqlalchemy.ext.asyncio import AsyncSession
from app.repository.base_repo import BaseRepo


class UserRepo(BaseRepo):
    def __init__(self, db: AsyncSession = Depends(get_async_session)):
        super().__init__(model=User, db=db)
