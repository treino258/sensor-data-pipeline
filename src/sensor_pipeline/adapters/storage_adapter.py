from typing import Dict, List
from datetime import datetime

def to_storage_records(
    pipeline_output: Dict[str, Dict[str, List[float]]],
    correlation_id: str
) -> List[Dict]:
    """
    Converte a saída do pipeline em registros flat para armazenamento.
    """
    records = []
    timestamp = datetime.utcnow().isoformat()

    for sensor, data in pipeline_output.items():
        for raw, norm in zip(data["raw"], data["normalized"]):
            records.append({
                "sensor": sensor,
                "raw": raw,
                "normalized": norm,
                "timestamp": timestamp,
                "correlation_id": correlation_id
            })

    return records
