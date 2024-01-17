from fastapi import APIRouter
from fastapi.security import HTTPBearer
from ..services.user_service import UserService
from ..schemas.user_schema import CreateUser, UserResponse, UpdateUser, UserFilter
from fastapi import Depends
from fastapi_filter import FilterDepends

user_router = APIRouter(prefix="/user", tags=["users"])

security = HTTPBearer()


@user_router.get("/list", response_model=list[UserResponse])
async def list(
    filter: UserFilter = FilterDepends(UserFilter),
    user_service: UserService = Depends(),
    authorization: str = Depends(security),
):
    return await user_service.get_all_users(filter)


@user_router.get("/get_by_id/{id}", response_model=UserResponse)
async def get(id: int, user_service: UserService = Depends()):
    return await user_service.get_one_user(id)


@user_router.post("/create")
async def create(user_in: CreateUser, user_service: UserService = Depends()):
    return await user_service.create_user(user_in)


@user_router.delete("/delete/{id}")
async def delete(id: int, user_service: UserService = Depends()):
    return await user_service.delete_user(id)


@user_router.patch("/update")
async def update(user_upd: UpdateUser, user_service: UserService = Depends()):
    return await user_service.update_user(user_upd)
