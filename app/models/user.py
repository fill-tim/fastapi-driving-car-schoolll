from sqlalchemy import Column, Integer, String
from .base import Base


class User(Base):
    __tablename__ = "users"

    id: int = Column(Integer, unique=True, primary_key=True)
    first_name: str = Column(String(255))
    last_name: str = Column(String(255))
    age: int = Column(Integer)
