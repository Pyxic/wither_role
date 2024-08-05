from utils.schemas.base import BaseSchema


class SkillSchema(BaseSchema):
    id: int
    name: str
    description: str
    attribute_id: int


class AttributeSchema(BaseSchema):
    id: int
    name: str
    short_name: str
    description: str
    code: str
    skills: list[SkillSchema] | None


class RegionSchema(BaseSchema):
    id: int
    name: str


class RaceSchema(BaseSchema):
    id: int
    name: str
    description: str | None


class ProfessionSchema(BaseSchema):
    id: int
    name: str
    defining_skill: str
    defining_skill_description: str
    energy: int
    description: str


class ConfigSchema(BaseSchema):
    regions: list[RegionSchema]
    races: list[RaceSchema]
    professions: list[ProfessionSchema]
    attributes: list[AttributeSchema]

