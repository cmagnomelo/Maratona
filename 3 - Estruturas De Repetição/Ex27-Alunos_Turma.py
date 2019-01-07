turmas = int(input('Informe a quantidade de turma: '))
media = 0

for i in range(1,turmas+1):
    condicao = True
    while condicao:
        quantidade = int(input('Qual a quantidade de alunos na turma {}? '.format(i)))
        if quantidade < 0:
            print('Quantidade de alunos deve ser maior que 0')
        elif quantidade > 40:
            print('Quantidade de alunos deve ser inferior a 40')
        else:
            media += quantidade
            condicao = False

print('A média de alunos nas trumas é de {}'.format(media/turmas))