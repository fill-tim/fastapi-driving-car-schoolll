from pydantic import BaseModel


class RegisterUser(BaseModel):
    phone_number: str
    password: str
    confirm_password: str


class LoginUser(BaseModel):
    phone_number: str
    password: str
