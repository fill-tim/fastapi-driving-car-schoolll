from contextlib import AbstractContextManager, contextmanager
from typing import Callable
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from .config import settings
from sqlalchemy.orm import Session


class DataBase:
    def __init__(self, url, echo) -> None:
        self.engine = create_async_engine(url=url, echo=echo)

        self.async_session = async_sessionmaker(
            bind=self.engine,
            autocommit=False,
            autoflush=False,
        )

    @contextmanager
    async def session(self) -> Callable[..., AbstractContextManager[Session]]:
        session: Session = self._session_factory()
        try:
            yield session
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()


data_base = DataBase(url=settings.url, echo=settings.echo)
