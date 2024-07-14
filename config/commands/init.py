from dependency_injector.wiring import Provide

from apps.character.enums import AttributeType
from apps.character.repository import AttributeRepository
from config.registry import Registry


class ProjectInitialization:

    @classmethod
    async def start(cls, app):
        await cls.create_attributes()

    @classmethod
    async def create_attributes(cls, attribute_repository: AttributeRepository = Provide[Registry.character_container.attribute_repository]):
        if not await attribute_repository.exists():
            attributes = [
                {
                    "name": "Интеллект",
                    "short_name": "Инт",
                    "description": "Решение загадок, проведение научных исследований, дедукция и прочие занятия, "
                                   "требующие умственных усилий.",
                    "code": AttributeType.INTELLIGENCE
                },
                {
                    "name": "Реакция",
                    "short_name": "Реа",
                    "description": "Необходимо в бою для уклонения от ударов и для занятий требующих быстрой "
                                   "реакции и точных движений",
                    "code": AttributeType.REACTION
                },
                {
                    "name": "Ловкость",
                    "short_name": "Лвк",
                    "description": "Lorem",
                    "code": AttributeType.DEXTERITY
                },
                {
                    "name": "Телосложение",
                    "short_name": "Тел",
                    "description": "Lorem",
                    "code": AttributeType.PHYSIQUE
                },
                {
                    "name": "Скорость",
                    "short_name": "Скор",
                    "description": "Lorem",
                    "code": AttributeType.SPEED,
                },
                {
                    "name": "Эмпатия",
                    "short_name": "Эмп",
                    "description": "Lorem",
                    "code": AttributeType.EMPATHY
                },
                {
                    "name": "Ремесло",
                    "short_name": "Рем",
                    "description": "Lorem",
                    "code": AttributeType.CRAFT
                },
                {
                    "name": "Воля",
                    "short_name": "Воля",
                    "description": "Lorem",
                    "code": AttributeType.VOLITION
                },
                {
                    "name": "Удача",
                    "short_name": "Удч",
                    "description": "Lorem",
                    "code": AttributeType.LUCK,
                },
                {
                    "name": "Энеогия",
                    "short_name": "Энг",
                    "description": "Lorem",
                    "code": AttributeType.ENERGY
                },
                {
                    "name": "Устойчивость",
                    "short_name": "Ус",
                    "description": "Lorem",
                    "code": AttributeType.SUSTAINABILITY
                },
                {
                    "name": "Бег",
                    "short_name": "Бег",
                    "description": "Lorem",
                    "code": AttributeType.RUNNING
                },
                {
                    "name": "Прыжок",
                    "short_name": "Прж",
                    "description": "Lorem",
                    "code": AttributeType.JUMPING
                },
                {
                    "name": "Пункты здоровья",
                    "short_name": "ПЗ",
                    "description": "Lorem",
                    "code": AttributeType.HEALTH_POINTS
                },
                {
                    "name": "Выносливость",
                    "short_name": "Вын",
                    "description": "Lorem",
                    "code": AttributeType.STAMINA
                },
                {
                    "name": "Переносимый вес",
                    "short_name": "Вес",
                    "description": "Lorem",
                    "code": AttributeType.TRANSFERABLE_WEIGHT
                },
                {
                    "name": "Отдых",
                    "short_name": "Отд",
                    "description": "Lorem",
                    "code": AttributeType.REST
                },
                {
                    "name": "Удар рукой",
                    "short_name": "уд рк",
                    "description": "Lorem",
                    "code": AttributeType.PUNCH
                },
                {
                    "name": "Удар ногой",
                    "short_name": "Уд нu",
                    "description": "Lorem",
                    "code": AttributeType.KICK
                },
            ]
            await attribute_repository.bulk_create(attributes)
