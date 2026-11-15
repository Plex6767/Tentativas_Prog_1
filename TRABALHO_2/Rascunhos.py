"""
import csv
with open("dados.csv", "r") as file:
    csvreader = csv.reader(file)

    for row in csvreader:
        print(row[2])

f = open(dados.csv, "r")
lines = f.readlines()
result = []
for x in lines:
    result.append(x.split(' ')[1])
f.close()
print([x.split(' ')[1] for x in open(dados.csv).readlines()])


"""
# ==========================================
# QUESTÃO 1: Leitura dos dados brutos
# ==========================================

import csv

# 1. Abrindo o arquivo. O csv.reader lida corretamente com vírgulas
#    dentro de aspas ("PRECIPITAÇÃO TOTAL, HORÁRIO (mm)") e com \r\n.
with open("dados.csv", "r", encoding="utf-8", newline="") as file:
    linhas = list(csv.reader(file))

# 2. Os títulos estão na linha 9 (índice 8). O csv.reader já separou
#    as colunas respeitando as aspas, então cada item é um título.
titulos = linhas[8]

# 4. Criação do dicionário principal e inicialização das listas vazias
dicionario_principal = {}
for titulo in titulos:
    dicionario_principal[titulo] = []

# 4. Laço para percorrer os dados reais (que começam na linha 10, índice 9)
for valores in linhas[9:]:

    # Verificação de segurança: ignora linhas vazias ou com nº errado de colunas
    if len(valores) != len(titulos):
        continue

    # Laço de 0 até o total de colunas para guardar cada dado no seu lugar
    for i in range(len(titulos)):
        chave_atual = titulos[i]
        dado_atual = valores[i]

        # Adiciona o dado na lista correspondente dentro do dicionário
        dicionario_principal[chave_atual].append(dado_atual)


# ==========================================
# TESTE RÁPIDO PARA VER SE FUNCIONOU
# ==========================================
# Imprimindo apenas os títulos e os 3 primeiros valores da coluna "Data"
# (para não travar a sua tela com milhares de dados de uma vez)
print("Colunas encontradas:", list(dicionario_principal.keys()))
print("-" * 50)
print("Primeiras 3 datas da coluna 'Data':", dicionario_principal['Data'][:3])
print("Primeiras 3 horas da coluna 'Hora UTC':", dicionario_principal['Hora UTC'][:3])



