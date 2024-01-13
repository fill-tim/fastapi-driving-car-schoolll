from fastapi import Depends
from ..core.db import get_async_session
from ..models.telegram_user import TelegramUser
from sqlalchemy.ext.asyncio import AsyncSession
from app.repository.base_repo import BaseRepo


class TelegramUserRepo(BaseRepo):
    def __init__(self, db: AsyncSession = Depends(get_async_session)):
        super().__init__(model=TelegramUser, db=db)
