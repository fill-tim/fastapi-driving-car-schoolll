from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, async_session, AsyncSession
from .config import settings

engine = create_async_engine(settings.url, echo=settings.echo)
async_session_maker = async_session(engine)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
