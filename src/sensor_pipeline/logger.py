import logging
import logging.handlers
from .config import (
    APP_LOG_FILE,
    ERROR_LOG_FILE,
    AUDIT_LOG_FILE,
    LOG_LEVEL,
)
from .logger_json import JsonFormatter


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(LOG_LEVEL)

    if logger.handlers:
        return logger

    # Formatter JSON
    json_formatter = JsonFormatter()

    # ───────────────────────────────────────────
    # HANDLER 1 — APP LOG (INFO, WARNING, DEBUG)
    # ───────────────────────────────────────────
    app_handler = logging.handlers.RotatingFileHandler(
        APP_LOG_FILE, maxBytes=2_000_000, backupCount=5
    )
    app_handler.setLevel(logging.INFO)
    app_handler.setFormatter(json_formatter)

    # Console (opcional, também JSON)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(json_formatter)

    # ───────────────────────────────────────────
    # HANDLER 2 — ERROR LOG (ERROR, CRITICAL)
    # ───────────────────────────────────────────
    error_handler = logging.handlers.RotatingFileHandler(
        ERROR_LOG_FILE, maxBytes=2_000_000, backupCount=5
    )
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(json_formatter)

    # Adiciona handlers
    logger.addHandler(app_handler)
    logger.addHandler(console_handler)
    logger.addHandler(error_handler)

    return logger