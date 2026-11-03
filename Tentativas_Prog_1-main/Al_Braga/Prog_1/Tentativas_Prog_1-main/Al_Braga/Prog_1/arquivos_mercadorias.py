arquivo = open('Mercadorias.txt', 'r')

linhas = arquivo.readlines()

for i in range(len(linhas)):
    print(f"{i}:{linhas[i]}")
    