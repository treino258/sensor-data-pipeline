📡 Sensor Data Processing Pipeline
✨ Pipeline profissional com arquitetura limpa, testes unitários e processamento determinístico.

Este projeto implementa um pipeline completo para leitura, limpeza, validação e normalização de dados de sensores — seguindo padrões profissionais de Engenharia de Software e MLOps.

Ele foi construído com foco em:

modularidade

testabilidade

previsibilidade

logging estruturado

arquitetura limpa

separação rígida de responsabilidades

🚀 Arquitetura do Pipeline

O sistema segue 4 etapas independentes:

1. load_file → leitura do arquivo bruto

valida existência

valida tamanho

usa encoding correto

não modifica nada

retorna apenas as linhas

2. clean_lines → limpeza determinística

remove linhas vazias

remove ruídos simples

preserva ordem

função pura

3. parse_lines_data → validação sintática

Valida cada linha garantindo:

exatamente 1 "="

chave não vazia

valor não vazio

valor convertível para float

padrão correto “chave=valor”

Retorna:

valid_readings

errors com códigos como:

expected_single_equal

empty_key

empty_value

invalid_float_value

4. normalize_readings → agregação por sensor

Transforma:

{"sensor": "temp", "value": 23.1}
{"sensor": "temp", "value": 23.3}
{"sensor": "ph", "value": 7.1}


em:

{
    "temp": [23.1, 23.3],
    "ph": [7.1]
}

🧪 Testes Unitários (pytest)

A suíte de testes cobre:

limpeza

parsing

normalização

pipeline completo (process_file)

Para rodar:

pytest -q

📦 Instalação
pip install -r requirements.txt

▶️ Como executar
from core.process import process_file

result = process_file("sample_data/sensor.txt")
print(result)

🔍 Exemplo de saída
{
  "temp": [23.4],
  "hum": [55.0],
  "ph": [6.8]
}

🧠 Por que este projeto importa?

Este pipeline demonstra:

engenharia real

modularização profissional

testes confiáveis

previsibilidade nas etapas

logging orientado a produção

habilidade de manter e escalar código

Este é o tipo de qualidade que empresas como NVIDIA, J&J e startups de IA buscam em estágios técnicos.

✨ Autor

Vitor Albuquerque
Futuro GenAI Engineer • NeuroIA • MLOps • Python Engineer