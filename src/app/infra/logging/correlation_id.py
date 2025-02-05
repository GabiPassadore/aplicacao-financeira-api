import contextvars
import uuid
from typing import Optional

from fastapi import Request
from loguru import logger
from starlette.middleware.base import BaseHTTPMiddleware

correlation_id_context: Optional[str] = contextvars.ContextVar("correlation_id", default=None)


class CorrelationIdMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        correlation_id = request.headers.get('X-Correlation-ID')

        if not correlation_id:
            correlation_id = str(uuid.uuid4())

        correlation_id_context.set(correlation_id)

        logger.bind(correlation_id=correlation_id)

        response = await call_next(request)

        response.headers['X-Correlation-ID'] = correlation_id

        return response
