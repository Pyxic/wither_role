from typing import Optional

from aiocache import cached
from dependency_injector.wiring import Provide, inject
from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.security.utils import get_authorization_scheme_param
from fastapi_babel.core import lazy_gettext as _

from apps.auth.schemas import UserPayload
from apps.user.models import User
from apps.user.repository import UserRepository
from config.registry import Registry
from config.settings import settings
from utils.exceptions.http.auth import UnauthorizedException, InvalidCredentialsException
from utils.security.jwt_backend import JWTBackend
from fastapi import Request


@cached()
async def get_jwt_backend() -> JWTBackend:
    """
    Get the JWT Backend for the given request.
    """
    return JWTBackend(
        access_expiration=settings.jwt_access_expiration,
        refresh_expiration=settings.jwt_refresh_expiration,
        jwt_secret=settings.jwt_secret,
        jwt_algorithm=settings.jwt_algorithm,
    )


class JwtHTTPBearer(HTTPBearer):
    async def __call__(
        self,
        request: Request,
    ) -> Optional[HTTPAuthorizationCredentials]:
        authorization: str = request.headers.get("Authorization")
        scheme, credentials = get_authorization_scheme_param(authorization)
        if not (authorization and scheme and credentials):
            if self.auto_error:
                raise UnauthorizedException()
            else:
                return None
        if scheme.lower() != "bearer":
            if self.auto_error:
                raise UnauthorizedException(_("Invalid authentication format."))
            else:
                return None
        return HTTPAuthorizationCredentials(scheme=scheme, credentials=credentials)


jwt_http_bearer = JwtHTTPBearer()


@inject
async def get_authenticated_user_payload(
    jwt_backend: JWTBackend = Depends(get_jwt_backend),
    bearer: str = Depends(jwt_http_bearer),
) -> UserPayload:
    if token := bearer.credentials:  # noqa
        if data := await jwt_backend.decode_token(token):
            user_payload = UserPayload(**data)
            if user_payload and user_payload.id:
                return user_payload
        raise InvalidCredentialsException()
    raise UnauthorizedException()


@inject
async def get_authenticated_user(
    user_payload: UserPayload = Depends(get_authenticated_user_payload),
    user_repository: UserRepository = Provide[Registry.user_container.repository]
) -> User:
    user = await user_payload.get_instance(user_repository)

    return user


class AuthenticatedUser:
    def __init__(
        self,
    ):
        pass

    @inject
    async def __call__(
            self,
            user_payload: UserPayload = Depends(get_authenticated_user_payload),
            user_repository: UserRepository = Depends(Provide[Registry.user_container.repository])
    ):
        user = await user_payload.get_instance(user_repository)
        return user
