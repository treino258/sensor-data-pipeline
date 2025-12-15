from collections import defaultdict
from sensor_pipeline.logger import get_logger
from sensor_pipeline.config import SENSOR_THRESHOLDS

logger = get_logger(__name__)

def validate_quality(valid_readings, invalid_readings):
    """
    Valida a qualidade dos dados de sensores com base em limites predefinidos. 
    
    Args: valid_readings: Dicionário contendo leituras válidas por sensor. invalid_readings: Dicionário contendo leituras inválidas por sensor.
    
    Returns: 
    """
    
    logger.info("Iniciando validação de qualidade por sensor.")

    stats = defaultdict(lambda: {"valid": 0, "invalid": 0})

    for r in valid_readings:
        stats[r["sensor"]]["valid"] += 1

    for r in invalid_readings:
        sensor = r.get("sensor", "DEFAULT")
        stats[sensor]["invalid"] += 1

    for sensor, counts in stats.items():
        total = counts["valid"] + counts["invalid"]
        if total == 0:
            continue

        ratio = counts["invalid"] / total
        max_ratio = SENSOR_THRESHOLDS.get(
            sensor, SENSOR_THRESHOLDS["DEFAULT"]
        )["max_invalid_ratio"]

        if ratio > max_ratio:
            logger.error(
                f"Sensor {sensor}: {ratio:.1%} inválidas (limite {max_ratio:.1%})"
            )
            raise ValueError(f"Qualidade insuficiente para sensor {sensor}")

        elif ratio > max_ratio / 2:
            logger.warning(
                f"Sensor {sensor}: {ratio:.1%} inválidas (próximo do limite)"
            )
        else:
            logger.info(
                f"Sensor {sensor}: qualidade ok ({ratio:.1%} inválidas)"
            )
