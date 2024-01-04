from ..repository.user_repo import UserRepo
from ..schemas.user import CreateUser
from fastapi import Depends


class UserService:
    userRepo: UserRepo

    def __init__(self, user_repo: UserRepo = Depends()):
        # self.repo: UserRepo = UserRepo
        self.userRepo = user_repo

    async def get_one_user(self, id: int):
        return await self.userRepo.get_one_user_by_id()

    async def get_all_users(self):
        return await self.userRepo.get_all_user()

    async def create_user(self, user_in: CreateUser):
        return await self.userRepo.create_user(user_in)
