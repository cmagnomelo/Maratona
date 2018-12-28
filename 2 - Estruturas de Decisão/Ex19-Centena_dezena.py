numero = int(input('Digite um numero menor que 1000: '))
centena = 0
dezena = 0
unidade = 0

print(numero,'=', end=' ')

if(numero > 100):
    centena = int(numero/100)
    dezena = int((numero - (centena*100))/10)
    unidade = numero - (centena * 100) - (dezena * 10)
else:
    dezena = int(numero/10)
    if(dezena > 0):
        unidade = numero - (centena * 100) - (dezena*10)
    else:
        unidade = numero - (centena*100)

if(centena == 0):
    print('', end=' ')
elif(centena == 1):
    print(centena, 'centena,', end=' ')
else:
    print(centena, 'centenas,', end=' ')

if(dezena == 0):
    print('e', end=' ')
elif(dezena == 1):
    print(dezena, 'dezena e', end=' ')
else:
    print(dezena, 'dezenas e', end=' ')

if(unidade == 0):
    print('', end=' ')
elif(unidade == 1):
    print(unidade, 'unidade')
else:
    print(unidade, 'unidades')


