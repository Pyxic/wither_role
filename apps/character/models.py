from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, Text, Integer, BigInteger, SmallInteger, Table, Column, Float

from apps.character.enums import SocialStatus, RegionType, ParentFateType, GenderType, AgeType, AttitudeType, \
    CharacterTraitType, ImportantEventType, WhomIsValued, WhatValue, AttributeType
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
    hairstyle: Mapped[str] = mapped_column(String(50), nullable=True)
    jewelry: Mapped[str] = mapped_column(String(50), nullable=True)
    who_is_valued: Mapped[WhomIsValued] = mapped_column(nullable=True)
    what_value: Mapped[WhatValue] = mapped_column(nullable=True)
    thinks_about_people: Mapped[str] = mapped_column(String(255), nullable=True)
    profession_id: Mapped[int] = mapped_column(ForeignKey("profession.id"), nullable=True)
    profession: Mapped["Profession"] = relationship("Profession")
    race_id: Mapped[int] = mapped_column(ForeignKey("race.id"), nullable=True)
    race: Mapped["Race"] = relationship("Race")
    region_id: Mapped[int] = mapped_column(ForeignKey("region.id"), nullable=True)
    region: Mapped["Region"] = relationship("Region")

    character_attributes = relationship('CharacterAttribute', back_populates='character')
    character_skills = relationship('CharacterSkill', back_populates="character")
    character_equipments = relationship("Equipment", back_populates="character")
    traits = relationship("CharacterTrait", back_populates="character")


class CharacterTrait(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    character_id: Mapped[int] = mapped_column(ForeignKey("character.id"))
    character: Mapped["Character"] = relationship(back_populates="traits")


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


profession_equipment_association = Table(
    'profession_equipment',
    Base.metadata,
    Column('profession_id', Integer, ForeignKey('profession.id')),
    Column('equipment_id', Integer, ForeignKey('equipment.id'))
)


class Profession(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(80), unique=True)
    defining_skill: Mapped[str] = mapped_column(String(100))
    defining_skill_description: Mapped[str] = mapped_column(Text)
    energy: Mapped[int] = mapped_column(SmallInteger, default=0)
    equipments = relationship('Equipment', secondary=profession_equipment_association,
                              back_populates='professions')
    description: Mapped[str] = mapped_column(Text)


class Attribute(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(15), unique=True)
    short_name: Mapped[str] = mapped_column(String(5), unique=True)
    description = Column(String)
    code: Mapped[AttributeType] = mapped_column(unique=True)
    skills = relationship("Skill", back_populates="attribute")


class CharacterAttribute(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    character_id: Mapped[int] = mapped_column(ForeignKey('character.id'))
    attribute_id: Mapped[int] = mapped_column(ForeignKey('attribute.id'))
    value: Mapped[int] = mapped_column(SmallInteger())
    character = relationship("Character", back_populates="character_attributes")
    attribute = relationship("Attribute")


class Skill(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[int] = mapped_column(String(25), unique=True)
    attribute_id: Mapped[int] = mapped_column(ForeignKey("attribute.id"))
    attribute = relationship("Attribute", back_populates="skills")
    description: Mapped[str] = mapped_column(Text, nullable=True)


class CharacterSkill(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    character_id: Mapped[int] = mapped_column(ForeignKey('character.id'))
    skill_id: Mapped[int] = mapped_column(ForeignKey('skill.id'))
    value: Mapped[int] = mapped_column(SmallInteger())
    character = relationship("Character", back_populates="character_skills")
    attribute = relationship("Skill", back_populates="characters")


class Equipment(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    price: Mapped[int] = mapped_column(SmallInteger)
    weight: Mapped[float] = mapped_column(Float)
    description: Mapped[str] = mapped_column(Text)


class CharacterEquipment(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    character_id: Mapped[int] = mapped_column(ForeignKey('character.id'))
    equipment_id: Mapped[int] = mapped_column(ForeignKey('equipment.id'))
    quantity: Mapped[int] = mapped_column(SmallInteger())
    character = relationship("Character", back_populates="character_equipments")
    equipment = relationship("Equipment")
