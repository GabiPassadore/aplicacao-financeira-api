import json

from pydantic import Field
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    # App
    project_name: str = Field("aplicacao-financeira-api", env="PROJECT_NAME_API")
    hot_reload: bool = Field(False, env="HOT_RELOAD")
    hostname: str = Field("aplicacao-financeira-api", env="HOSTNAME")
    
    @property
    def formatted_deployment_name(self) -> str:
        return "-".join(self.hostname.split("-")[:-2])

      
class SentrySettings(BaseSettings):
    # Sentry
    sentry_dsn: str = Field("", env="SENTRY_DSN")
    sentry_environment: str = Field("", env="SENTRY_ENVIRONMENT")


class DatabaseSettings(BaseSettings):
    database_port: int = Field(5432, env='DATABASE_PORT')
    database_host: str = Field('localhost', env='DATABASE_HOST')
    database_name: str = Field('postgres', env='DATABASE_NAME')
    database_user: str = Field('postgres', env='DATABASE_USER')
    database_password: str = Field('postgres', env='DATABASE_PASSWORD')
    
    @property
    def database_sync_uri(self):
        return self._get_database_uri()
    
    @property
    def database_async_uri(self):
        return self._get_database_uri()

    def _get_database_uri(self) -> str:
        return f'postgresql+asyncpg://{self.database_user}:{self.database_password}@{self.database_host}:{self.database_port}/{self.database_name}'  # noqa E501


class Settings(BaseSettings):
    database_settings: DatabaseSettings = DatabaseSettings()
    app_settings: AppSettings = AppSettings()
    sentry_settings: SentrySettings = SentrySettings()
    
settings = Settings()
