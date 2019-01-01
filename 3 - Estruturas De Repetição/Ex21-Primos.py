primo = int(input('Digite um numero inteiro: '))
contador = 0

for i in range(1,primo+1):
    if primo % i == 0:
        contador += 1

if contador == 2:
    print('É primo')
else:
    print('Não é primo')

