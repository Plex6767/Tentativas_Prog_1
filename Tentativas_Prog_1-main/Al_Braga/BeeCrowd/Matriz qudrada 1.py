while True:
    N = int(input())
    if N == 0:
        break
    for i in range(N):
        linha = []
        for j in range(N):
            dist_topo= i
            dist_esquerda= j
            dist_fundo=(N-1) - i
            dist_direita=(N-1) - j
            valor = (
                min(dist_topo, dist_esquerda, dist_direita, dist_fundo) + 1
            )
            linha.append(f"{valor:3d}")
        print(" ".join(linha))