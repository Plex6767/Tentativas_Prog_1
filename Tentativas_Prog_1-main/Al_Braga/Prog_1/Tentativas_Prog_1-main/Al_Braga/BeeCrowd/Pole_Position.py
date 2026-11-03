import sys


def resolver():
    while True:
        # Lê a linha que contém o número de carros N
        linha = sys.stdin.readline().split()
        if not linha:
            break

        N = int(linha[0])

        # Critério de parada do Beecrowd (N = 0)
        if N == 0:
            break

        # Cria um grid de largada vazio com N posições (preenchido com zeros)
        grid = [0] * N
        valido = True

        # Lê a situação atual de cada um dos N carros
        for posicao_atual in range(1, N + 1):
            C, P = map(int, sys.stdin.readline().split())

            # Se já identificamos uma inconsistência anterior, apenas continua lendo as linhas restantes
            if not valido:
                continue

            # Calcula o índice correto na lista do Python (0 até N - 1)
            posicao_inicial_python = (posicao_atual - 1) - P

            # Verificação 1: A posição inicial fica dentro dos limites da pista (0 até N-1)?
            if 0 <= posicao_inicial_python < N:
                # Verificação 2: A posição inicial está vazia?
                if grid[posicao_inicial_python] == 0:
                    grid[posicao_inicial_python] = C
                else:
                    valido = False  # Conflito: dois carros no mesmo lugar
            else:
                valido = False  # Posição inválida fora dos limites da pista

        # Imprime o resultado do caso de teste
        if valido:
            # Transforma a lista [1, 2, 3, 4] na string "1 2 3 4" separada por espaços
            print(*(grid))
        else:
            print(-1)


if __name__ == '__main__':
    resolver()