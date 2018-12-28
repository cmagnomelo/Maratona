print('Equação do Segundo Grau: ax² + bx + c = 0')
a = float(input('Informe o valor de A: '))

if a == 0:
    print('Não é uma equação do segundo grau.')
    exit()

b = float(input('Informe o valor de B: '))
c = float(input('Informe o valor de C: '))

delta = (b**2) - (4 * a * c)
print(delta)
raiz = None

if delta == 0:
    raiz = ((-1)*b / (2 * a))
    print(raiz)
elif delta > 0:
    raiz = (((-1) * b + (delta ** (1 / 2))) / (2 * a))
    print('x\' é', raiz)
    raiz = (((-1) * b - (delta**(1/2))) / (2 * a))
    print('x\'\' é', raiz)
else:
    print('Não possui raiz real')