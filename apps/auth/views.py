from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from fastapi import Request
from starlette import status
from starlette.responses import Response

from apps.auth.schemas import UserCreateSchema, UserPayload
from apps.auth.services import AuthService
from config.registry import Registry
from utils.exceptions.examples_generator import generate_examples
from utils.exceptions.http.api import NotFoundException, RateLimitException
from utils.exceptions.http.auth import InvalidCredentialsException
from utils.security.schemas import AccessRefreshTokensSchema

auth_router = APIRouter()


# @auth_router.get("/login/", response_class=HTMLResponse, name="auth:login")
# def get_login_page(request: Request):
#     return templates.TemplateResponse("auth/login.html", {"request": request})


@auth_router.post(
    "/register/",
    name="auth:login",
    summary="Login to the user system. Only for users.",
    description="Login to the user site. Only for users. Rate limited.",
    status_code=status.HTTP_200_OK,
    response_model=UserPayload,
    responses=generate_examples(
        InvalidCredentialsException,
        NotFoundException,
        RateLimitException,
    ),
)
@inject
async def register_user(
        request: Request,
        user_create_schema: UserCreateSchema,
        auth_service: AuthService = Depends(Provide[Registry.authentication.auth_service])
):
    return await auth_service.register(user_create_schema)
