from typing import AsyncIterator
from sqlalchemy.ext.asyncio import AsyncSession

from src.app.infra.data.database import get_session

async def resolve_session_db() -> AsyncIterator[AsyncSession]:
    async with get_session() as session:
        yield session
