from apps.character.repository import AttributeRepository
from apps.character.schemas import AttributeSchema
from base.repository.repository import BaseRepository


class BaseService:
    def __init__(self, repository: BaseRepository):
        self.repository = repository

    async def list(self):
        return await self.repository.get()


class SkillService(BaseService):
    pass


class AttributeService(BaseService):
    repository: AttributeRepository

    async def list(self) -> list[AttributeSchema]:
        attributes = await self.repository.get_attributes_with_skills()
        return [AttributeSchema.model_validate(attribute) for attribute in attributes]


class RaceService(BaseService):
    pass


class RegionService(BaseService):
    pass


class ProfessionService(BaseService):
    pass
