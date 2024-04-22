from fastapi import APIRouter
from fastapi import Request

from config.settings import templates

auth_router = APIRouter()


@auth_router.get("/login/")
def get_login_page(request: Request):
    return templates.TemplateResponse("auth/login.html", {"request": request})

