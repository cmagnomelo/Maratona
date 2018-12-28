lado1 = float(input('Informe a medida do lado 1: '))
lado2 = float(input('Informe a medida do lado 2: '))
lado3 = float(input('Informe a medida do lado 3: '))

if (lado1 + lado2) > lado3 or (lado1 + lado3) > lado2 or (lado2 + lado3) > lado1:
    if(lado1 == lado2 and lado2 == lado3):
        print('É um triangulo Equilátero')
    elif(lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3):
        print('É um triangulo Isósceles')
    else:
        print('É um triangulo Escaleno')
else:
    print('Não é um triangulo')
