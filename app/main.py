from contextlib import asynccontextmanager
from fastapi import FastAPI
from .models.base import Base
from .api import user_router, auth_router
from .core.db import engine
from . import models


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        async with engine.begin() as conn:
            # await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)
        yield
    except Exception as error:
        print(error)


app = FastAPI(lifespan=lifespan)


from app.permission import middleware


app.include_router(user_router)
app.include_router(auth_router)
