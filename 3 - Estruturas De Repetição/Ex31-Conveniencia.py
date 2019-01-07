condicao = True

while condicao:
    print('Lojas Tabajara')
    total = 0.0
    valor = 1
    cont = 1

    while valor != 0:
        valor = float(input('Produto {}:'.format(cont)))
        cont += 1
        total += valor

    print('Total: R$ {:.2f}'.format(total))
    dinheiro = float(input('Dinheiro: R$'))
    print('Troco: R$ {:.2f}'.format(dinheiro - total))

    print('Proxima compra?')
    op = int(input('1 - Sim 2 - Não'))
    if op == 2:
        condicao = False