numero1 = int(input('Informe primeiro numero inteiro: '))
numero2 = int(input('Informe segundo numero inteiro: '))
soma = 0

for i in range(numero1, numero2 + 1):
        soma += i

for i in range(numero1, numero2 - 1, -1):
    soma += i

print('A soma do intervalo é', soma)