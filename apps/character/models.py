from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, Text, Integer, BigInteger, SmallInteger

from apps.character.enums import SocialStatus, RegionType, ParentFateType, GenderType, AgeType, AttitudeType, \
    CharacterTraitType, ImportantEventType
from apps.user.models import User
from config.database import Base
from sqlalchemy.dialects.postgresql import BIGINT


class Character(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(80), nullable=True)
    age: Mapped[int] = mapped_column(SmallInteger())
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="characters")
    parent_fate_type: Mapped[ParentFateType] = mapped_column(nullable=True)
    clothes: Mapped[str] = mapped_column(String(80), nullable=True)


class CharacterTrait(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    character_id: Mapped[int] = mapped_column(ForeignKey("character.id"))
    user: Mapped["Character"] = relationship(back_populates="traits")


class Race(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)
    description: Mapped[str] = mapped_column(Text)
    social_status: Mapped[SocialStatus]
    family_is_live: Mapped[bool] = mapped_column(nullable=True)
    parents_is_live: Mapped[bool] = mapped_column(nullable=True)


class Region(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(70), unique=True)
    region_type: Mapped[RegionType]


class FamilyFate(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(Text)
    region_type: Mapped[RegionType]


class ParentFate(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(Text)
    region_type: Mapped[RegionType]


class FamilySituation(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(Text)
    region_type: Mapped[RegionType]


class Friend(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(Text)
    region_type: Mapped[RegionType]
    equipment_id: Mapped[int] = mapped_column(ForeignKey("equipment.id"))
    equipment: Mapped["Equipment"] = relationship("Equipment")


class Relative(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    gender: Mapped[GenderType]
    age: Mapped[AgeType]
    attitude: Mapped[AttitudeType]
    core_character_trait: Mapped[CharacterTraitType]


class ImportantEvent(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    event_type: Mapped[ImportantEventType]
    description: Mapped[str] = mapped_column(Text)
    character = relationship("Character", back_populates="important_events")


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
