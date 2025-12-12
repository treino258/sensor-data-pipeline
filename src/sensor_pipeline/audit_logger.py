
import logging
import logging.handlers
from sensor_pipeline.config import AUDIT_LOG_FILE
from sensor_pipeline.logger_json import JsonFormatter

def get_audit_logger() -> logging.Logger:
    audit = logging.getLogger("audit")
    audit.setLevel(logging.INFO)

    if audit.handlers:
        return audit

    handler = logging.handlers.RotatingFileHandler(
        AUDIT_LOG_FILE, maxBytes=2_000_000, backupCount=5
    )
    handler.setFormatter(JsonFormatter())
    handler.setLevel(logging.INFO)

    audit.addHandler(handler)
    return audit
