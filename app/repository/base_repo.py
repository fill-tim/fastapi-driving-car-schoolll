from sqlalchemy import update, select, delete


class BaseRepo:
    def __init__(self, model, db) -> None:
        self.model = model
        self.db = db

    async def get_one(self, id: int):
        obj = await self.db.execute(select(self.model).filter_by(id=id))
        return obj.scalar()

    async def get_all(self, filter_query):
        objs = await self.db.execute(
            select(self.model).filter_by(**filter_query.model_dump(exclude_unset=True))
        )
        return list(objs.scalars())

    async def create(self, obj_in):
        obj = self.model(**obj_in.model_dump())

        self.db.add(obj)
        await self.db.commit()
        await self.db.refresh(obj)

        return obj

    async def update(self, obj_upd):
        updated_obj = await self.db.execute(
            update(self.model)
            .filter_by(id=obj_upd.id)
            .values(obj_upd.model_dump(exclude_unset=True))
        )
        await self.db.commit()
        return updated_obj

    async def delete(self, id: int):
        deleted_obj = await self.db.execute(delete(self.model).filter_by(id=id))
        await self.db.commit()
        return deleted_obj
