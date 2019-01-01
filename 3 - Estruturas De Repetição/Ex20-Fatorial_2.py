print('Calcular Fatorial')
print('Regras:')
print('1 - Informe apenas numeros inteiros')
print('2 - Informe apenas numeros positivos')
print('3 - nforme apenas numeros menos que 16')

condicao = True

while condicao:
    numero = float(input('Informe o numero que deseja saber o fatorial: '))
    decimal = round(numero) - numero
    fatorial = 1

    while(decimal != 0) or (numero < 0) or (numero > 16):
        print('Numero inválido')
        numero = float(input('Informe o numero que deseja saber o fatorial: '))
        decimal = round(numero) - numero

    for i in range(int(numero), 1, -1):
        fatorial *= i

    print(fatorial)

    opcao = input('Deseja fazer outro calculo? S/N')
    if opcao == 'N' or opcao == 'n':
        condicao = False

