# Exercicio 1013-AREA de Python do URI author:Julia Suriani
import math
A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)
maiorAB = (A+B+abs(A-B))/2
maiorABC = (maiorAB+C+abs(maiorAB-C))/2
print('{:.0f} eh o maior'.format(maiorABC))
#ou  print(f'eh o maior {maiorABC:.0f}')
