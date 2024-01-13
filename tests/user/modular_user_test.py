from fastapi import Depends
import pytest
from conftest import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from app.repository.user_repo import UserRepo
from conftest import User, async_session_maker

@pytest.mark.asyncio(scope="session")
async def test_get_by_id():
    async with AsyncSession() as db: 
        async with db.begin():
            
            user_repo = UserRepo(db)
            print(user_repo)
            user = await user_repo.get_by_id(1)
            print(user)
            assert user.id == 1
