from sqlalchemy import Column, Integer, String
from .base import Base


class LessonType(Base):
    __tablename__ = "lesson_types"

    id: int = Column(Integer, unique=True, primary_key=True)
    name: str = Column(String(255))
