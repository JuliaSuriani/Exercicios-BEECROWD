# Exercicio 1329 de Python do URI, usando arquivos binários para executar author:Julia Suriani
import pickle

while 1:
    qte = int(input())

    if qte == 0:
        break
    arq = open('arquivo1329.pck', 'wb')
    resultados = list(map(int, input().split()))
    m = 0
    j = 0

    for v in resultados:
        if v == 0:
            m += 1

        else:
            j += 1
    pickle.dump(m, arq)
    pickle.dump(j, arq)
    arq.close()
    arq = open('arquivo1329.pck', 'rb')
    mary = pickle.load(arq)
    jhon = pickle.load(arq)
    print('Mary won {} times and John won {} times'.format(mary, jhon))
    arq.close()
