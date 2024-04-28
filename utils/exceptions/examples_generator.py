# -*- coding: utf-8 -*-
from typing import Optional, Type

from starlette import status
from utils.exceptions.http.auth import InsufficientRightsException, InvalidCredentialsException, UnauthorizedException
from utils.exceptions.http.base import DefaultHTTPException


class ExamplesGenerator:
    auth_error = (
        UnauthorizedException,
        InvalidCredentialsException,
        InsufficientRightsException,
    )

    @staticmethod
    def generate_nested_schema_for_code(responses, error_code):
        responses[error_code] = {}
        responses[error_code]["content"] = {}
        responses[error_code]["content"]["application/json"] = {}

    @classmethod
    def get_error_responses(cls, *args: Optional[Type[DefaultHTTPException]], auth: bool = False) -> dict:
        responses = {}
        if auth:
            args += cls.auth_error

        error_codes = {error.status_code for error in args}

        for error_code in error_codes:
            examples = {}

            for error in args:
                instance = error()  # noqa
                if instance.status_code == error_code:
                    examples[instance.error] = instance.example()

            cls.generate_nested_schema_for_code(responses, error_code)
            responses[error_code]["content"]["application/json"]["examples"] = examples

        cls.change_422_validation_schema(responses)

        return responses

    @classmethod
    def change_422_validation_schema(cls, responses):
        cls.generate_nested_schema_for_code(responses, status.HTTP_422_UNPROCESSABLE_ENTITY)
        example = {
            "validation_errors": {
                "summary": "Validation Error",
                "value": [
                    {
                        "code": "validation-error",
                        "type": "string",
                        "message": "string",
                        "field": "string",
                    },
                ],
            },
        }
        responses[status.HTTP_422_UNPROCESSABLE_ENTITY]["content"]["application/json"]["examples"] = example


generate_examples = ExamplesGenerator.get_error_responses
