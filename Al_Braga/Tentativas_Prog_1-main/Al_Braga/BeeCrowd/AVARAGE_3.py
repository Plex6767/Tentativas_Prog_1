"""
Leia quatro números (N1, N2, N3, N4), qual aquele com 1 algarismo após a vírgula,
 correspondente a 4 notas obtidas por um aluno. Calcule a média com pesos 2, 3, 4 e 1
  respectivamente, para esses 4 escores e imprima a mensagem "Mídia:" (Média), seguido do
  resultado calculado. Se a média foi de 7,0 ou mais, imprima a mensagem "Aluno aprovado."
   (Aluno Aprovado). Se a média foi inferior a 5,0, imprima a mensagem: "Aluno reprovado." (Aluno Reprovado)
   . Se a média ficou entre 5,0 e 6,9, incluindo estes, o programa deve imprimir a mensagem "Aluno em exame".
    (Em estudante de provas).

Em caso de exame, leia mais uma nota. Imprimir a mensagem "Nota do exame:" (Escore do exame)
 seguido da pontuação digitada. Recalcular a média (somar a nota do exame com a média calculada
 anterior e dividir por 2) e imprimir a mensagem “Aluno aprovado.” (Aluno aprovado) em caso de média 5,0 ou mais)
  ou "Aluno reprovado." (Aluno reprovado) em caso de média 4,9 ou menos. Para esses 2 casos
  (aprovados ou reprovados após o exame) imprima a mensagem "Final da mídia:" (Média final) seguida
  da média final para este aluno da última linha.

Entrada
A entrada contém quatro números de ponto flutuante que representam as notas dos alunos.

Saída
Imprima todas as respostas com um dígito após a vírgula.
"""
N1, N2, N3, N4 = map(float, input().split())

M = (N1 * 2 + N2 * 3 + N3 * 4 + N4 * 1) / 10.0

print(f"Media: {M:.1f}")
if M >= 7.0:
    print("Aluno aprovado.")
elif M < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    NE = float(input())
    print(f"Nota do exame: {NE:.1f}")
    M_final = (M + NE) / 2.0

    if M >= 5.0:
        print("Aluno aprovado.")
        print(f"Media final: {M_final:.1f}")
    else:
        print("Aluno reprovado.")
