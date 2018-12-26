valor_hora = float(input('Quanto você ganha por hora? '))
hora_trabalho = int(input('Quantas horas você trabalhou? '))

valor_receber = valor_hora * hora_trabalho

print('Você deve receber {:.2f} reais pelas horas trabalhadas'.format(valor_receber))