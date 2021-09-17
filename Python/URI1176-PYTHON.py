# Exercicio 1176 de Python do URI, author:Julia Suriani
t = int(input())

for i in range(0, t):
    x = int(input())
    f = [0, 1]
    if x > 1:
        for j in range(2, x + 1):
            f.append(f[j - 2] + f[j - 1])
        print('Fib({}) = {}'.format(x, f[x]))
    if x <= 1:
        print('Fib({}) = {}'.format(x, f[x]))
