from sqlalchemy import Column, Integer, String, ForeignKey
from .base import Base


class User(Base):
    id: int = Column(Integer, unique=True, primary_key=True)
    first_name: str = Column(String(255))
    last_name: str = Column(String(255))
    phone_number: str = Column(String(255))
    password: str = Column(String(255))
    age: int = Column(Integer)
    photo: str = Column(String(255))
    telegram_user_id: int = Column(Integer, ForeignKey("telegram_users.id"))
    role_id: int = Column(Integer, ForeignKey("roles.id"))
    school_id: int = Column(Integer, ForeignKey("schools.id"))
