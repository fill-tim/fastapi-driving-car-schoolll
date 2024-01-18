from sqlalchemy import Column, Integer, String, ForeignKey
from .base import Base


class User(Base):
    id: int = Column(Integer, unique=True, primary_key=True)
    first_name: str = Column(String(255), nullable=True)
    last_name: str = Column(String(255), nullable=True)
    phone_number: str = Column(String(255), nullable=True)
    password: str = Column(String(255), nullable=True)
    age: int = Column(Integer, nullable=True)
    photo: str = Column(String(255), nullable=True)
    telegram_user_id: int = Column(
        Integer, ForeignKey("telegram_users.id"), nullable=True
    )
    role_id: int = Column(Integer, ForeignKey("roles.id"), nullable=True)
    school_id: int = Column(Integer, ForeignKey("schools.id"), nullable=True)
