from asyncio import current_task
from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, async_scoped_session, AsyncSession
from sqlalchemy.orm import DeclarativeBase, declared_attr

from config.settings import settings


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}"


class DatabaseHelper:

    def __init__(self):
        self.engine = create_async_engine(
            url=settings.db_url,
            echo=settings.postgres_echo
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            expire_on_commit=False,
            autocommit=False
        )

    def get_scope_session(self):
        return async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task
        )

    @asynccontextmanager
    async def get_db_session(self):
        from sqlalchemy import exc

        session: AsyncSession = self.session_factory()
        try:
            yield session
        except exc.SQLAlchemyError as error:
            await session.rollback()
            raise
        finally:
            await session.close()


db_helper = DatabaseHelper()
