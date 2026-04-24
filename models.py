from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase
from typing import List

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user_account"

    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    id: Mapped[int] = mapped_column(primary_key=True)

    tasks: Mapped[List["Task"]] = relationship(back_populates="owner")


class Task(Base):
    __tablename__ = "task"
    id: Mapped[int] = mapped_column(primary_key=True)
    
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
    content: Mapped[str] = mapped_column(nullable=False)
    priority: Mapped[int] = mapped_column(nullable=True)
    isCompleted: Mapped[bool] = mapped_column()

    owner: Mapped["User"] = relationship(back_populates="tasks")