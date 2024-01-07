from sqlalchemy import Column, Integer, String
from .base import Base


class Car(Base):
    id: int = Column(Integer, unique=True, primary_key=True)
    model: str = Column(String(255))
    number: str = Column(String(255))
