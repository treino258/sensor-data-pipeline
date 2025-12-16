from src.sensor_pipeline.core.process import process_file
import pytest

def test_process_file_happy_path(tmp_path):
    content = """temp=25.0
ph=7.1
temp=26.5
"""

    file = tmp_path / "data.txt"
    file.write_text(content)

    result = process_file(str(file))

    assert result["temp"]["raw"] == [25.0, 26.5]
    assert result["ph"]["raw"] == [7.1]

def test_process_file_with_invalid_lines(tmp_path):
    content = """temp=20
invalid_line
ph=7
"""

    file = tmp_path / "data.txt"
    file.write_text(content)

    result = process_file(str(file))

    assert result["temp"]["raw"] == [20]
    assert result["ph"]["raw"] == [7]



def test_process_file_quality_error(tmp_path):
    content = """temp=10
invalid
invalid
invalid
"""

    file = tmp_path / "data.txt"
    file.write_text(content)

    result = process_file(str(file))

    # Como decidimos que o pipeline é tolerante:
    assert "temp" in result
    assert result["temp"]["raw"] == [10.0]

        
def test_process_file_empty(tmp_path):
    file = tmp_path / "empty.txt"
    file.write_text("")

    with pytest.raises(ValueError):
        process_file(str(file))
