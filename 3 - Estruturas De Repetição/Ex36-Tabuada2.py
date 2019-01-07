condicao = True
while condicao:
    numero = int(input('Montar a tabuada de: '))
    comeco = int(input('Começar por: '))
    final = int(input('Final por: '))
    if final < comeco:
        print('Final deve ser maior que começo!!!')
        final = int(input('Final por: '))
    else:
        condicao = False


print('Vou mantar a tabuada de', numero,'começando em', comeco,'e terminando em',final,':')
for i in range(comeco,final+1):
    print(numero,'x',i,'=',numero * i)