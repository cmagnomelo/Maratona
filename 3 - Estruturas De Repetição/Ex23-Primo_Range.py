numero = int(input('Quantos numero primos temos de 1 a '))
divisao = 0


for i in range(1,numero + 1):
    contador = 0
    for y in range(1, i + 1):
        if i % y == 0:
            contador += 1

        divisao += 1

    if contador == 2:
        print(i,'é primo')
        contador = 0

print('Foram feitas',divisao,'divisões')