n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
n3 = int(input('Terceiro numero: '))

aux = None

if n1 > n2 and n2 > n3:
    print(n1, n2, n3)
    if n1 > n3:
        print(n1, n3, n2)
    else:
        print(n3, n1, n2)
elif n2 > n3:
    if n1 > n3:
        print(n2, n1, n3)
    else:
        print(n2, n3, n1)
else:
    print(n3, n2, n1)