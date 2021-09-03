# Exercicio 1160 de Python do URI, author:Julia Suriani
def anos():
    print('{} anos'.format(ano))


# Programa principal
t = int(input())
for i in range(0, t):
    PA, PB, GA, GB = map(float, input().split())
    PA = int(PA)
    PB = int(PB)
    ano = 0
    while PB >= PA:
        PA = int(PA * (1 + GA / 100))
        PB = int(PB * (1 + GB / 100))
        ano += 1
        if ano > 100:
            print('Mais de 1 seculo.')
            break
    if ano <= 100:
        ano = int(ano)
        anos()
