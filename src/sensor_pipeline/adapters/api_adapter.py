from typing import Dict, List

def to_api_response(
    pipeline_output: Dict[str, Dict[str, List[float]]]
) -> List[Dict]:
    """
    Converte a saída do pipeline para resposta JSON amigável.
    """
    response = []

    for sensor, data in pipeline_output.items():
        response.append({
            "sensor": sensor,
            "raw": data["raw"],
            "normalized": data["normalized"]
        })

    return response
