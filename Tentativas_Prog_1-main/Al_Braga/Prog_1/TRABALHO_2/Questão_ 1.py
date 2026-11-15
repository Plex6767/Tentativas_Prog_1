# Questão 1. Leitura dos dados brutos.
#
# Você também deve preparar um script em Python que seja capaz de ler o
# arquivo com os dados meteorológicos e guardá-lo por completo na memória,
# usando uma lista (lista normal de Python ou numpy) para cada coluna do
# dado bruto. Estas listas devem ser organizadas em um único dicionário,
# usando como chave o título da coluna original da tabela de dados
# fornecida.

# Abrindo e lendo o arquivo como texto puro (utf-8 ajuda com a acentuação)
with open("dados.csv", "r", encoding="utf-8") as file:
    conteudo = file.read()

# Uso da função splitlines para quebrar o arquivo em linhas
linhas = conteudo.splitlines()

# Limpando aspas e vírgulas falsas do título, para depois separar pela vírgula verdadeira!
# Isso evita que textos como "PRECIPITAÇÃO, HORÁRIO" sejam quebrados ao meio.
linha_limpa = linhas[8].replace('"', '').replace(', ', ' - ')
titulos = linha_limpa.split(",")

# Criação do dicionário principal para os títulos
dicionario_principal = {}
for titulo in titulos:
    # Criação de uma lista vazia para cada título
    dicionario_principal[titulo] = []

# A partir da linha 9 que os dados começam
for linha in linhas[9:]:

    # A função split serve para transformar o texto longo de cada linha em uma lista de valores
    valores = linha.split(',')

    # Verificação para garantir que processe os dados caso a linha tenha a mesma quantidade de colunas que os títulos
    if len(valores) == len(titulos):

        # Laço de 0 até o fim das colunas
        for i in range(len(titulos)):
            # Uso do título e o valor da posição "i"
            chave_atual = titulos[i]
            dado_atual = valores[i]

            # Guardamos na lista correspondente dentro do dicionário
            dicionario_principal[chave_atual].append(dado_atual)

# ==========================================
# EXIBIÇÃO ALINHADA (Para ver se funcionou)
# ==========================================
print(f"{'DATA':<15} | {'HORA':<10} | {'TEMPERATURA (°C)'}")
print("-" * 50)

# Resgatando as listas específicas dentro do dicionário
lista_datas = dicionario_principal["Data"]
lista_horas = dicionario_principal["Hora UTC"]
# Atenção ao nome exato da chave após a nossa limpeza de vírgulas falsas:
lista_temps = dicionario_principal["TEMPERATURA DO AR - BULBO SECO - HORARIA (°C)"]

# Imprimindo apenas as 15 primeiras linhas de forma tabular
for i in range(15):
    print(f"{lista_datas[i]:<15} | {lista_horas[i]:<10} | {lista_temps[i]}")