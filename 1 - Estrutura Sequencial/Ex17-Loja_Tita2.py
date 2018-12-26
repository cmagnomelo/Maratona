import math

lata = 18
galao = 3.6
preco_lata = 80
preco_galao = 25
litro_tinta = 6

area = float(input('Qual o tamanho da area? '))
litros = math.ceil(area/litro_tinta)
print('Você vai precisar de', litros,'litros')
print('')

latas_necessarias = math.ceil(litros/lata)
print('Latas necessárias:', latas_necessarias, (lata * latas_necessarias), 'litros')
print('Valor total de latas é: R$ {:.2f}'.format(latas_necessarias * preco_lata))
print('')

galoes_necessarios = math.ceil(litros/galao)
print('Galões necessários:', galoes_necessarios, (galao * galoes_necessarios), 'litros')
print('Valor total de galões é: R$ {:.2f}'.format(galoes_necessarios * preco_galao))

if((litros % lata) < (3.6 * 4)):# 4 galões são mais caros que uma lata
    galoes_necessarios = math.ceil((litros % lata) / galao)
    latas_necessarias -= galoes_necessarios

print('Latas {} e Galoes {}: Preço Final {}'.format(latas_necessarias, galoes_necessarios, (latas_necessarias * preco_lata) + (galoes_necessarios * preco_galao)))
