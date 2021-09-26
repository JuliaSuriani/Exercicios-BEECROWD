# Exercicio 2850 de Python do URI, author:Julia Suriani
papagaio = {'esquerda': 'ingles', 'direita': 'frances', 'nenhuma': 'portugues', 'as duas': 'caiu'}
i = 1
while i > 0:
    t = input()
    if t == 'esquerda':
        print(papagaio['esquerda'])
        i = i + 1
    if t == 'direita':
        print(papagaio['direita'])
        i = i + 1
    if t == 'nenhuma':
        print(papagaio['nenhuma'])
        i = i + 1
    if t == 'as duas':
        print(papagaio['as duas'])
        i = i + 1
