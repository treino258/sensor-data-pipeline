from src.sensor_pipeline.core.parse import parse_lines_data

def test_parse_valid_lines():
    """
    Testa a função parse_lines_data para garantir que linhas válidas e inválidas sejam corretamente identificadas.
    
    returns:
        None    
        
    args:
        None
    
    """
    lines = ["temp=25.0"]
    valid, errors = parse_lines_data(lines)
    
    
    
    assert len(valid) == 1
    assert valid[0]["sensor"] == "temp"
    assert valid[0]["value"] == 25.0
    assert len(errors) == 0

def test_parse_invalid_no_equal():
    """
    Testa a função parse_lines_data para garantir que linhas sem '=' sejam identificadas como inválidas.
    
    returns:
        None
        
    args:
        None
    """
    
    lines = ["temp25"]
    valid, errors = parse_lines_data(lines)
    
    assert len(valid) == 0
    assert len(errors) == 1
    assert errors[0]["erro"] == "expected_single_equal"
 
"""
def test_parse_invalid_empty_key():
    
    Testa a função parse_lines_data para garantir que linhas com chave vazia sejam identificadas como inválidas.
    
    returns:
        None
        
    args:
        None
    
    
    lines = ["=25.0"]
    valid, errors = parse_lines_data(lines)
    
    assert len(valid) == 0
    assert len(errors) == 1
    assert errors[0]["erro"] == "empty_key"
"""
"""
def test_parse_invalid_float_value():
    
    Testa a função parse_lines_data para garantir que linhas com valor não convertível para float sejam identificadas como inválidas.
    
    returns:
        None
        
    args:
        None
    
    lines = ["temp=abc"]
    valid, errors = parse_lines_data(lines)
    
    assert len(valid) == 0
    assert len(errors) == 1
    assert errors[0]["reason"] == "invalid_float_value"

    """

def test_parse_mixed_lines():
    """
    Testa a função parse_lines_data para garantir que uma mistura de linhas válidas e inválidas seja processada corretamente.
    
    returns:
        None
        
    args:
        None
    """
    lines = [
        "temp=20",
        "x=",
        "invalid line",
        "ph=7.1",
        "=10",
        "y=abc"
    ]
    
    valid, errors = parse_lines_data(lines)
    
    assert len(valid) == 2
    assert len(errors) == 4
    
    
    
         
    