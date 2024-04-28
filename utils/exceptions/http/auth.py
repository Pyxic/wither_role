# -*- coding: utf-8 -*-
from fastapi_babel.core import lazy_gettext as _
from starlette import status

from .base import DefaultHTTPException


class UnauthorizedException(DefaultHTTPException):
    error = "UNAUTHORIZED"
    message = _("Credentials were not provided.")
    status_code = status.HTTP_403_FORBIDDEN


class InvalidCredentialsException(DefaultHTTPException):
    error = "LOGIN_BAD_CREDENTIALS"
    message = _("Invalid credentials.")
    status_code = status.HTTP_401_UNAUTHORIZED


class InvalidResetPasswordTokenException(DefaultHTTPException):
    error = "RESET_PASSWORD_BAD_TOKEN"
    message = _("Invalid token.")
    status_code = status.HTTP_400_BAD_REQUEST


class InsufficientRightsException(DefaultHTTPException):
    error = "INSUFFICIENT_RIGHTS"
    message = _("Insufficient rights to perform this action.")
    status_code = status.HTTP_403_FORBIDDEN


class RecaptchaFailException(DefaultHTTPException):
    error = "RECAPTCHA_TOKEN_ERROR"
    message = "reCAPTCHA token error."
    status = status.HTTP_403_FORBIDDEN
