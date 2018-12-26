kg_peixe = float(input('Quantos kg tem o peixe? '))
quilo_excedente = kg_peixe - 50
multa = quilo_excedente * 4.00

if(quilo_excedente <= 0):
    print('Não pagará multa')
else:
    print('Sua pesagem ultrapassou o limite em', quilo_excedente)
    print('Valor da multa é {:.2f}'.format(multa))