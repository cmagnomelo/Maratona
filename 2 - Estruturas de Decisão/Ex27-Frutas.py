qtde_morango = float(input('Quantos Kg de morango você deseja? '))
qtde_maca = float(input('Quantos Kg de maçã você deseja? '))

if qtde_morango >= 0 and qtde_morango <= 5:
    valor_morango = qtde_morango * 2.50
elif qtde_morango > 5:
    valor_morango = qtde_morango * 2.20
else:
    print('Quantidade negativa')
    exit()

if qtde_maca >= 0 and qtde_maca <= 5:
    valor_maca = qtde_maca * 1.80
elif qtde_maca > 5:
    valor_maca = qtde_maca * 1.50
else:
    print('Quantidade negativa')
    exit()

qtde_total = qtde_morango + qtde_maca
valor_total = valor_maca + valor_morango

if qtde_total > 8 or valor_total > 25:
    valor_total -= valor_total * (10/100)

print('Valor total a pagar é {}'.format(valor_total))
