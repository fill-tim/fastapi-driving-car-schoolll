from fastapi import Depends
from ..core.db import get_async_session
from ..models.lesson import Lesson
from sqlalchemy.ext.asyncio import AsyncSession
from app.repository.base_repo import BaseRepo


class LessonRepo(BaseRepo):
    def __init__(self, db: AsyncSession = Depends(get_async_session)):
        super().__init__(model=Lesson, db=db)
