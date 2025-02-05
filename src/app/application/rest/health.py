from fastapi import Response, status

from src.app.application.common.custom_router import CustomAPIRouter

router = CustomAPIRouter(
    prefix='/healthcheck',
    tags=['Healthcheck'],
)

@router.get('/', status_code=status.HTTP_200_OK)
def healthcheck() -> Response:
    return {'status': 'alive'}
