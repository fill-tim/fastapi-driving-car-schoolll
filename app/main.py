from contextlib import asynccontextmanager
from fastapi import FastAPI
from core.db import data_base
from models import Base

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with data_base.engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
