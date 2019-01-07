quantidade = int(input('Informe a quantidade de CD\'s: ' ))
total = 0


for i in range(1,quantidade + 1):
    valor = float(input('Qual o valor do CD {}: '.format(i)))
    total += valor

print('Valor total gasto foi {:.2f}'.format(total))
print('A média por cd foi {:.2f}'.format(total/quantidade))