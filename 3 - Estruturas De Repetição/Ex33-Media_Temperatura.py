temperaturas = []
condicao = True

while condicao:
    temperatura = float(input('Informe a temperatura: '))
    temperaturas.append(temperatura)
    op = input('Deseja continuar(S/N): ')
    if op == 'N' or op == 'n':
        condicao = False

maior = temperaturas[0]
menor = temperaturas[0]
total = 0

for i in range(len(temperaturas)):
    if temperaturas[i] > maior:
        maior = temperaturas[i]

    if temperaturas[i] < menor:
        menor = temperaturas[i]

    total += temperaturas[i]

print('Maior temperatura é: ', maior)
print('Menor temperatura é: ', menor)
print('Temperatura média foi:', total / len(temperaturas))
