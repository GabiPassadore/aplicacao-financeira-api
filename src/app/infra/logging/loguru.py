import logging
import sys

from loguru import logger

from src.app.infra.logging.correlation_id import correlation_id_context


def _exclude_logs() -> None:
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
    logging.getLogger("uvicorn.error").setLevel(logging.CRITICAL)
    logging.getLogger("uvicorn").setLevel(logging.WARNING)


def _correlation_id_filter(record):
    record["extra"]["correlation_id"] = correlation_id_context.get()
    return True


def configure_logging() -> None:
    logger.remove()
    logger.configure(
        handlers=[
            {
                "sink": sys.stdout,
                "format": (
                    "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
                    "<level>{level: <8}</level> | "
                    "<level>{extra[correlation_id]} - {message}</level>"
                ),
                "filter": _correlation_id_filter,
            }
        ]
    )

    logger.configure(extra={"correlation_id": '00000000-0000-0000-0000-000000000000'})

    _exclude_logs()
