from typing import List, Tuple, Dict
from collections import defaultdict
from sensor_pipeline.logger import get_logger

logger = get_logger(__name__)

def parse_lines_data(lines: List[str]) -> Dict[str, dict[str, list]]:
    """
    
    Valida os seguintes tópicos de acordo com o dataset atual por linha:
      - 1 “=”
      - chave não vazia
      - valor não vazio
      - valor convertível para float
      - caracteres válidos
      - padrão “chave=valor”
      - agrupa os dados válidos e inválidos em listas separadas.

    Returns:
        Valida e agrupa leituras por sensor. O formato retornado é:
    {
        sensor: {
            "valid": [float],
            "invalid": [dict]
        }
    }
        
    Args:
        lines: lista de linhas a serem analisadas.
        
    """
    
    logger.info("Iniciando análise e validação dos dados.")
    
    data = defaultdict(lambda: {"valid": [], "invalid": []})
 
    for index, line in enumerate(lines, start=1):
        
        if line.count('=') != 1:
            data["UNKNOWN"]["invalid"].append({
                "line": index,
                "conteudo": line,
                "erro": "expected_single_equal_sign"
            })
            continue
        
        chave, valor = line.split('=', 1)
        chave = chave.strip()
        valor = valor.strip()
        
        # chave vazia
        if not chave:
            data["UNKOWN"]["invalid"].append({
                "linha": index,
                "conteudo": line,
                "erro": "empty_key"
            })
            continue
        
        # valor vazio
        if not valor:
            data[chave]["invalid"].append({
                "linha": index,
                "conteudo": line,
                "erro": "empty_value"
            })
            continue
        
        # conversão para float
        try:
            valor_float = float(valor)
        except ValueError:
            data[chave]["invalid"].append({
                "linha": index,
                "conteudo": line,
                "erro": "invalid_float_value"
            })
            continue
        
        data[chave]["valid"].append(valor_float)
        
        logger.info(f"Parse concluído. Sensore detectado: {list(data.keys())}")
        
    return dict[data]