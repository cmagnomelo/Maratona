atual = 0
proximo = 1

print(atual)

while atual < 500:
    anterior = atual
    atual = proximo
    proximo = atual + anterior
    print(atual)