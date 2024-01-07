from sqlalchemy import Column, Integer, String, ForeignKey
from .base import Base


class School(Base):
    id: int = Column(Integer, unique=True, primary_key=True)
    name: str = Column(String(255))
    guid: str = Column(String(255), unique=True)
    city_id: int = Column(Integer, ForeignKey('cities.id'))
