from main.app.core.db import engine, Base


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all())
        # await conn.run_sync(Base.metadata.drop_all())
