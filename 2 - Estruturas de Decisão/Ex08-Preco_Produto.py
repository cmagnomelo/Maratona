preco1 = float(input('Informe o preço do produto 1: '))
preco2 = float(input('Informe o preço do produto 2: '))
preco3 = float(input('Informe o preço do produto 3: '))

if preco1 < preco2 and preco1 < preco3:
    print('Você deve comprar o produto 1.')
elif preco2 < preco3:
    print('Você deve comprar o produto 2.')
else:
    print('Você deve comprar o produto 3.')