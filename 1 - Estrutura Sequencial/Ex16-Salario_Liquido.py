valor_hora = float(input('Quanto você ganha por hora? '))
hora_trabalho = int(input('Quantas horas você trabalhou? '))
valor_receber = valor_hora * hora_trabalho
ir = (valor_receber * 11) / 100
inss = (valor_receber * 8) / 100
sindicato = (valor_receber * 5) / 100
descontos = ir + sindicato + inss


print('+ Salário Bruto  : R$ {:.2f}'.format(valor_receber))
print('- IR             : R$ {:.2f}'.format(ir))
print('- INSS           : R$ {:.2f}'.format(inss))
print('- Sindicato      : R$ {:.2f}'.format(sindicato))
print('= Salário Liquido: R$ {:.2f}'.format(valor_receber - descontos))
