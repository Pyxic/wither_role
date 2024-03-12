from sqlalchemy.orm import Mapped, mapped_column

from config.database import Base


class Character(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    age: Mapped[int]
