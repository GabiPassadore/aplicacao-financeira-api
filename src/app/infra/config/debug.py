from loguru import logger


def set_debugpy() -> None:
    import debugpy
    debugpy.listen(('0.0.0.0', 5678))
    logger.info("[*] Debug Started!")


__all__ = ["set_debugpy"]
