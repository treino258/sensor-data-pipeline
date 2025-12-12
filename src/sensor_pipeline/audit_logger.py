import logging
import logging.handlers
from .config import AUDIT_LOG_FILE
from .logger_json import JsonFormatter


def get_audit_logger() -> logging.Logger:
    logger = logging.getLogger("audit")
    logger.setLevel(logging.INFO)

    if logger.handlers:
        return logger

    handler = logging.handlers.RotatingFileHandler(
        AUDIT_LOG_FILE, maxBytes=2_000_000, backupCount=5
    )
    handler.setFormatter(JsonFormatter())

    logger.addHandler(handler)

    return logger
