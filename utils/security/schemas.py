# -*- coding: utf-8 -*-
from pydantic import EmailStr, Field, field_validator

from utils.schemas.base import BaseSchema


class AccessTokenSchema(BaseSchema):
    """
    Access token schema.
    """

    access: str


class RefreshTokenSchema(BaseSchema):
    """
    Refresh token schema.
    """

    refresh: str


class AccessRefreshTokensSchema(AccessTokenSchema, RefreshTokenSchema):
    """
    Access and refresh token schema.
    """
