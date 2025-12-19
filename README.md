# 📡 Sensor Data Processing Pipeline
### Pipeline de processamento de dados de sensores, projetado com foco em **engenharia**, **qualidade de dados**, **observabilidade** e **testabilidade**, simulando cenários reais de ingestão imperfeita.  
![status](https://img.shields.io/badge/status-stable-brightgreen)  ![python](https://img.shields.io/badge/python-3.10%2B-blue)
 
![tests](https://img.shields.io/badge/tests-pytest-blue) ![license](https://img.shields.io/badge/license-MIT-lightgrey)
  
![build](https://github.com/treino258/sensor-data-pipeline/actions/workflows/tests.yml/badge.svg)


## 🧠 Visão Geral
Este projeto implementa um pipeline que processa leituras de sensores a partir de arquivos de texto no formato:

```
sensor=value
```

Exemplo:

```
sensor1=10
sensor2=20
sensor1=15
sensor3=9.5
```

O pipeline é **tolerante a falhas**, **auditável** e **configurável por sensor**, permitindo que dados inválidos sejam analisados sem interromper toda a execução.

---

## 🧱 Arquitetura do Pipeline

Fluxo lógico do processamento:

```
File → Clean → Parse → Validate Quality → Metrics → Normalize
```

---

## 1️⃣ Load
Responsável por carregar o arquivo do disco.
- Falha crítica: arquivo inexistente ou inacessível
- Interrompe o pipeline em caso de erro

---

## 2️⃣ Clean
Responsável por:
- Remover linhas vazias
- Normalizar espaços
- Garantir formato básico

Não valida conteúdo semântico.

---

## 3️⃣ Parse

Responsabilidade:
- Interpretar linhas no padrão `chave=valor`
- Classificar leituras em **válidas** e **inválidas**
- Agrupar por sensor
- Nunca interrompe o pipeline

Formato de saída:

```python
{
  "sensor": {
    "valid": [float],
    "invalid": [dict]
  }
}
```

Leituras inválidas são preservadas para:
- auditoria
- métricas
- análise de qualidade

Linhas sem sensor identificável são agrupadas como `UNKNOWN`.

---

## 4️⃣ Validação de Qualidade

Responsável por avaliar a qualidade dos dados **por sensor**, utilizando limites configuráveis.

Exemplo de configuração:

```python
SENSOR_THRESHOLDS = {
    "sensor1": {"max_invalid_ratio": 0.1},
    "sensor2": {"max_invalid_ratio": 0.2},
    "DEFAULT": {"max_invalid_ratio": 0.3},
}
```

Regras:
- Sensores usam thresholds específicos quando disponíveis
- Caso contrário, utilizam `DEFAULT`
- Sensor `UNKNOWN` não quebra o pipeline
- Pipeline só falha quando a qualidade ultrapassa limites críticos

---

## 5️⃣ Métricas

Responsabilidade:
- Observar o estado do pipeline
- Gerar indicadores
- Não transformar dados

Exemplos:
- Total de sensores
- Total de leituras
- Taxa de invalidez

---

## 6️⃣ Normalização

Responsável por:
- Normalizar valores válidos
- Preservar valores crus
- Garantir rastreabilidade

Formato de saída:

```python
{
  "sensor": {
    "raw": [...],
    "normalized": [...]
  }
}
```

Essa decisão permite:
- auditoria
- reprocessamento
- debug avançado

---

## 📊 Observabilidade e Logging

- Logs estruturados em JSON
- Uso de `correlation_id` via `contextvars`
- Todos os logs de uma execução podem ser correlacionados

Formato:

```json
{
  "timestamp": "...",
  "level": "INFO",
  "module": "...",
  "message": "...",
  "correlation_id": "..."
}
```

Decisões:
- Um único stream de logs
- Segmentação via `logger.name`, `level` e `correlation_id`
- Compatível com ELK / Datadog / CloudWatch

---

## 🧪 Testes

Os testes validam **comportamento**, não implementação.

Cobertura:
- parsing
- tolerância a falhas
- qualidade de dados
- normalização
- pipeline completo

---

## ⚠️ Limitações Conhecidas

- Não persiste saída
- Input apenas via arquivo texto
- Thresholds simples
- Sem paralelismo

Limitações são intencionais.

---

## 🚀 Possíveis Evoluções

- Persistência (CSV, Parquet, DB)
- Streaming (Kafka)
- Observabilidade com OpenTelemetry
- Validações estatísticas avançadas
- Novos formatos de entrada

---

## 🧠 Filosofia

Este projeto prioriza:
- Clareza de responsabilidades
- Contratos explícitos
- Tolerância a falhas
- Decisões técnicas justificadas

Não foi feito para ser simples, mas para ser correto.


## ✨ Autor
**Vitor Albuquerque**  
Futuro GenAI Engineer • NeuroIA • MLOps • Edge AI • Python Software Engineer  
GitHub: https://github.com/treino258  
