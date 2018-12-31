cont_par = 0
cont_impar = 0


for i in range(1,11):
    print('Digite o o numero',i, end=' ')
    numero = int(input(':'))
    if numero % 2 == 0:
        cont_par += 1
    else:
        cont_impar += 1

print('A quantidade de numeros pares foi', cont_par)
print('A quantidade de numeros impares foi', cont_impar)