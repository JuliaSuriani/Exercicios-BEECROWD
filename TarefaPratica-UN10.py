"""
Entrega da Tarefa Prática da Unidade 10 - 23/10/2021

Escreva uma função recursiva para calcular o fatorial de um número.

Use essa função num programa em python que leia valores gravados em um arquivo texto. 
Podem existir vários valores no arquivo, e o objetivo é calcular o fatorial de cada valor.

O resultado (valor de cada fatorial) deve ser gravado em arquivo.

author: Julia Suriani
"""


def fatorial(N):
    if N == 0:
        return 1
    else:
        return N * fatorial(N - 1)


while 1:
    x = int(input())
    if x < 0:
        print('O valor inserido é incorreto. Por favor insira um valor > ou = a 0')

    arq = open('Arquivo.txt', 'w')
    arq.write(str(x))
    arq.write('\n')
    y = fatorial(x)
    arq.write(str(y))
    arq.write('\n')
    arq.close()
    arq = open('Arquivo.txt', 'r')
    arq.seek(0, 0)
    lista = arq.readlines()
    num = lista[0].split('\n')
    print('O fatorial de', int(x), 'é', int(y))
    arq.close()
