from src.app.application.app_builder import AppBuilder

app = AppBuilder().with_sentry().create()
