def tipo_carne(opcao):
    if opcao == '1':
        return 'File Duplo'
    elif opcao == '2':
        return 'Alcatra'
    elif opcao == '3':
        return 'Picanha'
    else:
        exit()

def calcula_preco(tipo_carne, quantidade):
    if tipo_carne == 'File Duplo':
        if quantidade > 0 and quantidade <= 5:
            return quantidade * 4.90
        elif quantidade > 5:
            return quantidade * 5.80
        else:
            print('Quantidade Inválida')
    elif tipo_carne == 'Alcatra':
        if quantidade > 0 and quantidade <= 5:
            return quantidade * 5.90
        elif quantidade > 5:
            return quantidade * 6.80
        else:
            print('Quantidade Inválida')
    elif tipo_carne == 'Picanha':
        if quantidade > 0 and quantidade <= 5:
            return quantidade * 6.90
        elif quantidade > 5:
            return quantidade * 7.80
        else:
            print('Quantidade Inválida')
    else:
        print('Quantidade ou opção Inválida')
        exit()


print('#####################################')
print('#         PROMOCAO DE CARNES        #')
print('#           Até 5Kg      Acima 5kg  #')
print('#File duplo R$ 4.90 /kg  R$ 5,80 /Kg#')
print('#Alcatra    R$ 5.90 /kg  R$ 6,80 /Kg#')
print('#Picanha    R$ 6.90 /kg  R$ 7,80 /Kg#')
print('#####################################')

print('Você poderá escolher apenas 2 tipos de carne:')
print('1 - Fila Duplo')
print('2 - Alcatra')
print('3 - Picanha')

tipo1 = input('Opção 1: ')
tipo1 = tipo_carne(tipo1)
quantidade1 = float(input('Quantidade em Kg: '))
valor1 = calcula_preco(tipo1,quantidade1)

tipo2 = input('Opção 2: ')
tipo2 = tipo_carne(tipo2)
quantidade2 = float(input('Quantidade em Kg: '))
valor2 = calcula_preco(tipo2,quantidade2)
valor_total = valor1 + valor2


print('Tipo de pagamento: ')
print('1 - à vista: ')
print('2 - cartão: ')
print('3 - cartão da loja: ')
tipo_pagamento = int(input('Digite forma de pagamento: '))
desconto = 0

if tipo_pagamento == 3:
    desconto = valor_total*(5/100)

print('###################################')
print('          Cupom Fiscal           ')
print('{} {}kg R$ {}#'.format(tipo1,quantidade1,valor1))
print('{} {}kg R$ {}#'.format(tipo2,quantidade2,valor2))
if desconto != 0:
    print('(-)Desconto R$ {:.2f}#'.format(desconto))
print('TOTAL R$ {}'. format(valor_total - desconto))