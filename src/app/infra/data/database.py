from asyncio import current_task
from contextlib import asynccontextmanager
from typing import AsyncIterator

from sqlalchemy.ext.asyncio import AsyncSession, async_scoped_session, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.scoping import scoped_session

from src.app.environment import settings

AsyncSessionLocal = sessionmaker(
    bind=create_async_engine(url=settings.database_settings.database_sync_uri),
    class_=AsyncSession,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
    future=True,
)


@asynccontextmanager
async def get_session() -> AsyncIterator[AsyncSession]:
    scoped_session_: scoped_session = async_scoped_session(
        session_factory=AsyncSessionLocal, scopefunc=current_task
    )

    try:
        yield scoped_session_()

        await scoped_session_.commit()
    except:  # noqa
        await scoped_session_.rollback()
        raise
    finally:
        await scoped_session_.remove()


