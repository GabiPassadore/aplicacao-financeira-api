import json

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # App
    project_name: str = Field("aplicacao-financeira-api", env="PROJECT_NAME_API")
    hot_reload: bool = Field(False, env="HOT_RELOAD")

    # Sentry
    sentry_dsn: str = Field("", env="SENTRY_DSN")
    sentry_environment: str = Field("", env="SENTRY_ENVIRONMENT")

    # Project settings
    hostname: str = Field(None, env="HOSTNAME")

    @property
    def formatted_deployment_name(self) -> str:
        return "-".join(self.hostname.split("-")[:-2])


settings = Settings()
