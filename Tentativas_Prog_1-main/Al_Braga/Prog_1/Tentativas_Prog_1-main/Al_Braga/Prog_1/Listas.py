"""
================================
    LISTAS
================================
.append =  adciona um elemento no fim da lista
.insert = adiciona um elemento na posicao de sua escolha
del lista [i] = remove por posicao
lanche.pop[i] = remove por posicao
lista.remove('i') = remove por indice
if ('i') in lista = verifica o indice
list(range(4,11) - uma lista de 4 a 10
lista.sort() = ordena a lista
len(lista) = cardinalidade
"""

"""
num = [2, 3, 4, 5, 6, 7, 8, 9, 10]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 4)
num.remove(2)
print(num)
print(len(num))
"""

"""

valores = []
for cont in range(0, 5):
    valores.append(int(input("Digite um valor: ")))
"""

"""

for v in valores:
    print(f"{v}... ", end="")
"""

"""

for c, v in enumerate(valores):
    print(f"Na posicao {c}: {v}")
print("Fim")
"""

"""

a = [2, 3, 4, 5, 6, 7, 8, 9, 10]
b =  a[:]
b[2] = 3
print(f'Lista A: {a}')
print(f'Lista B: {b}')
"""

"""

teste = list()
teste.append(5)
teste.append(6)
galera = list()
galera.append(teste[:])
teste[0] = 'lula'
teste[1] = 13
galera.append(teste[:])
print(galera)
"""

"""

galera = [['joao', 19], ['lula', 13], ['flavio', 22], ['renan', 14]]
for p in galera:
    print(f'{p[0]} tem seu numero {p[1]}')
"""

"""

galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 2):
    dado.append(str(input("Digite um nome: ")))
    dado.append(int(input("Digite outro numero: ")))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f' O {p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'O {p[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmai} maiores de idade e temos {totmen} menores de idade')
"""



