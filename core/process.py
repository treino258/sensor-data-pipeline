from typing import List, Dict
import logging
from core.load import load_file
from core.clean import clean_lines
from core.parse import parse_lines_data
from core.normalize import normalize_readings

logger = logging.getLogger(__name__)

def process_file(path: str) -> Dict[str, List[float]]:
    """
    Processa o arquivo de leituras de sensores seguindo as etapas:
      - carregar o arquivo
      - limpar linhas
      - analisar e validar dados
      - normalizar leituras válidas
      
      returns:
          Dict[str, List[float]]: dicionário com leituras normalizadas por sensor.
          
          
      Args:
          path: caminho para o arquivo de texto.
        
      """
      
    
    # Carregar o arquivo
    dataset_load = load_file(path)
    
    # Limpar linhas
    dataset_clean = clean_lines(dataset_load)
    
    # Analisar e validar dados
    valid_readings, invalid_readings = parse_lines_data(dataset_clean)
    
    logger.info(f"Leituras inválidas: {len(invalid_readings)}")
    
    # Normalizar leituras válidas
    normalized_data = normalize_readings(valid_readings)
    
    logger.info("Processamento do arquivo concluído com sucesso.")
    
    return normalized_data