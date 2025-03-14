from typing import AsyncIterator
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.app.domain.person.usecases.create_person import CreatePerson
from src.app.infra.data.database import get_session
from src.app.infra.data.person.repository import PersonRepository

# 🔹 Resolve a sessão do banco de dados
async def resolve_session_db() -> AsyncIterator[AsyncSession]:
    async with get_session() as session:
        yield session  # Retorna a sessão para quem precisar dela

# 🔹 Resolve o repositório de pessoas
async def resolve_person_repository(
    session: AsyncSession = Depends(resolve_session_db),  # ✅ Dependência correta
) -> AsyncIterator[PersonRepository]:
    yield PersonRepository(session=session)

# 🔹 Resolve o caso de uso de criação de pessoa
async def resolve_create_person_usecase(
    repository: PersonRepository = Depends(resolve_person_repository),  # ✅ Dependência correta
) -> AsyncIterator[CreatePerson]:
    yield CreatePerson(repository=repository)