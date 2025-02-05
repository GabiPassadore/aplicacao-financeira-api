from fastapi import Request
from loguru import logger
from starlette.middleware.base import BaseHTTPMiddleware


async def log_request_body(request: Request) -> None:
    body = await request.body()

    if not body:
        return

    decoded_body = body.decode("utf-8").replace("\n", "").replace("  ", "")
    logger.info(f"Request body: {decoded_body}")


class RequestLoggerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_id = self._get_request_id(request)

        if self._should_skip_request_log(request):
            return await call_next(request)

        logger.info(f"Started {request_id}")

        try:
            response = await call_next(request)

            if response.status_code >= 200 and response.status_code < 400:
                logger.info(f"{request_id} successful - {response.status_code}")
            else:
                logger.error(f"{request_id} failed - {response.status_code}")

            return response
        except Exception as e:
            logger.error(f"{request_id} failed - {e}")
            raise e

    def _should_skip_request_log(self, request: Request) -> bool:
        return request.url.path in [
            "/metrics",
            "/healthcheck",
            "/swagger",
            "/favicon.ico",
            "/openapi.json",
        ]

    def _get_request_id(self, request: Request) -> str:
        url = request.url.path if not request.url.query else f"{request.url.path}?{request.url.query}"

        return f"{request.method} {url}"
