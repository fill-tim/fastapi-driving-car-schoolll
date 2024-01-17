from fastapi import Depends
from ..repository.auth_repo import AuthRepo
from ..models.user import User
from passlib.hash import bcrypt

class AuthService:
    def __init__(self, auth_repo: AuthRepo = Depends()):
        self._auth_repo = auth_repo

    async def auth_login(self, login_user):
        pass

    async def auth_register(self, register_user):
        form = register_user.model_dump()
        
        if form["password"] != form["confirm_password"]:
            return "Пароли не совпадают"
        
        user = await AuthRepo.find_user_by_phone_number(form["phone_number"])
        if user:
            return "Пользователь с таким номером телефона уже зарегистрирован"
        
        hash_password = bcrypt.hash(form["password"])
        
        user_data = {
            "phone_number": form["phone_number"],
            "password":  hash_password
        }
        
        user = await AuthRepo.create(user_data)
        return user
