maior = None
for i in range(5):
    numero = float(input('Digite o numero desejado: '))

    if maior == None:
        maior = numero
        
    if numero > maior:
        maior = numero

print('O maior numero digitado foi: ', maior)