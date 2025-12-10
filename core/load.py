
from pathlib import Path
from typing import List, Tuple, Union
import logging

logger = logging.getLogger(__name__)

def load_file(file_path: str) -> List[str]:
    """
     Carrega um arquivo e retorna suas linhas sem modificar o conteúdo.
    
    Regras:
      - valida se o caminho existe (FileNotFoundError)
      - valida se o arquivo não está vazio (ValueError)
      - abre o arquivo com encoding utf-8
      - não imprime nada; em caso de erro levanta exceção adequada
      
    returns:
        list[str]: lista de linhas do arquivo.  
      
    arg:
        file_path: caminho para o arquivo de texto.
        

    raises:
        FileNotFoundError: se arquivo não existir.
        ValueError: se arquivo existir mas estiver vazio.
        RuntimeError: se ocorrer erro de I/O inesperado.
    
    """
    path = Path(file_path)
    
    # --- validação de existência ---
    
    if not path.exists():
        logger.error(f"Arquivo não encontrado: {path}")       
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")
    
    # --- validação de arquivo vazio ---
    
    try:
        if path.stat().st_size == 0:
            logger.error(f"Arquivo vazio: {path}")
            raise ValueError(f"Arquivo vazio: {path}")
    except OSError as e:
        logger.exception("Erro ao verificar tamanho do arquivo.")
        raise RuntimeError(f"Erro ao acessar arquivo '{path}': {e}") from e
    
     # --- leitura pura ---
    
    try:
        with path.open("r", encoding="utf-8") as f:
            
            lines = f.readlines()
            
        logger.info(f"Arquivo carregado com sucesso: {path}")
        
        return lines

    except OSError as e:
        logger.exception("Erro ao ler o arquivo.")
        raise RuntimeError(f"Erro ao ler arquivo '{path}': {e}") from e