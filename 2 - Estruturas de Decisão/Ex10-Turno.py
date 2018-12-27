print('Informe seu Turno:')
print('Matutino---(M)')
print('Vespertino-(V)')
print('Noturno----(N)')
turno = input(': ')

if turno == 'M' or turno == 'm':
    print('Bom dia')
elif turno == 'V' or turno == 'v':
    print('Boa tarde')
elif turno == 'N' or turno == 'n':
    print('Boa Noite')
else:
    print('Opção inválida')