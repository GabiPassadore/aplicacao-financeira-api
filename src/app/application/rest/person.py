from fastapi import Depends, Response, status
from loguru import logger
from src.app.application.common.dependencies import resolve_create_person_usecase, resolve_get_person_usecase, resolve_session_db
from src.app.application.common.custom_router import CustomAPIRouter
from src.app.domain.person.schemas import PersonCreateSchema
from src.app.domain.person.usecases.create_person import CreatePerson
from src.app.domain.person.usecases.get_person_by_id import GetPersonById
from src.app.infra.data.person.repository import PersonRepository
from sqlalchemy.orm import Session

router = CustomAPIRouter(
    prefix='/person',
    tags=['Person'],
)

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_person(
    data:PersonCreateSchema,
    use_case: CreatePerson = Depends(resolve_create_person_usecase),  
) -> Response:
    return await use_case.execute(data=data)

@router.get('/{person_id}', status_code=status.HTTP_200_OK)
async def get_person_by_id(
    person_id: int,
    use_case: GetPersonById = Depends(resolve_get_person_usecase),  
) -> Response:
    return await use_case.execute(_id=person_id)