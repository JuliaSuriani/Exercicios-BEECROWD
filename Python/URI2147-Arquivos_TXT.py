# Exercicio 2147 de Python do URI, usando arquivos de texto para executar author:Julia Suriani

c = int(input())
for i in range(c):
    arq = open('Arquivo2147.txt', 'w')
    t = input()
    t = len(t)
    arq.write(str(t))
    arq.write('\n')
    arq.close()
    arq = open('Arquivo2147.txt', 'r')
    arq.seek(0, 0)
    lista = arq.readlines()
    num = lista[0].split('\n')
    print('{:.2f}'.format(float(lista[0])/100.0))
