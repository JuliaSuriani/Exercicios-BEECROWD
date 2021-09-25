# Exercicio 2061 de Python do URI, author:Julia Suriani
n = input()
n = n.split()
m = int(n[0])
for i in range(int(n[1])):
    a = input()

    if a == 'fechou':
        m = m + 1
    elif a == 'clicou':
        m = m -1
print(m)
