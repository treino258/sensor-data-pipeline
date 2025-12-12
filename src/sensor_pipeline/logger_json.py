import json
import logging
from datetime import datetime
from sensor_pipeline.context import correlation_id_ctx


class JSONFormatter(logging.Formatter):
    def format(self, record):
        """
        Formata a mensagem de log em JSON.
        
        returns:
            str: Mensagem de log formatada em JSON.
        
        args:
            record (logging.LogRecord): Registro de log a ser formatado.
            
        """
        
        log_record = {
            "timestamp": datetime.now().isoformat(),
            "level": record.levelname,
            "module": record.module,
            "message": record.getMessage(),
            "correlation_id": correlation_id_ctx.get(None),
        }
        
        return json.dumps(log_record, ensure_ascii=False)