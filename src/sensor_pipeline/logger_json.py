import json
import logging
from datetime import datetime
from sensor_pipeline.context import correlation_id_ctx


class JsonFormatter(logging.Formatter):
    """
    Formata logs como JSON em uma única linha.
    """

    def format(self, record: logging.LogRecord) -> str:
        correlation_id = correlation_id_ctx.get()

        log_data = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "module": record.name,
            "message": record.getMessage(),
            "correlation_id": correlation_id if correlation_id else None,
        }

        return json.dumps(log_data, ensure_ascii=False)
