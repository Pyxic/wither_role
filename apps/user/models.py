from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from config.database import Base


class User(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    avatar: Mapped[str]

    characters = relationship(back_populates="user")
