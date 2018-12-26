area = float(input('Qual o tamanho da area? '))
latas = area / 54
valor_total = latas * 80

print('Quantidade de Latas: {:.2f}'.format(latas))
print('Valor total a pagar é: R$ {:.2f}'.format(valor_total))