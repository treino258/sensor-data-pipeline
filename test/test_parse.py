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
    parsed = parse_lines_data(lines)
    
    
    
    assert "temp" in parsed
    assert parsed["temp"]["valid"] == [25.0]
    assert parsed["temp"]["invalid"] == []

def test_parse_invalid_no_equal():
    """
    Testa a função parse_lines_data para garantir que linhas sem '=' sejam identificadas como inválidas.
    
    returns:
        None
        
    args:
        None
    """
    
    lines = ["temp25"]
    parsed = parse_lines_data(lines)
    
    assert "UNKNOWN" in parsed
    assert len(parsed["UNKNOWN"]["invalid"]) == 1
    assert parsed["UNKNOWN"]["invalid"][0]["erro"] == "expected_single_equal_sign"
 


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
    
    parsed = parse_lines_data(lines)
    
    assert parsed["temp"]["valid"] == [20.0]
    assert parsed["ph"]["valid"] == [7.1]

    total_invalid = sum(
        len(sensor["invalid"]) for sensor in parsed.values()
    )

    assert total_invalid == 4
    
    
    
         
    