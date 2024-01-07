from sqlalchemy import Column, Integer, ForeignKey
from .base import Base


class SchoolCar(Base):
    __tablename__ = "school_cars"

    id: int = Column(Integer, unique=True, primary_key=True)
    car_id: int = Column(Integer, ForeignKey("cars.id"))
    school_id: int = Column(Integer, ForeignKey("schools.id"))
