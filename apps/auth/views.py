from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from fastapi import Request
from starlette.responses import Response

from apps.auth.schemas import UserCreateSchema
from apps.auth.services import AuthService
from config.registry import Registry

auth_router = APIRouter()


# @auth_router.get("/login/", response_class=HTMLResponse, name="auth:login")
# def get_login_page(request: Request):
#     return templates.TemplateResponse("auth/login.html", {"request": request})


@auth_router.post("/register/")
@inject
async def register_user(
        request: Request,
        user_create_schema: UserCreateSchema,
        auth_service: AuthService = Depends(Provide[Registry.authentication.auth_service])
):
    await auth_service.register(user_create_schema)
    return Response(True)
