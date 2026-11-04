

mat = [1] * 3

for i in  range(len(mat)):
    mat[i] = [" "] * 3

n = 1
while True:
#        n_alunos, n_jantares = map(int, input().split())
    x, y  = map(int, input('Jogador O:').split())
    mat[x][y]="O"
    print(mat)
    n = n + 1

    x, y  = map(int, input('Jogador x:').split())
    mat[x][y]="X"
    print(mat)
    n = n + 1

    if not mat[0][0] == " ":
        if mat[0][0] == mat[0][1] and mat[0][0] == mat[0][2]:# -
            vencedor = mat[0][0]
            break
        if mat[0][0] == mat[1][1] and mat[2][2] == mat[2][2]:# \
            vencedor = mat[2][0]
            break
    if not mat[1][0] == " ":
        if mat[1][0] == mat[1][1] and mat[1][0] == mat[1][2]:# -
            vencedor = mat[1][0]
            break

        if mat[0][1] == mat[1][1] and mat[2][1] == mat[2][2]:  # |
            vencedor = mat[0][1]
            break
    if not mat[2][0] == " ":
        if mat[2][0] == mat[2][1] and mat[2][0] == mat[2][2]:# _
            vencedor = mat[2][0]
            break

        if mat[0][2] == mat[1][1] and mat[2][0] == mat[2][2]:# /
            vencedor = mat[0][2]
            break



    if n >= 9:
        print("Jogo Encerrado")
        print(f"{vencedor}")
        break

