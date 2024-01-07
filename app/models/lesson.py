from sqlalchemy import Column, Integer, ForeignKey
from .base import Base


class Lesson(Base):
    id: int = Column(Integer, unique=True, primary_key=True)
    date: int = Column(Integer)
    user_id: int = Column(Integer, ForeignKey("users.id"))
    school_id: int = Column(Integer, ForeignKey("schools.id"))
    instructor_id: int = Column(Integer, ForeignKey("instructors.id"))
    lesson_type_id: int = Column(Integer, ForeignKey("lesson_types.id"))
