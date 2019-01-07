valor = 0.18

print('Panificadora Pão de Ontem - Tabela de preços')

for i in range(1,51):
    print('{} - {:.2f}'.format(i, i * valor))