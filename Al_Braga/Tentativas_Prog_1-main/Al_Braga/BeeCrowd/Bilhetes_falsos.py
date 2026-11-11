import sys


def resolver():
    while True:
        # Lê N e M
        linha = input().split()
        N = int(linha[0])
        M = int(linha[1])

        # Critério de parada
        if N == 0 and M == 0:
            break

        # Lê a lista de ingressos do pacote
        ingressos = list(map(int, input().split()))

        vistos = set()
        clones = set()

        # Processa cada ingresso
        for bilhete in ingressos:
            if bilhete in vistos:
                clones.add(bilhete)
            else:
                vistos.add(bilhete)

        # Imprime o resultado do caso de teste atual
        print(len(clones))


if __name__ == '__main__':
    resolver()