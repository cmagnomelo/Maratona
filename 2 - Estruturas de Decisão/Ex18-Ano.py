dia, mes, ano = input('Digite uma data no seguinte formato dd/mm/aaaa:').split('/')
dia = int(dia)
mes = int(mes)
ano = int(ano)

if dia < 0 or dia > 31:
    print('Data invalida')
elif mes < 0 or mes > 12:
    print('Data invalida')
elif ano < 0:
    print('Data invalida')
else:
    print(dia,'/',mes,'/',ano,'É uma data Valida')