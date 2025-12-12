from typing import List, Tuple, Dict
from sensor_pipeline.logger import get_logger



def parse_lines_data(lines: List[str]) -> Tuple[List[Dict], List[Dict]]:
    """
    
    Valida os seguintes tópicos de acordo com o dataset atual por linha:
      - 1 “=”
      - chave não vazia
      - valor não vazio
      - valor convertível para float
      - caracteres válidos
      - padrão “chave=valor”

    Returns:
        Tuple[List[Dict], List[Dict]]: uma tupla contendo duas listas de dicionários.
            A primeira lista contém os dados válidos.
            A segunda lista contém os dados inválidos (linhas que não seguem o formato esperado).
        
    Args:
        lines: lista de linhas a serem analisadas.
        
    """
    logger = get_logger(__name__)
    
    logger.info("Iniciando análise e validação dos dados.")
    
    valid_readings: List[Dict] = []
    erros:List[Dict] = []
 
    for index, line in enumerate(lines, start=1):
        
        if line.count('=') != 1:
            erros.append({
                "linha": index,
                "conteudo": line,
                "erro": "expected_single_equal"
            })
            
            continue
        
        chave, valor = line.split('=', 1)
        chave = chave.strip()
        valor = valor.strip()
        
        # chave vazia
        if not chave:
            erros.append({
                "linha": index,
                "conteudo": line,
                "erro": "empty_key"
            })
            continue
        
        # valor vazio
        if not valor:
            erros.append({
                "linha": index,
                "conteudo": line,
                "erro": "empty_value"
            })
            continue
        
        # conversão para float
        try:
            valor_float = float(valor)
        except ValueError:
            erros.append({
                "linha": index,
                "conteudo": line,
                "erro": "invalid_float_value"
            })
            continue
        
        valid_readings.append({
            "line": index,
            "sensor": chave,
            "value": valor_float
        })
        
        logger.info(f"Análise concluída. Leituras válidas: {len(valid_readings)}, Leituras inválidas: {len(erros)}")
        
    return valid_readings, erros