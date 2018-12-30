numero = float(input('Digite um numero: '))
decimal = round(numero) - numero

if(decimal != 0):
    print('O valor digitado foi um numero real.')
else:
    print('O valor digitado foi um numero inteiro')