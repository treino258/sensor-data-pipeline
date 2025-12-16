from src.sensor_pipeline.core.normalize import normalize_readings


def test_normalize_basic():
    """
    testa a função normalize_readings para garantir que as leituras sejam corretamente normalizadas por sensor.
    
    returns:
        None    
        
    args:
        None
        
    """
    
    data = {
        "sensor1": {"valid": [10, 20], "invalid": []},
        "sensor2": {"valid": [5], "invalid": []}
    }

    result = normalize_readings(data)

    assert result["sensor1"]["normalized"] == [0.0, 1.0]
    assert result["sensor1"]["raw"] == [10, 20]
    
