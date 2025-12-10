from core.clean import clean_lines

def test_clean_lines():
    """
    Testa a função clean_lines para garantir que linhas vazias e espaços excedentes sejam removidos corretamente.
    
    returns:
        None    
        
    args:
        None
    
    """
    
    raw = [" temp=10 ", "", "", "   ", "ph=7.1", "ok=20", " s@ns$or=10"]  
    cleaned = clean_lines(raw)
    
    assert cleaned == ["temp=10", "ph=7.1", "ok=20", "s@ns$or=10"]
    