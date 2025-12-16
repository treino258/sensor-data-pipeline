from collections import defaultdict
from sensor_pipeline.logger import get_logger
from sensor_pipeline.config import SENSOR_THRESHOLDS

logger = get_logger(__name__)

def validate_quality(parsed_data: dict) -> None:
    """
    Valida a qualidade dos dados de sensores com base em limites predefinidos. 
    
    Args: valid_readings: Dicionário contendo leituras válidas por sensor. invalid_readings: Dicionário contendo leituras inválidas por sensor.
    
    Returns: 
    """
    
    logger.info("Iniciando validação de qualidade por sensor.")


    for sensor, data in parsed_data.items():
        valid = len(data["valid"])
        invalid = len(data["invalid"])
        total = valid + invalid
        
        if sensor == "UNKNOWN":
            logger.info("Ignorando sensor UNKNOWN na validação de qualidade")
            continue
        
        if total == 0:
            logger.warning(f"Sensor {sensor} sem leituras")
            continue

        invalid_ratio = invalid / total
        
        thresholds = SENSOR_THRESHOLDS.get(
            sensor,
            SENSOR_THRESHOLDS["DEFAULT"]
        )
        
        if not thresholds:
            logger.warning(f"Sensor {sensor} sem thresholds definidos. Ignorado.")
            continue

        max_ratio = thresholds["max_invalid_ration"]
        
        
        if invalid_ratio > max_ratio:
            logger.error(
                f"Sensor {sensor} com taxa inválida [invalid_ratio:.1%]"
                f"(limite {max_ratio:.1%})"
            )
            raise ValueError(f"Qualidade insuficiente para sensor {sensor}")
        
        
        elif invalid_ratio > max_ratio / 2:
            logger.warning(
                f"Sensor {sensor} próximo do limite ({invalid_ratio:.1%})"
            )
        else:
            logger.info(
                f"Sensor {sensor} dentro do esperado ({invalid_ratio:.1%})"
            )

    logger.info("Validação de qualidade concluída.")
            
        