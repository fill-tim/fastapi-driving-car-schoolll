from fastapi import Depends
from ..core.db import get_async_session
from ..models.city import City
from sqlalchemy.ext.asyncio import AsyncSession
from app.repository.base_repo import BaseRepo


class CityRepo(BaseRepo):
    def __init__(self, db: AsyncSession = Depends(get_async_session)):
        super().__init__(model=City, db=db)