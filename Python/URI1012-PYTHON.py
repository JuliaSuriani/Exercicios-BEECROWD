# Exercicio 1012-AREA de Python do URI author:Julia Suriani
A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)
tri = (A*C)/2
cir = (3.14159*(C*C))
tra = ((A+B)*C)/2
qua = (B*B)
ret = (A*B)
print('TRIANGULO: {:.3f}'.format(tri))
print('CIRCULO: {:.3f}'.format(cir))
print('TRAPEZIO: {:.3f}'.format(tra))
print('QUADRADO: {:.3f}'.format(qua))
print('RETANGULO: {:.3f}'.format(ret))

'''
OU 
print(f'TRIANGULO: {tri:.3f}')
print(f'CIRCULO: {cir:.3f}')
print(f'TRAPEZIO: {tra:.3f}')
print(f'QUADRADO: {qua:.3f}')
print(f'RETANGULO: {ret:.3f}')
'''