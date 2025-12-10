# 📡 Sensor Data Processing Pipeline
### Pipeline profissional para leitura, limpeza, validação e normalização de dados de sensores  
![status](https://img.shields.io/badge/status-stable-brightgreen)  ![python](https://img.shields.io/badge/python-3.10%2B-blue)
 
![tests](https://img.shields.io/badge/tests-pytest-blue) ![license](https://img.shields.io/badge/license-MIT-lightgrey)
  
![build](https://github.com/treino258/sensor-data-pipeline/actions/workflows/tests.yml/badge.svg)


## 🧠 Visão Geral
Este projeto implementa um pipeline completo, modular e profissional para processamento de dados de sensores.

Ele segue padrões reais de engenharia usados em MLOps, Sistemas de telemetria, Edge AI, Observabilidade e pré-processamento para ML.

O sistema recebe leituras brutas e passa por 4 estágios:
1. Carregamento do arquivo  
2. Limpeza  
3. Parsing e validação  
4. Normalização

---

## ⚙️ Arquitetura
```
core/
│── load.py
│── clean.py
│── parse.py
│── normalize.py
│── process.py
tests/
│── test_clean.py
│── test_parse.py
│── test_normalize.py
│── test_process.py
sample_data/
│── sensor.txt
```

---

## 🔍 Etapas do Pipeline

### 1️⃣ load_file — Leitura segura  
- valida existência  
- valida arquivo vazio  
- abre em UTF-8  
- não altera conteúdo  

### 2️⃣ clean_lines — Limpeza determinística  
- remove espaços  
- remove linhas vazias  
- preserva ordem  

### 3️⃣ parse_lines_data — Validação sintática  
Valida:
- 1 "="  
- chave não vazia  
- valor não vazio  
- float válido  
- formato chave=valor  

Retorna `valid_readings` e `errors`.

### 4️⃣ normalize_readings — Agregação por sensor  
Transforma:
```
temp=20
temp=25
ph=7.1
```
em:
```
{ "temp": [20,25], "ph": [7.1] }
```

---

## ▶️ Como Usar

### Instalar dependências:
```
pip install -r requirements.txt
```

### Executar:
```python
from core.process import process_file
result = process_file("sample_data/sensor.txt")
print(result)
```

---

## 🧪 Testes
Rodar todos os testes:
```
pytest -q
```

---

## 📊 Exemplo de Entrada
```
temp=23.4
hum=56
ph=6.8
erro invalido
temp=25.1
```

## 📈 Exemplo de Saída
```python
{
  "temp": [23.4, 25.1],
  "hum": [56.0],
  "ph": [6.8]
}
```

Erros:
```python
[
  {
    "linha": 4,
    "conteudo": "erro invalido",
    "reason": "expected_single_equal"
  }
]
```

---

## ✨ Autor
**Vitor Albuquerque**  
Futuro GenAI Engineer • NeuroIA • MLOps • Edge AI • Python Software Engineer  
GitHub: https://github.com/treino258  
