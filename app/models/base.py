from sqlalchemy.orm import  DeclarativeBase, declared_attr


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls):  # noqa: N805
        return cls.__name__.lower()
