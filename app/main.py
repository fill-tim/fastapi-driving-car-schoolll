from contextlib import asynccontextmanager
from fastapi import FastAPI
from .models.base import Base
from .api.user import user_router
from .core.db import engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)


app.include_router(user_router)
