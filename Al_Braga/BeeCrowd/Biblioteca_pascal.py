while True:
    try:
        n_alunos, n_jantares = map(int, input().split())
        if n_alunos == 0 and n_jantares == 0:
             break

        # multiplicar a lista contendo 0 pelo n de alunos
        presencas_totais = [0] * n_alunos

        # lê a linha inteira do jantar e transforma em um contador de presença
        for a in range(n_jantares):
            presencas_jantar = list(map(int, input().split()))

            # percorre cada aluno vazio e soma a presença dele
            for i in range(n_alunos):
                presencas_totais[i] += presencas_jantar[i]

        if n_jantares in presencas_totais:
            print("yes")
        else:
            print("no")

    except EOFError:
        break