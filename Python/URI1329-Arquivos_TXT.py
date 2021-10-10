# Exercicio 1329 de Python do URI, usando arquivos de texto para executar author:Julia Suriani


while 1:
    qte = int(input())

    if qte == 0:
        break
    arq = open('Arquivo1329.txt', 'w')
    resultados = list(map(int, input().split()))
    m = 0
    j = 0

    for v in resultados:
        if v == 0:
            m += 1

        else:
            j += 1

    arq.write(str(m))
    arq.write('\n')
    arq.write(str(j))
    arq.write('\n')
    arq.close()
    arq = open('Arquivo1329.txt', 'r')
    arq.seek(0, 0)
    lista = arq.readlines()
    num = lista[0].split('\n')
    print('Mary won {} times and John won {} times'.format(int(lista[-2]), int(lista[-1])))
    arq.close()
