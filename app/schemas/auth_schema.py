from pydantic import BaseModel, Field


class RegisterUser(BaseModel):
    phone_number: str = Field(...)
    password: str = Field(...)
    confirm_password: str = Field(...)


class LoginUser(BaseModel):
    phone_number: str = Field(...)
    password: str = Field(...)
