from typing import List, Dict
from uuid import uuid4
from sensor_pipeline.logger import get_logger
from sensor_pipeline.core.load import load_file
from sensor_pipeline.core.clean import clean_lines
from sensor_pipeline.core.parse import parse_lines_data
from sensor_pipeline.core.normalize import normalize_readings
from sensor_pipeline.context import correlation_id_ctx
from sensor_pipeline.valid_sensor_quality import validate_quality
from sensor_pipeline.metrics.pipeline_metrics import compute_metrics
from sensor_pipeline.utils.timing import measure_time


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
    
    logger.info(f"Iniciando o processamento do arquivo:", extra={"path": path})
    
    
    # Carregar o arquivo
    dataset_load = load_file(path)
    logger.info(f"Arquivo carregado. Total de linhas", extra={"lines": len(dataset_load)})
    
    
    

    # Limpar linhas
    dataset_clean = clean_lines(dataset_load)
    logger.info(f"Linhas limpas. Total de linhas após limpeza", extra={"lines": len(dataset_clean)})
    
    
    with measure_time() as elapsed:
        # Analisar e validar dados
        parsed_data = parse_lines_data(dataset_clean)
        
        validate_quality(parsed_data)
        
    logger.info("Parse e validação concluidos")
        
        
        
    metrics = compute_metrics(parsed_data)
    logger.info("Métricas computadas", extra={"metrics": metrics})
           
    
    # Normalizar leituras válidas
    normalized_data = normalize_readings(parsed_data)
    logger.info(f"Normalização concluida", extra={"sensores": len(normalized_data)})    

    
    logger.info(f"Processamento concluído com sucesso.")
        
    return normalized_data