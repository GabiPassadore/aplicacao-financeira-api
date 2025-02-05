from starlette.config import Config
from loguru import logger

env = Config()
logger.info("[*] Env Started!")