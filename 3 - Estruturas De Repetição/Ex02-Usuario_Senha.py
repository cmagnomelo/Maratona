condicao = True

while condicao:
    user = input('Digite usuário: ')
    password = input('Digite senha: ')

    if user == password:
        print('Logado no sistema')
        condicao = False
    else:
        print('Usuário e Senha não são iguais. Tente novamente')