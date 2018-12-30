valido = True

while valido:
    numero = float(input('Informe uma nota: '))
    if numero < 0 or numero > 10:
        print('Nota informada é invalida.')
    else:
        valido = False
