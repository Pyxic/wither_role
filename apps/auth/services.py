from typing import Optional

from email_validator import validate_email
from fastapi.encoders import jsonable_encoder

from apps.auth.exceptions import InvalidEmailException
from apps.auth.schemas import LoginSchema, UserPayload, UserCreateSchema
from apps.user.models import User
from apps.user.repository import UserRepository
from utils.exceptions.http.api import NotFoundException, AlreadyExistsException
from utils.exceptions.http.auth import InvalidCredentialsException
from utils.security.jwt_backend import JWTBackend
from utils.security.password_helper import password_helper
from utils.security.schemas import AccessRefreshTokensSchema


class AuthService:
    def __init__(self, user_repository: UserRepository, jwt_backend: JWTBackend):
        self.user_repository = user_repository
        self.jwt_backend = jwt_backend

    async def login(self, user_login_schema: LoginSchema) -> AccessRefreshTokensSchema:
        """
        Login staff user to crm system.
        """
        # get user
        user: User = await self._get_user_by_email(
            email=user_login_schema.email,
        )

        return await self._login(user, user_login_schema)

    async def register(self, user_create_schema: UserCreateSchema) -> User:
        try:
            validate_email(user_create_schema.email, timeout=5)
        except Exception as e:
            raise InvalidEmailException(e)
        if await self.user_repository.exists(email=user_create_schema.email):
            raise AlreadyExistsException("User with this email already exists.")
        user_dict = user_create_schema.model_dump()
        password = user_dict.pop("password")
        user_dict["password"] = password_helper.hash(password)
        return await self.user_repository.create(user_dict)

    async def _get_user_by_email(self, email: str, raise_not_found: bool = True) -> User:
        """
        Get user by email.
        """
        # get user
        user: User = await self.user_repository.get_single(
            email=email.lower(),
            raise_not_found=raise_not_found,
        )
        # check if user exists
        if not user and raise_not_found:
            raise NotFoundException("User not found")
        return user

    async def _login(self, user: User, login_schema: LoginSchema) -> AccessRefreshTokensSchema:
        """
        Check staff credentials and return user data and tokens.
        """
        # check passwords
        if not password_helper.verify_and_update(
            plain_password=login_schema.password,
            hashed_password=user.password,
        )[0]:
            raise InvalidCredentialsException("Invalid password.")

        # create tokens
        tokens = await self._get_tokens(user)

        return tokens

    async def _get_tokens(self, user: User) -> AccessRefreshTokensSchema:
        """
        Get user tokens.
        """
        payload = UserPayload.model_validate(user)
        user_data = jsonable_encoder(payload)
        tokens = self.jwt_backend.create_tokens(user_data)
        return tokens

    async def _get_refresh_token_payload(self, refresh: str) -> dict:
        refresh_token_payload = await self.jwt_backend.decode_token(refresh)

        # Check if refresh token is valid.
        if refresh_token_payload is None or refresh_token_payload.get("type") != "refresh":
            raise InvalidCredentialsException()
        return refresh_token_payload

    async def refresh_tokens(self, refresh: str):
        refresh_token_payload = await self._get_refresh_token_payload(refresh)
        user: Optional[User] = await self.user_repository.get_single(
            id=refresh_token_payload.get("id"),
        )
        return await self._get_tokens(user)
