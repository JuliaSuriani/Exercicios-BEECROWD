# Exercicio 1180 de Python do URI, author:Julia Suriani
n = int(input())
x = []
a = list(map(int, input().split()))
for cont in range(n):
    x.insert(cont, a[cont])
    if x[cont] == min(x):
        posicao = cont
print('Menor valor: {}'.format(min(x)))
print('Posicao: {}'.format(posicao))
