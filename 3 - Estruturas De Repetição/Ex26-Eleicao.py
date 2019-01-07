cadidato1 = 0
cadidato2 = 0
cadidato3 = 0

eleitores = int(input('Qual o número total de eleitores? '))

for i in range(1,eleitores+1):
    print('Eleitor numero {}'.format(i))
    print('Votação')
    print('1 - Cadidato 1')
    print('2 - Cadidato 2')
    print('3 - Cadidato 3')
    op = int(input('Em quem deseja vota? '))

    if op == 1:
        cadidato1 += 1
    elif op == 2:
        cadidato2 += 1
    elif op == 3:
        cadidato3 += 1
    else:
        print('Você anulou seu voto')

print('Cadidato 1 teve {} votos'.format(cadidato1))
print('Cadidato 2 teve {} votos'.format(cadidato2))
print('Cadidato 3 teve {} votos'.format(cadidato3))