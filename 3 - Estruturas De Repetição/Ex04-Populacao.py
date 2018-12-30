pais_a = 80000
pais_b = 200000
taxa_a = 3/100
taxa_b = 1.5/100
anos = 0

while pais_a < pais_b:
    pais_a += pais_a * taxa_a
    pais_b += pais_b * taxa_b
    anos += 1
    
print('O numero de anos necessarios para o Pais A ultrapassar o Pais b é', anos)