"""
Estação meteorológica: Niterói – RJ.
Ano dos dados: 2025.
Quantidade de registros: 8.760 linhas.
Quantidade de colunas: 19.
Cada linha representa uma hora de um dia.

"""

#Abrindo e lendo o arquivo como texto puro
with open("dados.csv", "r") as file:
    #recebe todo o código em uma única string
    conteudo = file.read()

#Uso da função splitlines para quebrar o arquivo em linhas
linhas = conteudo.splitlines()

#Para evitar que haja separação de títulos como "TOTAL" e "HORARIO"
linha_limpa = linhas[8].replace('"', '').replace(', ', ' - ')
titulos = linha_limpa.split(",")

#Criação do dicionário principal para os títulos
dicionario_principal = {}
for titulo in titulos:
    # Criação de uma lista vazia para cada título
    dicionario_principal[titulo] = []

#A partir da linha 9 que os dados começam
for linha in linhas[9:]:

    #A função split serve para transformar o texto longo de cada linha em uma lista de valores
    valores = linha.split(',')

    #Verificação para garantir que processe os dados caso a linha tenha a mesma quantidade de colunas que os títulos
    if len(valores) == len(titulos):

        #Laço de 0 até o fim das colunas
        for i in range(len(titulos)):
            #Uso do título e o valor da posição "i"
            chave_atual = titulos[i]
            dado_atual = valores[i]

            #Guardamos na lista dentro do dicionário
            dicionario_principal[chave_atual].append(dado_atual)

#Uso de uma lista de todos os títulos
todas_as_colunas = list(dicionario_principal.keys())

#Montando o cabeçalho alinhado
cabecalho = ""
for coluna in todas_as_colunas:
    cabecalho += f"{coluna[:15]:<17} | "

print(cabecalho)
print("-" * len(cabecalho))

#Descobrindo o total de linhas do arquivo lido
total_linhas = len(dicionario_principal[todas_as_colunas[0]])

#Imprimindo as 10 primeiras linhas de Janeiro
for i in range(10):
    linha_formatada = ""
    for coluna in todas_as_colunas:
        dado = dicionario_principal[coluna][i]
        linha_formatada += f"{dado[:15]:<17} | "
    print(linha_formatada)


print(f'Foram {total_linhas} linhas salvas!')