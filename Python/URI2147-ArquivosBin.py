# Exercicio 2147 de Python do URI, usando arquivos binários para executar author:Julia Suriani
import pickle

c = int(input())
for i in range(c):
    arq = open('arquivo2147.pck', 'wb')
    t = input()
    t = len(t)
    pickle.dump(t, arq)
    arq.close()
    arq = open('arquivo2147.pck', 'rb')
    tam = pickle.load(arq)
    print('{:.2f}'.format(float(tam)/100.0))
    arq.close()
