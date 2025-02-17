import sentry_sdk
from sentry_sdk.integrations.fastapi import FastApiIntegration
from sentry_sdk.integrations.loguru import LoguruIntegration
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration
from sentry_sdk.integrations.starlette import StarletteIntegration

from src.app.environment import settings


class Sentry:
    def start(self) -> None:
        sentry_sdk.init(
            dsn=settings.sentry_settings.sentry_dsn,
            environment=settings.sentry_settings.sentry_environment,
            integrations=[
                StarletteIntegration(transaction_style='url'),
                FastApiIntegration(transaction_style='url'),
                SqlalchemyIntegration(),
                LoguruIntegration(),
            ],
            send_default_pii=True,
            attach_stacktrace=True,
            traces_sample_rate=1.0,
        )
