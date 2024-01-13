from ..repository.user_repo import UserRepo
from ..schemas.user_schema import CreateUser, UpdateUser, UserFilter
from fastapi import Depends


class UserService:
    def __init__(self, user_repo: UserRepo = Depends()):
        self.userRepo = user_repo

    async def get_one_user(self, id: int):
        return await self.userRepo.get_by_id(id)

    async def get_all_users(self, filter_query: UserFilter):
        return await self.userRepo.get_all(filter_query)

    async def create_user(self, user_in: CreateUser):
        return await self.userRepo.create(user_in)

    async def delete_user(self, id: int):
        return await self.userRepo.delete(id)

    async def update_user(self, user_upd: UpdateUser):
        return await self.userRepo.update(user_upd)
