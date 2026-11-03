operator = input( 'Qual operacao deseja utilizar? (+ , - , * , /) ou (s) para sair ')
num_1 = float(input('Escreva o primeiro numero:'))
num_2 = float(input('Escreva o segundo numero:'))

while 's':
    if operator == '+':
        result = num_1 + num_2
        print(round(result, 3))
        break
    elif operator == '-':
        result = num_1 - num_2
        print(round(result, 3))
        break

    elif operator == '*':
        result = num_1 * num_2
        print(round(result, 3))
        break
    elif operator == '/':
        result = num_1 / num_2
        print(round(result, 3))
        break


