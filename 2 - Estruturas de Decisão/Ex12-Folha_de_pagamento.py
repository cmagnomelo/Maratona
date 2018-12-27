horas = int(input('Informe numero de horas trabalhadas: '))
valor_hora = float(input('Informe valor por hora: '))
print('')
salario = valor_hora * horas
ir = None
inss = 10

if salario > 0 and salario <= 900:
    ir = 0
elif salario > 900 and salario <= 1500:
    ir = 5
elif salario > 1500 and salario <= 2500:
    ir = 10
elif salario > 2500:
    ir = 20
else:
    print('Valor inválido')

print('Salário Bruto: R$ {:.2f}'.format(salario))
if ir == 0:
    print('(-) IR : Isento')
else:
    print('(-) IR ({}%) : R$ {:.2f}'.format(ir, (salario * ir) / 100))
print('(-) INSS ({}%) : R$ {:.2f}'.format(ir, (salario * inss) / 100))
print('FGRS (11%) : R${:.2f}'.format((salario * 11) / 100))
print('Total de descontos: R${:.2f}'.format((salario * ir) / 100 + (salario * inss) / 100))
print('Salário Liquido: R$ {:.2f}'.format(salario - ((salario * ir) / 100 + (salario * inss) / 100)))
