# -*- coding: utf-8 -*-
from dependency_injector import containers, providers

from apps.auth.containers import AuthContainer
from apps.character.containers import CharacterContainer
from apps.user.containers import UserContainer
from config.database import DatabaseHelper


class Gateways(containers.DeclarativeContainer):
    database_client = providers.Singleton(DatabaseHelper)

    session_factory = providers.Singleton(
        database_client.provided.get_db_session,
    )


class Registry(containers.DeclarativeContainer):
    """
    Registry container. It is a root container for all other containers.

    It is used to provide access to all other containers from any place
    of the application.

    """

    wiring_config: containers.WiringConfiguration = containers.WiringConfiguration(
        packages=[
            "apps.user",
            "apps.auth",
            "apps.character",
            "config.commands",
        ],
    )

    gateways_container = providers.Container(Gateways)

    user_container = providers.Container(UserContainer, gateways_container=gateways_container)
    character_container = providers.Container(CharacterContainer, gateways_container=gateways_container)
    authentication = providers.Container(AuthContainer, user_container=user_container)


registry = Registry()


def wire_packages(registry_object: Registry):
    registry_object.wire()
