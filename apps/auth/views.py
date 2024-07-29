from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from fastapi import Request
from starlette import status

from apps.auth.dependencies import AuthenticatedUser
from apps.auth.schemas import UserCreateSchema, UserPayload, LoginSchema
from apps.auth.services import AuthService
from apps.user.models import User
from config.registry import Registry
from utils.exceptions.examples_generator import generate_examples
from utils.exceptions.http.api import NotFoundException, RateLimitException
from utils.exceptions.http.auth import InvalidCredentialsException
from utils.security.schemas import AccessRefreshTokensSchema, RefreshTokenSchema

auth_router = APIRouter()


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


@auth_router.post(
    "/login/",
    name="auth:login",
    summary="Login to the admin system. Only for staff users.",
    description="Login to the CRM system. Only for staff users. Rate limited.",
    status_code=status.HTTP_200_OK,
    response_model=AccessRefreshTokensSchema,
    responses=generate_examples(
        InvalidCredentialsException,
        NotFoundException,
        RateLimitException,
    ),
)
@inject
async def login_to_site(
    user_login_schema: LoginSchema,
    auth_service: AuthService = Depends(Provide[Registry.authentication.auth_service]),
    # dependencies=Depends(  # noqa
    #     RateLimiter(
    #         times=15,
    #         seconds=60,
    #     ),
    # ),
):
    """
    Login with email and password to CRM system.

    Only for common users. Returns user payload and access/refresh
    tokens. Rate limited.

    """
    tokens: AccessRefreshTokensSchema = await auth_service.login(user_login_schema=user_login_schema)

    return tokens


@auth_router.post(
    "/refresh/",
    name="auth:refresh",
    summary="Refresh tokens for user",
    status_code=status.HTTP_200_OK,
    response_model=AccessRefreshTokensSchema,
    responses=generate_examples(),
)
@inject
async def staff_refresh_access_token(
    refresh_token: RefreshTokenSchema,
    auth_service: AuthService = Depends(Provide[Registry.authentication.auth_service]),
) -> AccessRefreshTokensSchema:
    """
    Refresh tokens from refresh_token.
    """
    tokens: AccessRefreshTokensSchema = await auth_service.refresh_tokens(refresh_token.refresh)
    return tokens


@auth_router.get(
    "/profile/",
    name="auth:profile",
    summary="Get base profile data.",
    description="Get base profile data of user. Rate limited.",
    status_code=status.HTTP_200_OK,
    response_model=UserPayload,
    responses=generate_examples(
        InvalidCredentialsException,
        NotFoundException,
        RateLimitException,
    ),
)
@inject
async def get_profile_data(
    user: User = Depends(AuthenticatedUser())
):
    """
    Login with email and password to CRM system.

    Only for common users. Returns user payload and access/refresh
    tokens. Rate limited.

    """
    return UserPayload.model_validate(user)
