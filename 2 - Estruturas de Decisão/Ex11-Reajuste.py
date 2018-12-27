salario = float(input('Informe o salário: '))
valor_reajuste = None
reajuste = None

if salario >= 0 and salario < 280:
    reajuste = 20
    valor_reajuste = (salario * reajuste) / 100
elif salario >= 280 and salario < 700:
    reajuste = 15
    valor_reajuste = (salario * reajuste) / 100
elif salario >= 700 and salario < 1500:
    reajuste = 10
    valor_reajuste = (salario * reajuste) / 100
elif salario >= 1500:
    reajuste = 5
    valor_reajuste = (salario * reajuste) / 100
else:
    print('informação inválida')
    exit()

print('Salário antes do reajuste: R$ {:.2f}'.format(salario))
print('Percentual do reajuste   :  + {}%'.format(reajuste))
print('Valor do aumento         : R$ {:.2f}'.format(valor_reajuste))
print('Salário rejustado        : R$ {:.2f}'.format(salario + valor_reajuste))
