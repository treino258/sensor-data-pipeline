from typing import Dict, List
from sensor_pipeline.logger import get_logger

logger = get_logger(__name__)


def normalize_readings(parsed_data: Dict[str, Dict[str, List[float]]]) -> Dict[str, Dict[str, List[float]]]:
    """
    Normaliza os valores das leituras por sensor preservando os valores brutos.

    Input:
    {
        sensor: {
            "valid": [float, ...],
            "invalid": [...]
        }
    }

    Output:
    {
        sensor: {
            "raw": [...],
            "normalized": [...]
        }
    }
    """
    logger.info("Iniciando normalização das leituras.")

    result: Dict[str, Dict[str, List[float]]] = {}

    for sensor, data in parsed_data.items():
        raw_values = data.get("valid", [])

        if not raw_values:
            logger.warning(f"Sensor {sensor} não possui leituras válidas para normalização.")
            result[sensor] = {"raw": [], "normalized": []}
            continue

        min_v = min(raw_values)
        max_v = max(raw_values)

        if min_v == max_v:
            normalized = [0.0 for _ in raw_values]
        else:
            normalized = [
                (v - min_v) / (max_v - min_v)
                for v in raw_values
            ]

        result[sensor] = {
            "raw": raw_values,
            "normalized": normalized
        }

        logger.info(
            f"Sensor {sensor} normalizado ({len(raw_values)} valores)."
        )

    logger.info("Normalização concluída.")
    return result
