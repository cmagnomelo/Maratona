fibonacci = int(input('Qual termo de Fibonacci você deseja? '))
atual = 0
proximo = 1

print(atual)

for i in range(fibonacci - 1):
    anterior = atual
    atual = proximo
    proximo = atual + anterior
    print(atual)
