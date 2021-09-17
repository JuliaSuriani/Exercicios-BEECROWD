# Exercicio 1065 de Python do URI, author:Julia Suriani
listaNumeros = []
for i in range(0, 5):
    n = int(input())  # entrada de cinco valores
    listaNumeros.append(int(n))  # adiciona os valores n a lista

i = 0
for j in range(5):
    if listaNumeros[j] % 2 == 0:
        i += 1
print(i, 'valores pares')
