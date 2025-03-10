from fastapi import Response, status
from loguru import logger
from src.app.application.common.custom_router import CustomAPIRouter

router = CustomAPIRouter(
    prefix='/person',
    tags=['Person'],
)

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_person() -> Response:
    logger.info('Person criado')
    return {'status': 'alive'}

@router.get('/', status_code=status.HTTP_200_OK)
async def get_persons() -> Response:
    logger.info('Persons recuperados')
    return {'status': 'alive'}