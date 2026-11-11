lista = [64, -12, 42, 8, 99, -5, 0, 15, 23, 77, -45, 12, 3, 88, 51, -1, 30, 9, 100, -18, 55, 14, 27, 4, -33, 62, 7, 81,
         19, -8, 40, 92, 11, 35, 2]


def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        trocou = False
        for elemento in range(0, n - 1 - i):
            if lista[elemento] > lista[elemento + 1]:
                lista[elemento], lista[elemento + 1] = lista[elemento + 1], lista[elemento]
                trocou = True
        if not trocou:
            break

def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == alvo:
            return meio

        elif lista[meio] > alvo:
            fim = meio - 1

        else:
            inicio = meio + 1

    return -1

bubble_sort(lista)
print("Lista ordenada:", lista)

alvo = 77
posicao = busca_binaria(lista, alvo)

if posicao != -1:
    print(f"O número {alvo} foi encontrado no índice {posicao}.")
else:
    print(f"O número {alvo} não está na lista.")