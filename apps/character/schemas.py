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

