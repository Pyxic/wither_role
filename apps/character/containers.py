# -*- coding: utf-8 -*-
from dependency_injector import containers, providers

from apps.character.models import Attribute, Race, Region, FamilyFate, ParentFate, FamilySituation, Friend, \
    ImportantEvent, Profession, Skill
from apps.character.services import SkillService, AttributeService
from apps.user.models import User
from apps.character.repository import AttributeRepository
from base.repository.repository import BaseRepository


class CharacterContainer(containers.DeclarativeContainer):
    """
    Container for user services.
    """

    gateways_container = providers.DependenciesContainer()

    attribute_repository = providers.Singleton(
        AttributeRepository,
        model=Attribute,
        db_session=gateways_container.session_factory
    )
    skill_repository = providers.Singleton(
        BaseRepository,
        model=Skill,
        db_session=gateways_container.session_factory
    )
    race_repository = providers.Singleton(
        BaseRepository,
        model=Race,
        db_session=gateways_container.session_factory
    )
    region_repository = providers.Singleton(
        BaseRepository,
        model=Region,
        db_session=gateways_container.session_factory
    )
    family_fate_repository = providers.Singleton(
        BaseRepository,
        model=FamilyFate,
        db_session=gateways_container.session_factory,
    )
    parent_fate_repository = providers.Singleton(
        BaseRepository,
        model=ParentFate,
        db_session=gateways_container.session_factory,
    )
    family_situation_repository = providers.Singleton(
        BaseRepository,
        model=FamilySituation,
        db_session=gateways_container.session_factory
    )
    friend_repository = providers.Singleton(
        BaseRepository,
        model=Friend,
        db_session=gateways_container.session_factory
    )
    important_event_repository = providers.Singleton(
        BaseRepository,
        model=ImportantEvent,
        db_session=gateways_container.session_factory
    )
    profession_repository = providers.Singleton(
        BaseRepository,
        model=Profession,
        db_session=gateways_container.session_factory,
    )

    skill_service = providers.Singleton(
        SkillService,
        skill_repository=skill_repository,
    )

    attribute_service = providers.Singleton(
        AttributeService,
        attribute_repository=attribute_repository
    )
