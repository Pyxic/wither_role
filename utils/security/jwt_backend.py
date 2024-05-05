# -*- coding: utf-8 -*-
import logging
from datetime import datetime, timedelta
from typing import Optional

import jwt

from config.settings import settings
from utils.security.schemas import AccessRefreshTokensSchema

logger = logging.getLogger(__name__)


class JWTBackend:
    """
    Set up the JWT Backend with the given cache backend and private key.
    """

    def __init__(
        self,
        access_expiration: int,
        refresh_expiration: int,
        jwt_secret: str,
        jwt_algorithm: str,
    ) -> None:
        self._access_expiration = access_expiration
        self._refresh_expiration = refresh_expiration
        self._jwt_secret = jwt_secret
        self._jwt_algorithm = jwt_algorithm

    @staticmethod
    async def decode_token(token: str, leeway: int = 0) -> Optional[dict]:
        if token:
            try:
                payload = jwt.decode(
                    token,
                    settings.jwt_secret,
                    leeway=leeway,
                    algorithms=settings.jwt_algorithm,
                )
                return payload
            except Exception as err:
                logger.warning(err)
                return None
        return None

    def _create_token(
        self,
        payload: dict,
        token_type: str,
        expiration_delta: Optional[int] = None,
    ) -> str:
        iat = datetime.utcnow()
        if expiration_delta:
            exp = datetime.utcnow() + timedelta(seconds=expiration_delta)
        else:
            exp = datetime.utcnow() + timedelta(seconds=60)

        payload |= {"type": token_type, "exp": exp, "iat": iat}

        token = jwt.encode(payload, self._jwt_secret, algorithm=self._jwt_algorithm)
        if isinstance(token, bytes):
            # For PyJWT <= 1.7.1
            return token.decode("utf-8")
        # For PyJWT >= 2.0.0a1
        return token

    def create_access_token(self, payload: dict) -> str:
        return self._create_token(payload, "access", self._access_expiration)

    def create_refresh_token(self, payload: dict) -> str:
        return self._create_token(payload, "refresh", self._refresh_expiration)

    def create_tokens(self, payload: dict) -> AccessRefreshTokensSchema:
        access = self.create_access_token(payload)
        refresh = self.create_refresh_token(payload)

        return AccessRefreshTokensSchema(access=access, refresh=refresh)
