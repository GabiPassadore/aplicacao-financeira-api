from fastapi import Response, status
from prometheus_client import REGISTRY
from src.app.application.common.custom_router import CustomAPIRouter
from prometheus_client.openmetrics.exposition import CONTENT_TYPE_LATEST, generate_latest

router = CustomAPIRouter(
    prefix="/metrics",
    tags=["Metrics"],
)

@router.get("/", status_code=status.HTTP_200_OK)
def metrics() -> Response:
    return Response(generate_latest(REGISTRY), headers={'Content-Type': CONTENT_TYPE_LATEST})