
import logging
from logging.handlers import RotatingFileHandler
from sensor_pipeline.config import (
    LOG_FILE,
    LOG_LEVEL,
)
from sensor_pipeline.logger_json import JsonFormatter
from sensor_pipeline.context import correlation_id_ctx



class ContextFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        record.correlation_id = correlation_id_ctx.get()
        return True


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(LOG_LEVEL)

    if logger.handlers:
        return logger

    formatter = JsonFormatter()

    # Console
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    console.addFilter(ContextFilter())

    # File (único arquivo)
    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=10 * 1024 * 1024,
        backupCount=5,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)
    file_handler.addFilter(ContextFilter())

    logger.addHandler(console)
    logger.addHandler(file_handler)

    logger.propagate = False
    return logger
