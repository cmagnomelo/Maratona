numero = int(input('Informe numero base desejado: '))
expoente = int(input('Informe o expoente: '))
resultado = 1

if expoente == 0:
    print('1')
else:
    for i in range(1, expoente + 1):
        resultado *= numero

print(resultado)