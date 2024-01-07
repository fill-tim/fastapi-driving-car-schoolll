from sqlalchemy import Column, Integer, String, ForeignKey
from .base import Base


class TelegramUser(Base):
    __tablename__ = "telegram_users"

    id: int = Column(Integer, unique=True, primary_key=True)
    tg_name: str = Column(String(255))
    tg_uniq_name: str = Column(String(255), unique=True)
    chat_id: int = Column(Integer, unique=True)
    registration_date: int = Column(Integer)
    school_id: int = Column(Integer, ForeignKey("schools.id"))
