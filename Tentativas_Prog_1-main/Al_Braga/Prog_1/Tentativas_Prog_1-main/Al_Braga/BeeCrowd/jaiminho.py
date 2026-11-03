# Quantidade de casos de teste
qt = int(input())

for _ in range(qt):
    # Lê a quantidade de dias
    n = int(input())

    # Guarda o total em minutos
    saldo_total = 0

    for _ in range(n):
        # Lê a linha completa '07:55 12:03 | 13:54 18:02'
        linha = input()

        # Remove a barra e transforma os 4 horários em uma lista
        horarios = linha.replace("|", "").split()

        # Conversão de horários para minutos
        h, m = map(int, horarios[0].split(":"))
        e1 = h * 60 + m

        h, m = map(int, horarios[1].split(":"))
        s1 = h * 60 + m

        h, m = map(int, horarios[2].split(":"))
        e2 = h * 60 + m

        h, m = map(int, horarios[3].split(":"))
        s2 = h * 60 + m

        # 1) Primeira Entrada (esperado: 08:00 = 480 min)
        diferenca_e1 = 480 - e1
        if abs(diferenca_e1) > 5:
            saldo_total += diferenca_e1

        # 2) Primeira Saída (esperado: 12:00 = 720 min)
        diferenca_s1 = s1 - 720
        if abs(diferenca_s1) > 5:
            saldo_total += diferenca_s1

        # 3) Segunda Entrada (esperado: 14:00 = 840 min)
        diferenca_e2 = 840 - e2
        if abs(diferenca_e2) > 5:
            saldo_total += diferenca_e2

        # 4) Segunda Saída (esperado: 18:00 = 1080 min)
        diferenca_s2 = s2 - 1080
        if abs(diferenca_s2) > 5:
            saldo_total += diferenca_s2

    # Decidir o sinal do resultado (fora do loop dos dias!)
    sinal = "+" if saldo_total >= 0 else "-"

    # Converter o total acumulado em minutos em horas e minutos
    saldo_abs = abs(saldo_total)
    horas = saldo_abs // 60
    minutos = saldo_abs % 60

    print(f"{sinal} {horas:02d}:{minutos:02d}")