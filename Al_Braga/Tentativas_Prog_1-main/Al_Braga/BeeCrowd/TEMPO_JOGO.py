incio, fim = map(int, input().split())

duracao = fim - incio

if duracao <= 0: 
    duracao += 24

print (f"O JOGO DUROU {duracao} HORAS)")
