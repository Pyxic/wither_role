from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, Text, Integer, SmallInteger, Table, Column, Float

from apps.character.enums import SocialStatus, RegionType, ParentFateType, GenderType, AgeType, AttitudeType, \
    CharacterTraitType, ImportantEventType, WhomIsValued, WhatValue, AttributeType
from apps.user.models import User
from config.database import Base


character_event_association = Table(
    'character_event_association', Base.metadata,
    Column('character_id', Integer, ForeignKey('character.id')),
    Column('event_id', Integer, ForeignKey('importantevent.id'))
)


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
    family_fate_id: Mapped[int] = mapped_column(ForeignKey("familyfate.id"), nullable=True)
    family_fate: Mapped["FamilyFate"] = relationship("FamilyFate")
    parent_fate_id: Mapped[int] = mapped_column(ForeignKey("parentfate.id"), nullable=True)
    parent_fate: Mapped["ParentFate"] = relationship("ParentFate")
    family_situation_id: Mapped[int] = mapped_column(ForeignKey("familysituation.id"), nullable=True)
    family_situation: Mapped["FamilySituation"] = relationship("FamilySituation")
    friend_id: Mapped[int] = mapped_column(ForeignKey("friend.id"), nullable=True)
    friend: Mapped["Friend"] = relationship("Friend")

    character_attributes = relationship('CharacterAttribute', back_populates='character')
    character_skills = relationship("CharacterSkill", back_populates="character")
    character_equipments = relationship("CharacterEquipment", back_populates="character")  # Изменено
    important_events = relationship("ImportantEvent",
                                    secondary=character_event_association, back_populates="characters")  # Добавлено
    traits = relationship("CharacterTrait", back_populates="character")

    def __str__(self):
        return f"{self.id} - {self.name}"


class CharacterTrait(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    character_id: Mapped[int] = mapped_column(ForeignKey("character.id"))
    character: Mapped["Character"] = relationship(back_populates="traits")

    def __str__(self):
        return {f"{self.character_id - self.title}"}


class Race(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)
    description: Mapped[str] = mapped_column(Text)
    social_status: Mapped[SocialStatus]
    family_is_live: Mapped[bool] = mapped_column(nullable=True)
    parents_is_live: Mapped[bool] = mapped_column(nullable=True)

    def __str__(self):
        return self.name


class Region(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(70), unique=True)
    region_type: Mapped[RegionType]

    def __str__(self):
        return self.name


class FamilyFate(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(Text)
    region_type: Mapped[RegionType]

    def __str__(self):
        return self.description


class ParentFate(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(Text)
    region_type: Mapped[RegionType]

    def __str__(self):
        return self.description


class FamilySituation(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(Text)
    region_type: Mapped[RegionType]

    def __str__(self):
        return self.description


class Friend(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(Text)
    region_type: Mapped[RegionType]
    equipment_id: Mapped[int] = mapped_column(ForeignKey("equipment.id"), nullable=True)
    equipment: Mapped["Equipment"] = relationship("Equipment")

    def __str__(self):
        return self.description


class Relative(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    gender: Mapped[GenderType]
    age: Mapped[AgeType]
    attitude: Mapped[AttitudeType]
    core_character_trait: Mapped[CharacterTraitType]

    def __str__(self):
        return self.gender


class ImportantEvent(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    event_type: Mapped[ImportantEventType]
    description: Mapped[str] = mapped_column(Text)
    characters: Mapped[list["Character"]] = relationship(
        "Character",
        secondary=character_event_association,
        back_populates="important_events"
    )

    def __str__(self):
        return f"{self.event_type} {self.description}"


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
    equipments = relationship("Equipment", secondary=profession_equipment_association,
                              back_populates="professions")
    description: Mapped[str] = mapped_column(Text)

    def __str__(self):
        return self.name


class Attribute(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25), unique=True)
    short_name: Mapped[str] = mapped_column(String(5), unique=True)
    description = Column(String)
    code: Mapped[AttributeType] = mapped_column(unique=True)
    skills = relationship("Skill", back_populates="attribute")

    def __str__(self):
        return self.name


class CharacterAttribute(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    character_id: Mapped[int] = mapped_column(ForeignKey('character.id'))
    attribute_id: Mapped[int] = mapped_column(ForeignKey('attribute.id'))
    value: Mapped[int] = mapped_column(SmallInteger())
    character = relationship("Character", back_populates="character_attributes")
    attribute = relationship("Attribute")


class Skill(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[int] = mapped_column(String(40), unique=True)
    attribute_id: Mapped[int] = mapped_column(ForeignKey("attribute.id"))
    attribute = relationship("Attribute", back_populates="skills")
    description: Mapped[str] = mapped_column(Text, nullable=True)
    characters = relationship("CharacterSkill", back_populates="skill")

    def __str__(self):
        return self.name


class CharacterSkill(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    character_id: Mapped[int] = mapped_column(ForeignKey('character.id'))
    skill_id: Mapped[int] = mapped_column(ForeignKey('skill.id'))
    value: Mapped[int] = mapped_column(SmallInteger())
    character: Mapped["Character"] = relationship("Character", back_populates="character_skills")
    skill: Mapped["Skill"] = relationship("Skill", back_populates="characters")


class Equipment(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    price: Mapped[int] = mapped_column(SmallInteger)
    weight: Mapped[float] = mapped_column(Float)
    description: Mapped[str] = mapped_column(Text)
    character_equipments = relationship("CharacterEquipment", back_populates="equipment")
    professions = relationship("Profession", secondary=profession_equipment_association,
                               back_populates="equipments")

    def __str__(self):
        return self.name


class CharacterEquipment(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    character_id: Mapped[int] = mapped_column(ForeignKey('character.id'))
    equipment_id: Mapped[int] = mapped_column(ForeignKey('equipment.id'))
    quantity: Mapped[int] = mapped_column(SmallInteger())
    character: Mapped["Character"] = relationship("Character", back_populates="character_equipments")
    equipment: Mapped["Equipment"] = relationship("Equipment")
