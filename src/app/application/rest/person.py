from fastapi import Depends, Response, status
from loguru import logger
from src.app.application.common.dependencies import resolve_create_person_usecase, resolve_session_db
from src.app.application.common.custom_router import CustomAPIRouter
from src.app.domain.person.schemas import PersonCreateSchema
from src.app.domain.person.usecases.create_person import CreatePerson
from src.app.infra.data.person.repository import PersonRepository
from sqlalchemy.orm import Session

router = CustomAPIRouter(
    prefix='/person',
    tags=['Person'],
)

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_person(
    data:PersonCreateSchema,
     use_case: CreatePerson = Depends(resolve_create_person_usecase),  # ✅ FastAPI injeta automaticamente
) -> Response:
    return await use_case.execute(data=data)

@router.get('/', status_code=status.HTTP_200_OK)
async def get_persons() -> Response:
    logger.info('Persons recuperados')
    return {'status': 'alive'}