from apps.character.repository import AttributeRepository
from apps.character.schemas import AttributeSchema
from base.repository.repository import BaseRepository


class SkillService:
    def __init__(self, skill_repository: BaseRepository):
        self.skill_repository = skill_repository

    async def list(self):
        return self.skill_repository.get()


class AttributeService:
    def __init__(self, attribute_repository: AttributeRepository):
        self.attribute_repository = attribute_repository

    async def list(self) -> list[AttributeSchema]:
        attributes = await self.attribute_repository.get_attributes_with_skills()
        return [AttributeSchema.model_validate(attribute) for attribute in attributes]
