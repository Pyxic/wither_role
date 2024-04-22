from fastapi import APIRouter

from apps.auth.views import auth_router

api_router = APIRouter(prefix="")

api_router.include_router(auth_router, prefix="/auth")
