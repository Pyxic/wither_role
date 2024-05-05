from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from fastapi import Request
from starlette.responses import HTMLResponse, RedirectResponse

from apps.auth.schemas import UserCreateSchema
from apps.auth.services import AuthService
from config.registry import Registry
from config.settings import templates
from utils.dependencies.csrf import generate_csrf_token, verify_csrf_token

auth_router = APIRouter()


@auth_router.get("/login/", response_class=HTMLResponse, name="auth:login")
def get_login_page(request: Request):
    return templates.TemplateResponse("auth/login.html", {"request": request})


@auth_router.get("/register/", response_class=HTMLResponse)
def get_register_page(request: Request, csrf: str = Depends(generate_csrf_token)):
    return templates.TemplateResponse("auth/register.html", {"request": request, "csrf_token": csrf})


@auth_router.post("/register/", response_class=RedirectResponse)
@inject
async def register_user(
        request: Request,
        csrf=Depends(verify_csrf_token),
        auth_service: AuthService = Depends(Provide[Registry.authentication.auth_service])):
    form_data = await request.form()
    user_create_schema = UserCreateSchema(**form_data)
    await auth_service.register(user_create_schema)
    return RedirectResponse(request.url_for("auth:login"), status_code=302)
