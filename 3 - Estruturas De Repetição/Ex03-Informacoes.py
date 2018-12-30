condicao = True
while condicao:
    nome = input('Escreva o nome: ')
    if len(nome) > 3:
        condicao = False
    else:
        print('Nome deve ter mais de 3 letras. Digite outro nome.')

condicao = True
while condicao:
    idade = int(input('Digite sua idade: '))
    if idade > 0 and idade <= 150:
        condicao = False
    else:
        print('Idade inválida')

condicao = True
while condicao:
    salario = float(input('Digite seu salario: R$ '))
    if salario > 0:
        condicao = False
    else:
        print('Salario menor que zero')

condicao = True
while condicao:
    sexo = input('Sexo: M - Mascuslino F - Feminino: ')
    if sexo == 'f' or sexo == 'F' or sexo == 'M' or sexo == 'm':
        condicao = False
    else:
        print('Opção inválida')

condicao = True
while condicao:
    estado_civil = input('Estado Civil: S - Solteiro C - Casado V - Viuvo D - Divorciado: ')
    if estado_civil == 'S' or estado_civil == 'C' or estado_civil == 'V' or estado_civil == 'D' or estado_civil == 's' or estado_civil == 'c' or estado_civil == 'v' or estado_civil == 'd':
        condicao = False
    else:
        print('Opção inválida')
