arquivo = float(input('Qual o tamanho do arquivo (Mb)? '))
largura = float(input('Qual a largura de banda(Mbps)? '))

velocidade = (arquivo * 1024) / ((largura*1024)/8)

print('Otempo para download é: {:.2f} minutos'.format(velocidade/60))