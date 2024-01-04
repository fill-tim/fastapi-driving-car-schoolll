from fastapi import APIRouter
from ..services.user_service import UserService
from ..schemas.user import CreateUser
from fastapi import Depends

user_router = APIRouter(tags=["users"])


@user_router.get("/users/")
async def get(userService: UserService = Depends()):
    return await userService.get_all_users()


@user_router.post("/create_user")
async def create(user_in: CreateUser, userService: UserService = Depends()):
    return await userService.create_user(user_in)
