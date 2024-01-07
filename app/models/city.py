from sqlalchemy import Column, Integer, String
from .base import Base


class City(Base):
    __tablename__ = "cities"

    id: int = Column(Integer, unique=True, primary_key=True)
    name: str = Column(String(255))
