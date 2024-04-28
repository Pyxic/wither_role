# -*- coding: utf-8 -*-
from dependency_injector import containers, providers


class Registry(containers.DeclarativeContainer):
    """
    Registry container. It is a root container for all other containers.

    It is used to provide access to all other containers from any place
    of the application.

    """

    wiring_config: containers.WiringConfiguration = containers.WiringConfiguration(
        packages=[
        ],
    )


registry = Registry()


def wire_packages(registry_object: Registry):
    registry_object.wire()
