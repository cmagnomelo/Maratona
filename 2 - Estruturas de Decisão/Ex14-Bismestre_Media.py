nota1 = float(input('Digite a Primeria nota: '))
nota2 = float(input('Digite a Segunda nota: '))
media = (nota1 + nota2) / 2
conceito = None
mensagem = None

if media <= 10 and media >= 9:
    conceito = 'A'
elif media < 9 and media >= 7.5:
    conceito = 'B'
elif media <= 7.5 and media >= 6:
    conceito = 'C'
elif media <= 6 and media >= 4:
    conceito = 'D'
else:
    conceito = 'E'

if conceito == 'A' or conceito == 'B' or conceito == 'C':
    mensagem = 'APROVADO'
else:
    mensagem = 'Reprovado'

print('Primeira Nota\tSegunda Nota\tMédia\tConceito\tSituação')
print('{:.2f}\t        {:.2f}\t        {:.2f}\t{}\t        {}'.format(nota1, nota2, media, conceito,mensagem))


