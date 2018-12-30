print('Qual combustível você deseja?')
print('A - Álcool')
print('G - gasolina')
opcao = input('Escolha: ')

litro_A = 1.90
litro_G = 2.50

if opcao == 'A' or opcao == 'a':
    print('Opção escolhida foi Álcool')
    opcao = float(input('Quantos litro você deseja: '))
    if opcao > 0 and opcao <= 20:
        litro_A = litro_A - (litro_A * (3 / 100))
        valor = opcao * litro_A
    elif opcao > 20:
        litro_A = litro_A - (litro_A * (5 / 100))
        valor = opcao * litro_A
    else:
        print('Opção inválida')
        exit()
elif opcao == 'G' or opcao == 'g':
    print('Opção escolhida foi Gasolina')
    opcao = float(input('Quantos litro você deseja: '))
    if opcao > 0 and opcao <= 20:
        litro_G = litro_G - (litro_G * (4 / 100))
        valor = opcao * litro_G
    elif opcao > 20:
        litro_G = litro_G - (litro_G * (6 / 100))
        valor = opcao * litro_G
    else:
        print('Opção inválida')
        exit()
else:
    print('Opção inválida')
    exit()

print('Valor a ser pago é {:.2f}'.format(valor))