numero1 = float(input('Digite o primeiro numero: '))
numero2 = float(input('Digite o segundo numero: '))
resultado = None

print('Qual operação deseja realizar:')
print('1 - SOMAR')
print('2 - SUBTRAIR')
print('3 - MULTIPLICAR')
print('4 - DIVIDIR')
opcao = int(input('Escolha a opção: '))

if opcao == 1:
    resultado = numero1 + numero2
elif opcao == 2:
    resultado = numero1 - numero2
elif opcao == 3:
    resultado = numero1 * numero2
elif resultado == 4:
    resultado = numero1 / numero2
else:
    print('Opção inválida')

print('O resultado é', resultado)

if resultado % 2 == 0:
    print('Resultado é par')
else:
    print('Resultado é impar')

if resultado >= 0:
    print('Resultado é positivo')
else:
    print('Resultado é negativo')

if (round(resultado) - resultado) == 0:
    print('Resultado é inteiro')
else:
    print('Resultado é decimal')