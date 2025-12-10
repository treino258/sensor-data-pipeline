from typing import List
import logging


def clean_lines(lines: List[str]) -> List[str]:
    """
    Remove linhas vazias e espaços excedentes, sem alterar o conteúdo dos dados.

    
    Returns:
        List[str]: lista de linhas limpas.
    
    Args:
        lines: lista de linhas a serem limpas.


    """
    logger = logging.getLogger(__name__)
    
    logger.info("Iniciando limpeza das linhas do arquivo.")
    
    cleaned_lines: List[str] = []

    for raw in lines:
        clean = raw.strip()
        if clean:
            cleaned_lines.append(clean)
    
    logger.info(f"Limpeza concluída. Linhas antes: {len(lines)}, Linhas depois: {len(cleaned_lines)}")

    return cleaned_lines