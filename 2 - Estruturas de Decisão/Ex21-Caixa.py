print('Quanto deseja sacar? Min R$10 Max R$ 600')
valor = float(input('Valor: '))

if valor < 10 and valor > 600:
    print('Valor não permitido!')
    exit()

centana = int(valor/100)
dezena = int((valor - (centana*100))/ 10)
unidade = int(valor - (dezena*10) - (centana*100))

print(centana, dezena, unidade)

if centana > 0:
    if centana == 1:
        print('{} cedula de R$ 100,00'.format(centana))
    else:
        print('{} cedulas de R$ 100,00'.format(centana))

if dezena > 0:
    if dezena >= 5:
        print('1 cedula de R$ 50,00'.format(dezena))
        dezena -= 5
        if dezena == 1:
            print('{} cedula de R$ 10,00'.format(dezena))
        elif dezena > 0:
            print('{} cedulas de R$ 10,00'.format(dezena))
    else:
        if dezena == 1:
            print('{} cedula de R$ 10,00'.format(dezena))
        elif dezena > 0:
            print('{} cedulas de R$ 10,00'.format(dezena))

if unidade > 0:
    if unidade >= 5:
        print('1 cedula de R$ 5,00'.format(unidade))
        unidade -= 5
        if unidade == 1:
            print('{} cedula de R$ 1,00'.format(unidade))
        elif unidade > 0:
            print('{} cedulas de R$ 1,00'.format(unidade))
    else:
        if unidade == 1:
            print('{} cedula de R$ 10,00'.format(unidade))
        elif unidade > 0:
            print('{} cedulas de R$ 10,00'.format(unidade))