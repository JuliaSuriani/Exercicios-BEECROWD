# Exercicio 3047 de Python do URI, utilizando tratamento de erro, author:Julia Suriani
M = int(input())
A = int(input())
B = int(input())
try:
    X = M - A - B
    if X > A and X > B:
        print(X)
    elif A > B and A > X:
        print(A)
    else:
        print(B)
except ValueError:
    print('Opa!O tipo de entrada é invalido.')
