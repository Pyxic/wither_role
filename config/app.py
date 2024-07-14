# -*- coding: utf-8 -*-
import pathlib
from contextlib import asynccontextmanager

import toml
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

from config.admin import admin_router
from config.registry import registry
from config.router import api_router
from config.settings import settings


def add_middleware(app_):
    """
    Add middleware.
    """
    app_.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origin_whitelist,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app_.add_middleware(SessionMiddleware, secret_key=settings.secret_key)


def init_routers(app_: FastAPI) -> None:
    app_.include_router(api_router, prefix="/api")


# extract title from pyproject.toml
def get_project_data() -> dict:
    pyproject_path = pathlib.Path("pyproject.toml")
    pyproject_data = toml.load(pyproject_path.open())
    poetry_data = pyproject_data["tool"]["poetry"]
    return poetry_data


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    yield


def get_application() -> FastAPI:
    poetry_data = get_project_data()

    app_ = FastAPI(
        lifespan=lifespan,
        title=poetry_data["name"],
        description=poetry_data["description"],
        version=poetry_data["version"],
        openapi_url="/api/documentation/openapi.json",
        docs_url="/api/documentation/",
        redoc_url="/api/documentation/redoc/",
    )

    # Initialize other utils.
    init_routers(app_=app_)
    add_middleware(app_)

    return app_


app_fastapi = get_application()
admin_router(app_fastapi)
registry.wire()
