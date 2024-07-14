# -*- coding: utf-8 -*-
from dependency_injector import containers, providers

from apps.character.models import Attribute
from apps.user.models import User
from apps.user.repository import UserRepository


class CharacterContainer(containers.DeclarativeContainer):
    """
    Container for user services.
    """

    gateways_container = providers.DependenciesContainer()

    attribute_repository = providers.Singleton(
        UserRepository,
        model=Attribute,
        db_session=gateways_container.session_factory
    )
