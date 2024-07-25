# -*- coding: utf-8 -*-
from typing import Optional

from fastapi import Request, Response
from fastapi_babel.middleware import InternationalizationMiddleware
from starlette.middleware.base import RequestResponseEndpoint

from config.settings import settings


class CustomInternationalizationMiddleware(InternationalizationMiddleware):
    async def dispatch(
        self,
        request: Request,
        call_next: RequestResponseEndpoint,
    ) -> Response:
        """
        Dispatch function.

        Args:
            request (Request): ...
            call_next (RequestResponseEndpoint): ...

        Returns:
            Response: ...

        """
        lang_code: Optional[str] = request.headers.get("Accept-Language", None)
        if lang_code and lang_code in settings.languages:
            self.babel.locale = lang_code.split(",")[0]
        response: Response = await call_next(request)
        return response
