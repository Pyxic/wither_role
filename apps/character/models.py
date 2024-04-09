from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, Text, Integer, BigInteger, SmallInteger

from apps.character.enums import SocialStatus
from config.database import Base
from sqlalchemy.dialects.postgresql import BIGINT


class Character(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(80), nullable=True)
    age: Mapped[int] = mapped_column(SmallInteger())
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user = relationship(back_populates="characters")


class Race(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)
    description: Mapped[str] = mapped_column(Text)
    social_status: Mapped[SocialStatus]


class Region(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(70), unique=True)


class Profession(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(80), unique=True)


class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    name = Column(String)
    race = Column(String)
    class_ = Column(String)
    origin = Column(String)
    description = Column(String)
    avatar = Column(String)
    user = relationship("User", back_populates="characters")
    attributes = relationship("Attribute", secondary=character_attribute_table)
    skills = relationship("Skill", secondary=character_skill_table)
    items = relationship("Item", secondary=character_item_table)
