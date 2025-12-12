from typing import List, Dict
from sensor_pipeline.logger import get_logger

def normalize_readings(readings: List[Dict[str, float]]) -> Dict[str, List[float]]:
    """
    Normaliza os valores das leituras.
        - pegar uma lista de leituras (sensor, value)
        
        - agrupa por sensor

        - acumula valores em listas

        - garante estrutura consistente para processamento posterior

        - não perder a ordem

    Returns:
        Dict[str, List[float]]: um dicionário onde as chaves são os nomes das variáveis
        e os valores são listas de valores normalizados correspondentes.

    Args:
        readings: lista de dicionários contendo as leituras com chaves como nomes de variáveis
                  e valores como floats.
    """
    logger = get_logger(__name__)
    
    normalized_readings: Dict[str, List[float]] = {}
    
    for entry in readings:
        sensor = entry["sensor"]
        valor = entry["value"]
        
        if sensor not in normalized_readings:
            normalized_readings[sensor] = []
            
        normalized_readings[sensor].append(valor)
        
    logger.info(f"Normalização concluída. Sensores normalizados: {list(normalized_readings.keys())}")
    
    return normalized_readings