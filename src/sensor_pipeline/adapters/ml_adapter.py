from typing import List, Dict

def to_ml_input(
    pipeline_output: Dict[str, Dict[str, List[float]]]
) -> Dict[str, List[float]]:
    """
    Converte a saída do pipeline para formato consumível por ML.
    Retorna apenas valores normalizados por sensor.
    
    return:
    
    args:
    """
    
    
    return {
        sensor: data["normalized"]
        for sensor, data in pipeline_output.items()
        if data["normalized"]
    }