from script import processar_csv

processar_csv(
    entrada='contratos.csv',
    saida='contratos_filtrados.csv',
    ini_periodo_str='01/01/2025',
    fim_periodo_str='31/12/2025'
)