from typing import List, TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from config.database import Base
if TYPE_CHECKING:
    from apps.character.models import Character


class User(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    avatar: Mapped[str] = mapped_column(nullable=True)

    characters: Mapped[List["Character"]] = relationship(back_populates="user")

    def __str__(self):
        return self.username
