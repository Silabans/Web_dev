import sqlalchemy as sa
from sqlalchemy import orm
from typing import List

class Base(orm.DeclarativeBase):
    pass

class User(Base):
    username: orm.Mapped[str] = orm.mapped_column(unique=True, nullable=False)
    password: orm.Mapped[str] = orm.mapped_column(nullable=False)
    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)

    tasks: orm.Mapped[List["Task"]] = orm.relationship(back_populate="owner")


class Task(Base):
