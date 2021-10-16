# Exercicio 2850 de Python do URI, utilizando dicionarios e tratamento de erro author:Julia Suriani
papagaio = {'esquerda': 'ingles', 'direita': 'frances', 'nenhuma': 'portugues', 'as duas': 'caiu'}

while True:
    try:
        t = str(input())
        if t == 'esquerda':
            print(papagaio['esquerda'])

        if t == 'direita':
            print(papagaio['direita'])

        if t == 'nenhuma':
            print(papagaio['nenhuma'])

        if t == 'as duas':
            print(papagaio['as duas'])
            
    except EOFError:
        break
