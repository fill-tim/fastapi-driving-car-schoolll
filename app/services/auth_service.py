from fastapi import Depends
from ..repository.auth_repo import AuthRepo
from ..schemas.user_schema import CreateUser

# from passlib.hash import bcrypt
import bcrypt


class AuthService:
    def __init__(self, auth_repo: AuthRepo = Depends()):
        self._auth_repo = auth_repo

    async def auth_login(self, login_user):
        form = login_user.model_dump()
        password = form["password"]
        user = await self._auth_repo.find_user_by_phone_number(form["phone_number"])

        if not user:
            return "Пользователя с таким phone_number"

        result = bcrypt.checkpw(password.encode("utf8"), (user.password).encode("utf8"))

        if not result:
            return "Логин или пароль введен неправильно"

        return user

    async def auth_register(self, register_user):
        form = register_user.model_dump()

        if form["password"] != form["confirm_password"]:
            return "Пароли не совпадают"

        user = await self._auth_repo.find_user_by_phone_number(form["phone_number"])
        if user:
            return "Пользователь с таким номером телефона уже зарегистрирован"

        hash_password = bcrypt.hashpw(form["password"], bcrypt.gensalt())

        create_user = CreateUser(
            phone_number=form["phone_number"], password=hash_password
        )


        user = await self._auth_repo.create(create_user)
        return user
