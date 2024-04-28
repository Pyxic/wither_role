from fastapi import APIRouter
from fastapi import Request
from starlette.responses import HTMLResponse, RedirectResponse

from config.settings import templates

auth_router = APIRouter()


@auth_router.get("/login/", response_class=HTMLResponse, name="auth:login")
def get_login_page(request: Request):
    return templates.TemplateResponse("auth/login.html", {"request": request})


@auth_router.get("/register/", response_class=HTMLResponse)
def get_register_page(request: Request):
    return templates.TemplateResponse("auth/register.html", {"request": request})


@auth_router.post("/register/", response_class=RedirectResponse)
def register_user(request: Request):
    print(request)
    return RedirectResponse(request.url_for("auth:login"), status_code=302)
