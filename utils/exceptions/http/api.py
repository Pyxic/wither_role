# -*- coding: utf-8 -*-
from starlette import status
from utils.exceptions import DefaultHTTPException


class NotFoundException(DefaultHTTPException):
    error = "NOT_FOUND"
    message = "The requested resource was not found."
    status_code = status.HTTP_404_NOT_FOUND


class RateLimitException(DefaultHTTPException):
    status_code: int = 429
    error: str = "RATE_LIMIT_EXCEPTION"
    message = "Too many requests"


class AlreadyExistsException(DefaultHTTPException):
    status_code: int = 400
    error: str = "ALREADY_EXISTS"
    message = "Object already exists"


class DBException(DefaultHTTPException):
    status_code: int = 400
    error: str = "DB_ERROR"


class MultipleFoundException(DefaultHTTPException):
    status_code: int = 400
    error: str = "MULTIPLE_FOUND"
