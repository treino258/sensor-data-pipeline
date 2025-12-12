from src.sensor_pipeline.core.normalize import normalize_readings


def test_normalize_basic():
    """
    testa a função normalize_readings para garantir que as leituras sejam corretamente normalizadas por sensor.
    
    returns:
        None    
        
    args:
        None
        
    """
    
    data = [
        {"sensor": "s1", "value": 25.0},
        {"sensor": "s2", "value": 30.5},
     ]
    
    norm = normalize_readings(data)
    
    assert (norm) == {
        "s1": [25.0],
        "s2": [30.5]
    }
    
def test_normalize_duplicate_data():
    """
    testa a função normalize_readings para garantir que múltiplas leituras do mesmo sensor sejam acumuladas corretamente.
    
    returns:
        None    
        
    args:
        None
        
    """
    
    data = [
        {"sensor": "s1", "value": 25.0},
        {"sensor": "s1", "value": 26.5},
        {"sensor": "s2", "value": 30.5},
        {"sensor": "s2", "value": 31.0},
     ]
    
    norm = normalize_readings(data)
    
    assert (norm) == {
        "s1": [25.0, 26.5],
        "s2": [30.5, 31.0]
    }
    
    def test_normalize_mixed_data():
        """
        testa a função normalize_readings para garantir que leituras de múltiplos sensores sejam normalizadas corretamente.
        
        returns:
            None    
            
        args:
            None
            
        """
        
        data = [
            {"sensor": "temp", "value": 25.0},
            {"sensor": "ph", "value": 7.5},
            {"sensor": "temp", "value": 26.5},
         ]
        
        norm = normalize_readings(data)
        
        assert (norm) == {
            "temp": [25.0, 26.5],
            "ph": [7.5],
        }