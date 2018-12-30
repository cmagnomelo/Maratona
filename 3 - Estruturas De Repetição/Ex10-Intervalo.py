numero1 = int(input('Informe primeiro numero inteiro: '))
numero2 = int(input('Informe segundo numero inteiro: '))

for i in range(numero1, numero2 + 1):
        print(i, end=' ')

for i in range(numero1, numero2 - 1, -1):
        print(i, end=' ')

print('END')