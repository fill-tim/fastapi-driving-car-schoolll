from sqlalchemy import select
from sqlalchemy.engine import Result
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.user import ListUsers
from core.db import get_async_session
from models import User

user_router = APIRouter(tags=["users"])


@user_router.get("/users/", response_model=ListUsers)
async def get_list(session: AsyncSession = Depends(get_async_session)):
    stmt = select(User)
    print(session)
    result: Result = await session.execute(stmt)
    tests = result.scalars().all()
    return list(tests)
