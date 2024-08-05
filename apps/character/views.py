from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, status, Depends

from apps.character.schemas import AttributeSchema, ConfigSchema
from apps.character.services import AttributeService, RegionService, RaceService, ProfessionService
from config.registry import Registry
from utils.exceptions.examples_generator import generate_examples

character_router = APIRouter()


@character_router.get(
    "/skills/",
    name="character:skill_list",
    summary="Get character skill list.",
    description="Get character skill list.",
    status_code=status.HTTP_200_OK,
    response_model=list[AttributeSchema],
    responses=generate_examples(
    ),
)
@inject
async def get_skill_list(
        attribute_service: AttributeService = Depends(Provide[Registry.character_container.attribute_service])
):
    return await attribute_service.list()


@character_router.get(
    "/configs/",
    name="character:configs",
    summary="Get common configs data",
    description="Get common configs data",
    status_code=status.HTTP_200_OK,
    response_model=ConfigSchema,
    responses=generate_examples(
    ),
)
@inject
async def get_common_configs(
        region_service: RegionService = Depends(Provide[Registry.character_container.region_service]),
        race_service: RaceService = Depends(Provide[Registry.character_container.race_service]),
        profession_service: ProfessionService = Depends(Provide[Registry.character_container.profession_service]),
        attribute_service: AttributeService = Depends(Provide[Registry.character_container.attribute_service])
):
    region_services = await region_service.list()

    return ConfigSchema(
        regions=region_services,
        races=await race_service.list(),
        professions=await profession_service.list(),
        attributes=await attribute_service.list(),
    )
