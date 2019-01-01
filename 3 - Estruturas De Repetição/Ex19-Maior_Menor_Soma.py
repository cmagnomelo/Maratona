condicao = True
conjunto = []

while condicao:
    numero = int(input('Digite o numero desejado entre 0 e 1000: '))
    while numero < 0 or numero > 1000:
        print('Numero invalido')
        numero = int(input('Digite o numero desejado entre 0 e 1000: '))

    conjunto.append(numero)
    opcao = input('Deseja continuar inserindo numeros no conjunto? S - SIM N - Não: ')
    if opcao == 'N' or opcao == 'n':
        condicao = False

maior = conjunto[0]
menor = conjunto[0]
soma = 0

for i in conjunto:
    if i > maior:
        maior = i

    if i < menor:
        menor = i

    soma += i

print('Maior numero é', maior)
print('Menor numero é', menor)
print('A soma do conjunto é', soma)