import uvicorn
from loguru import logger
from src.app.environment import settings


if __name__ == '__main__':
    uvicorn.run('src.app.server:app', host='0.0.0.0', port=8000, reload=settings.hot_reload)

    logger.info('[*] Server Started!')