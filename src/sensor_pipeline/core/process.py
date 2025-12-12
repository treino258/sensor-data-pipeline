from typing import List, Dict
from uuid import uuid4
from sensor_pipeline.logger import get_logger
from sensor_pipeline.core.load import load_file
from sensor_pipeline.core.clean import clean_lines
from sensor_pipeline.core.parse import parse_lines_data
from sensor_pipeline.core.normalize import normalize_readings
from sensor_pipeline.context import correlation_id_ctx

logger = get_logger(__name__)


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
    correlation_id = uuid4().hex
    correlation_id_ctx.set(correlation_id)
    logger.info(f"Iniciando o processamento do arquivo: {path}")
    
    try:
        logger.info("Carregando o arquivo.")
        # Carregar o arquivo
        dataset_load = load_file(path)
        logger.info(f"Arquivo carregado. Total de linhas: {len(dataset_load)}")
    except Exception as e:
        logger.error(f"Falha ao carregar o arquivo", exc_info=True)
        raise
    
    try:
        # Limpar linhas
        logger.info("Limpando as linhas do arquivo.")
        dataset_clean = clean_lines(dataset_load)
        logger.info(f"Linhas limpas. Total de linhas após limpeza: {len(dataset_clean)}")
    except Exception as e:
        logger.error(f"Falha ao limpar as linhas do arquivo", exc_info=True)
        raise
    
    try:
        logger.info("Analisando e validando os dados.")
        # Analisar e validar dados
        valid_readings, invalid_readings = parse_lines_data(dataset_clean)
        if invalid_readings:
            logger.warning(f"Foram encontradas {len(invalid_readings)} leituras inválidas durante a análise.")
        logger.info(f"Análise concluída. Leituras válidas: {len(valid_readings)}, Leituras inválidas: {len(invalid_readings)}")   
    except Exception as e:
        logger.error(f"Falha ao analisar os dados", exc_info=True)
        raise
        
    try:
        logger.info("Normalizando as leituras válidas.")
        # Normalizar leituras válidas
        normalized_data = normalize_readings(valid_readings)
        logger.info(f"Leituras normalizadas para {len(normalized_data)} sensores.")
    except Exception as e:
        logger.error(f"Falha ao normalizar os dados", exc_info=True)
        raise
    
    logger.info(f"Processamento concluído com sucesso.")
        
    return normalized_data