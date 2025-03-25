# 📄 Processador de Contratos CSV

Este projeto implementa uma solução eficiente para **processar grandes arquivos CSV** contendo dados de contratos, filtrando registros por **vigência em um período informado**, com **baixo consumo de memória**.

---

## ⚙️ Funcionalidades

- Leitura de arquivos CSV **em streaming** (sem carregar tudo na memória)
- Validação de **CPF**, **RG** e **datas**
- Verificação de **vigência de contratos** por sobreposição de datas
- Escrita de um novo CSV apenas com contratos válidos
- Geração de **métricas de performance** (tempo e contagem de registros)

---

## 📁 Exemplo de Entrada

```csv
nome,CPF,RG,endereco,data_inicial,data_final
João Silva,111.222.333-44,12.345.678-9,Rua A,01/01/2024,31/12/2024
Maria Souza,222.333.444-55,23.456.789-0,Av B,01/06/2024,31/05/2025
```

Se o período informado for `01/01/2025` a `31/12/2025`, apenas o contrato da Maria será incluído.

---

## 🚀 Como Usar

```python
from seu_script import processar_csv

processar_csv(
    entrada='contratos.csv',
    saida='contratos_filtrados.csv',
    ini_periodo_str='01/01/2025',
    fim_periodo_str='31/12/2025'
)
```

---

## 🧠 Otimizações Aplicadas

| Técnica                     | Descrição |
|----------------------------|-----------|
| **Leitura em streaming**   | Usa `csv.reader()` com `with open`, evitando sobrecarga de memória |
| **Validação antecipada**   | CPF/RG com `regex` e datas com `datetime.strptime` |
| **Filtro eficiente**       | Condição de overlap de datas simples e rápida: `ini_contrato <= fim_periodo and fim_contrato >= ini_periodo` |
| **Escrita incremental**    | `csv.writer()` grava linha por linha, sem manter buffer em memória |
| **Estatísticas integradas**| Usa `time.time()` e contadores para medir performance e total de registros |

---

## 📊 Saída Esperada no Console

```text
Registros lidos: 1000000
Registros filtrados: 54321
Tempo de execução: 12.87 segundos
```

---

## 🛠 Requisitos

- Python 3.7+
- Bibliotecas padrão: `csv`, `datetime`, `re`, `time`
