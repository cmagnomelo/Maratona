numero_notas = int(input('Informe quantas notas você irá digitar: '))
media = 0

for i in range(1,numero_notas + 1):
    notas = float(input('Digite a nota {} : '.format(i)))
    media += notas

print('A media dos numeros digitados foi {:.2f}'.format(media/numero_notas))