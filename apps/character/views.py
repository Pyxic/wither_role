from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, status, Depends

from apps.character.schemas import AttributeSchema
from apps.character.services import AttributeService
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
