from typing import AsyncIterator
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.app.domain.person.usecases.create_person import CreatePerson
from src.app.domain.person.usecases.get_person_by_id import GetPersonById
from src.app.infra.data.database import get_session
from src.app.infra.data.person.repository import PersonRepository


async def resolve_session_db() -> AsyncIterator[AsyncSession]:
    async with get_session() as session:
        yield session  


async def resolve_person_repository(
    session: AsyncSession = Depends(resolve_session_db),  
) -> AsyncIterator[PersonRepository]:
    yield PersonRepository(session=session)


async def resolve_create_person_usecase(
    repository: PersonRepository = Depends(resolve_person_repository),  
) -> AsyncIterator[CreatePerson]:
    yield CreatePerson(repository=repository)

async def resolve_get_person_usecase(
    repository: PersonRepository = Depends(resolve_person_repository),
) -> AsyncIterator[CreatePerson]:
    yield GetPersonById(repository=repository)
