from fastapi.exceptions import RequestValidationError
from fastapi import Request, Response, status
from pydantic import ValidationError
from starlette.responses import JSONResponse

from utils.exceptions import DefaultHTTPException


def register_exception_handlers(app):
    """
    Register exception handlers.
    """

    @app.exception_handler(RequestValidationError)
    async def request_validation_errors_handler(request: Request, exc: RequestValidationError) -> Response:
        """
        Handle validation errors.
        """
        error_list = []
        for error in exc.errors():
            loc = error["loc"]
            location = loc[0]
            field = loc[1] if len(loc) > 1 else None
            message = error["msg"]
            error_list.append({"location": location, "field": field, "message": message.capitalize()})
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={
                "status": status.HTTP_422_UNPROCESSABLE_ENTITY,
                "error": {"code": "VALIDATION_ERROR", "details": error_list},
            },
        )

    @app.exception_handler(ValidationError)
    async def validation_errors_handler(request: Request, exc: ValidationError) -> Response:
        """
        Handle validation errors.
        """
        error_list = []
        for error in exc.errors():
            location = "query"
            field = error["loc"][0]
            message = str(error["msg"])
            error_list.append(
                {
                    "location": location,
                    "field": field,
                    "message": message.capitalize(),
                },
            )
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={
                "status": status.HTTP_422_UNPROCESSABLE_ENTITY,
                "error": {"code": "VALIDATION_ERROR", "details": error_list},
            },
        )

    @app.exception_handler(DefaultHTTPException)
    async def http_exceptions_handler(request: Request, exc: DefaultHTTPException) -> JSONResponse:
        """
        Handle all HTTP exceptions.
        """
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "status": exc.status_code,
                "error": {
                    "code": exc.error,
                    "details": {
                        "message": str(exc.message),
                    },
                },
            },
        )