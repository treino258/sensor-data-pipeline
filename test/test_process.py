from src.sensor_pipeline.core.process import process_file

def test_process_file_basic(tmp_path):
    """
    Cria um arquivo temporário e testa a função process_file para garantir que o arquivo seja processado corretamente.
    
    returns:
        None    
        
    args:
        tmp_path: caminho temporário para criar arquivos de teste.
        
    """
    
    # Criar um arquivo temporário com dados de teste
    test_file = tmp_path / "test_data.txt"
    test_file.write_text("temp=25.0\nph=7.1\ninvalid_line\n=something\nhumidity=55.5", encoding="utf-8")
    
    # Processar o arquivo
    result = process_file(str(test_file))
    
    # Verificar o resultado
    assert result == {
        "temp": [25.0],
        "ph": [7.1],
        "humidity": [55.5]
    }