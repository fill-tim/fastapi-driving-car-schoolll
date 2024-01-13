from sqlalchemy import Column, Integer, ForeignKey
from .base import Base


class Instructor(Base):
    id: int = Column(Integer, unique=True, primary_key=True)
    user_id: int = Column(Integer, ForeignKey("users.id"))
    school_id: int = Column(Integer, ForeignKey("schools.id"))
    car_id: int = Column(Integer, ForeignKey("cars.id"))
