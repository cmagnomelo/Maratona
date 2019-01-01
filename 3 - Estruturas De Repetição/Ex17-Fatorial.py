numero = int(input('Informe o numero que deseja saber o fatorial: '))
fatorial = 1

for i in range(numero, 1, -1):
    fatorial *= i

print(fatorial)