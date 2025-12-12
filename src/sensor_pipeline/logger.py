
import logging
import logging.handlers
from sensor_pipeline.config import (
    APP_LOG_FILE,
    ERROR_LOG_FILE,
    AUDIT_LOG_FILE,
    LOG_LEVEL,
)
from sensor_pipeline.logger_json import JsonFormatter


def _resolve_level(level):
    import logging as _lg
    if isinstance(level, int):
        return level
    if isinstance(level, str):
        return getattr(_lg, level.upper(), _lg.INFO)
    return _lg.INFO


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(_resolve_level(LOG_LEVEL))

    if logger.handlers:
        return logger

    json_formatter = JsonFormatter()

    # APP handler (INFO+)
    app_handler = logging.handlers.RotatingFileHandler(
        APP_LOG_FILE, maxBytes=2_000_000, backupCount=5
    )
    app_handler.setLevel(_resolve_level(LOG_LEVEL))
    app_handler.setFormatter(json_formatter)

    # ERROR handler (ERROR+)
    error_handler = logging.handlers.RotatingFileHandler(
        ERROR_LOG_FILE, maxBytes=2_000_000, backupCount=5
    )
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(json_formatter)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(_resolve_level(LOG_LEVEL))
    console_handler.setFormatter(json_formatter)

    logger.addHandler(app_handler)
    logger.addHandler(error_handler)
    logger.addHandler(console_handler)

    return logger
