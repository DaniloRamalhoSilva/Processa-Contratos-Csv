import csv
import datetime
import re
import time
import sys

CPF_REGEX = re.compile(r"\d{3}\.\d{3}\.\d{3}-\d{2}")
RG_REGEX = re.compile(r"\d{2}\.\d{3}\.\d{3}-\d")

def parse_date(date_str):
    try:
        return datetime.datetime.strptime(date_str.strip(), "%d/%m/%Y").date()
    except ValueError:
        return None

def contrato_vigente(ini_contrato, fim_contrato, ini_periodo, fim_periodo):
    return ini_contrato <= fim_periodo and fim_contrato >= ini_periodo

def processar_csv(entrada, saida, ini_periodo_str, fim_periodo_str):
    ini_periodo = parse_date(ini_periodo_str)
    fim_periodo = parse_date(fim_periodo_str)
    if not ini_periodo or not fim_periodo:
        print("Período informado é inválido.")
        return

    total_lidos = 0
    total_filtrados = 0
    inicio_execucao = time.time()

    with open(entrada, mode='r', encoding='utf-8') as infile, \
         open(saida, mode='w', newline='', encoding='utf-8') as outfile:

        leitor = csv.reader(infile)
        escritor = csv.writer(outfile)
        escritor.writerow(["nome", "CPF", "RG", "endereco", "data_inicial", "data_final"])

        for linha in leitor:
            total_lidos += 1

            if len(linha) != 6:
                continue

            nome, cpf, rg, endereco, data_ini_str, data_fim_str = linha

            if not CPF_REGEX.fullmatch(cpf.strip()) or not RG_REGEX.fullmatch(rg.strip()):
                continue

            data_ini = parse_date(data_ini_str)
            data_fim = parse_date(data_fim_str)
            if not data_ini or not data_fim:
                continue

            if contrato_vigente(data_ini, data_fim, ini_periodo, fim_periodo):
                escritor.writerow(linha)
                total_filtrados += 1

    fim_execucao = time.time()
    print(f"Registros lidos: {total_lidos}")
    print(f"Registros filtrados: {total_filtrados}")
    print(f"Tempo de execução: {fim_execucao - inicio_execucao:.2f} segundos")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Uso: python script.py <entrada.csv> <saida.csv> <data_inicial> <data_final>")
        print("Exemplo: python script.py contratos.csv filtrados.csv 01/01/2025 31/12/2025")
    else:
        entrada, saida, data_ini, data_fim = sys.argv[1:5]
        processar_csv(entrada, saida, data_ini, data_fim)
