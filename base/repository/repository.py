from typing import List

from sqlalchemy import select, delete
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.exc import IntegrityError, SQLAlchemyError, NoResultFound, MultipleResultsFound
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import load_only

from config.database import Base
from utils.exceptions.http.api import AlreadyExistsException, DBException, NotFoundException, MultipleFoundException


class BaseRepository:
    model = None

    def __init__(self, model: Base, db_session: AsyncSession):
        """
        Initializes the BaseRepository with the specified model and database session.

        :param model: The model to be used in the repository.
        :param db_session: The asynchronous session to interact with the database.
        """
        self.session_factory = db_session
        self.model = model

    async def create(self, data: dict):
        async with self.session_factory() as session:
            instance = self.model(**data)
            session.add(instance)
            try:
                await session.commit()
            except IntegrityError:
                raise AlreadyExistsException(f"object {self.model.__name__} already exists.")
            return instance

    async def bulk_create(self, data: List[dict]):
        async with self.session_factory() as session:
            stmt = insert(self.model).values(data).returning(self.model)
            try:
                result = await session.execute(stmt)
            except IntegrityError:
                raise AlreadyExistsException(f"object {self.model.__name__} already exists.")
            try:
                await session.commit()
            except SQLAlchemyError as e:
                return DBException(str(e))
            return result.scalar()

    async def update(self, data: dict, filters=None):
        async with self.session_factory() as session:
            if not data:
                raise DBException(f"Pass empty data to update {self.model}")
            query = select(self.model)
            if filters:
                query = query.filter_by(**filters)
            try:
                result = await session.execute(query)
                obj = result.one()[0]
            except NoResultFound:
                raise NotFoundException()

            for key, value in data.items():
                if not hasattr(obj, key):
                    raise DBException(f"Field {key} not exists in {self.model.__name__}")
                setattr(obj, key, value)

            try:
                await session.commit()
            except IntegrityError:
                raise AlreadyExistsException(f"object {self.model.__name__} already exists.")
            return obj

    async def delete(self, **filters):
        async with self.session_factory() as session:
            result = await session.execute(delete(self.model).filter_by(**filters))
            if result.rowcount == 0:
                raise NotFoundException()
            await session.commit()

    async def get(
            self,
            filters=None,
            fields: List[str] | None = None,
            order_by = None,
            limit: int | None = None,
            offset: int | None = None
    ):
        async with self.session_factory() as session:
            stmt = select(self.model)

            if filters:
                stmt = stmt.filter_by(**filters)
            if fields:
                model_fields = [getattr(self.model, field) for field in fields]
                stmt = stmt.options(load_only(*model_fields))
            if order_by is not None:
                stmt = stmt.order_by(order_by)
            if limit is not None:
                stmt = stmt.limit(limit)
            if offset is not None:
                stmt = stmt.offset(offset)

            row = await session.execute(stmt)
            return row.scalars.all()

    async def filter(self, **filters):
        return await self.get(filters)

    async def get_single(self, **filters):
        async with self.session_factory() as session:
            row = await session.execute(select(self.model).filter_by(**filters))
            try:
                result = row.scalar_one()
            except NoResultFound:
                raise NotFoundException()
            except MultipleResultsFound:
                raise MultipleFoundException(f"for model {self.model.__name__} found multiple rows")

    async def exists(self, **filters) -> bool:
        stmt = select(self.model).filter_by(**filters)
        async with self.session_factory() as session:
            result = await session.execute(stmt)
            return result.scalar() is not None
