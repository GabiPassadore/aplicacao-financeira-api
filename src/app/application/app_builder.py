from fastapi import Depends, FastAPI
from fastapi.middleware import Middleware
from loguru import logger

from src.app.application.rest import health, metric, person
from src.app.environment import settings 
from src.app.infra.logging.correlation_id import CorrelationIdMiddleware
from src.app.infra.logging.loguru import configure_logging
from src.app.infra.logging.request_logger import (
    RequestLoggerMiddleware,
)
from src.app.infra.monitoring.prometheus import PrometheusMiddleware
from src.app.infra.monitoring.sentry import Sentry


class AppBuilder:
    def with_sentry(self) -> "AppBuilder":
        if settings.sentry_settings.sentry_dsn:
            Sentry().start()

            logger.info("Sentry started")

        return self

    def create(self) -> FastAPI:
        configure_logging()

        middlewares = [
            Middleware(PrometheusMiddleware, app_name=settings.app_settings.formatted_deployment_name),
            Middleware(CorrelationIdMiddleware),
            Middleware(RequestLoggerMiddleware),
        ]
        app = FastAPI(
            title="Aplicação Financeira API",
            docs_url="/swagger",
            redoc_url=None,
            middleware=middlewares,
        )

        logger.info("API started")

        app.include_router(metric.router)
        app.include_router(health.router)
        app.include_router(person.router)

        return app
