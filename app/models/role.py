from sqlalchemy import Column, Integer, String
from .base import Base


class Role(Base):
    id: int = Column(Integer, unique=True, primary_key=True)
    name: str = Column(String(255))
