from fastapi import Depends
from ..core.db import get_async_session
from ..models.lesson_type import LessonType
from sqlalchemy.ext.asyncio import AsyncSession
from app.repository.base_repo import BaseRepo


class LessonTypeRepo(BaseRepo):
    def __init__(self, db: AsyncSession = Depends(get_async_session)):
        super().__init__(model=LessonType, db=db)