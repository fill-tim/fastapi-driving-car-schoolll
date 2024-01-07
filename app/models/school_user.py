from sqlalchemy import Column, Integer, ForeignKey
from .base import Base


class SchoolUser(Base):
    __tablename__ = "school_users"

    id: int = Column(Integer, unique=True, primary_key=True)
    school_user: int = Column(Integer, ForeignKey("schools.id"))
    user_id: int = Column(Integer, ForeignKey("users.id"))
