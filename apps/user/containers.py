# -*- coding: utf-8 -*-
from dependency_injector import containers, providers

from apps.user.models import User
from apps.user.repository import UserRepository


class UserContainer(containers.DeclarativeContainer):
    """
    Container for user services.
    """

    gateways_container = providers.DependenciesContainer()

    repository = providers.Singleton(
        UserRepository,
        model=User,
        db_session=gateways_container.session_factory
    )
