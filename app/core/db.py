import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession

from main.app.core.db import init_models

url = f"postgresql+asyncpg://postgres:1234@localhost:5432/drivingCarSchool"
echo = True


engine = create_async_engine(
    url=url,
    echo=echo
)

Base = declarative_base()

async_session = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)

asyncio.run(init_models())
