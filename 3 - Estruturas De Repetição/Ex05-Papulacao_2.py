pais_a = int(input('Informe a população do primeira pais: '))
pais_b = int(input('Informe a população do segundo pais: '))
taxa_a = float(input('Informe a taxa de crescimento populacional do primeiro pais: ')) / 100
taxa_b = float(input('Informe a taxa de crescimento populacional do segundo pais: ')) / 100
anos = 0


while pais_a < pais_b:
    pais_a += pais_a * taxa_a
    pais_b += pais_b * taxa_b
    anos += 1

print('O numero de anos necessarios para o Pais A ultrapassar o Pais B é', anos)