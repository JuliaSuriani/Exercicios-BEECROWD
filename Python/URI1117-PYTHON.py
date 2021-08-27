# Exercicio 1117 de Python do URI author:Julia Suriani
media = 0
c = 0
while c < 2:
    nota1 = float(input(''))
    if 0 <= nota1 <= 10:
        c = c+1
        media = media+nota1

    else:
        print('nota invalida')
media = media/2
print('media = {:.2f}'.format(media))
