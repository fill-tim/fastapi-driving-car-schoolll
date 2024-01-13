from fastapi import APIRouter
from ..services.user_service import UserService
from ..schemas.user_schema import CreateUser, UserResponse, UpdateUser, UserFilter
from fastapi import Depends
from fastapi_filter import FilterDepends

user_router = APIRouter(prefix="/user", tags=["users"])


@user_router.get("/list", response_model=list[UserResponse])
async def list(filter: UserFilter = FilterDepends(UserFilter), userService: UserService = Depends()):
    return await userService.get_all_users(filter)


@user_router.get("/get_by_id/{id}", response_model=UserResponse)
async def get(id: int, userService: UserService = Depends()):
    return await userService.get_one_user(id)


@user_router.post("/create")
async def create(user_in: CreateUser, userService: UserService = Depends()):
    return await userService.create_user(user_in)


@user_router.delete("/delete/{id}")
async def delete(id: int, userService: UserService = Depends()):
    return await userService.delete_user(id)


@user_router.patch("/update")
async def update(user_upd: UpdateUser, userService: UserService = Depends()):
    return await userService.update_user(user_upd)
