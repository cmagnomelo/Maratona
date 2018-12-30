print('Responda as peguntas abaixo com \'S\' para SIM e \'N\' para NÃO')
contador = 0
respota = None

respota = input('Telefonou para a vítima?')
if respota == 'S' or respota == 's':
    contador += 1

respota = input('Esteve no local do crime?')
if respota == 'S' or respota == 's':
    contador += 1

respota = input('Mora perto da vítima?')
if respota == 'S' or respota == 's':
    contador += 1

respota = input('Devia para a vítima?')
if respota == 'S' or respota == 's':
    contador += 1

respota = input('Já trabalhou coma vítima?')
if respota == 'S' or respota == 's':
    contador += 1

if(contador > 0 and contador <= 2):
    print('Suspeito')
elif(contador > 2 and contador <= 4):
    print('Cúmplice')
elif(contador == 5):
    print('Assassino')
else:
    print('Inocente')