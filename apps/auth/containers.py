# -*- coding: utf-8 -*-
from dependency_injector import containers, providers

from apps.auth.services import AuthService
from config.settings import settings
from utils.security.jwt_backend import JWTBackend


class AuthContainer(containers.DeclarativeContainer):
    user_container = providers.DependenciesContainer()

    jwt_backend = providers.Singleton(
        JWTBackend,
        access_expiration=settings.jwt_access_expiration,
        refresh_expiration=settings.jwt_refresh_expiration,
        jwt_secret=settings.jwt_secret,
        jwt_algorithm=settings.jwt_algorithm,
    )

    auth_service = providers.Singleton(
        AuthService,
        user_repository=user_container.repository,
        jwt_backend=jwt_backend,
    )