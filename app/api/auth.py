from fastapi import APIRouter, Depends
from ..schemas.auth_schema import RegisterUser, LoginUser
from ..schemas.user_schema import UserResponse
from ..services.auth_service import AuthService

auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.post("/register", response_model=UserResponse)
async def register(register_form: RegisterUser, auth_service: AuthService = Depends()):
    return await auth_service.auth_register(register_form)


@auth_router.post("/login")
async def register(login_form: LoginUser):
    pass
