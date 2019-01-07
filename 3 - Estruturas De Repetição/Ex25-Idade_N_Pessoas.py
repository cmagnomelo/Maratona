quantidade = int(input('Quantas pessoas tem na Turma? '))
media = 0

for i in range(1,quantidade+1):
    idade = float(input('Informe a idade do aluno {}: '.format(i)))
    media += idade

media = media / quantidade

if media >= 0 and media <= 25:
    print('A turma é jovem')
elif media >= 26 and media <= 60:
    print('A turma é adulta')
elif media > 60:
    print('A turma pe idosa')
else:
    print('media invalida')