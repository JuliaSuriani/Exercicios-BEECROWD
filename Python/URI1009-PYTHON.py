# Exercicio 1009 de Python do URI author:Julia Suriani

nome = str(input())  # nome do vendedor
v1 = float(input())  # salário fixo do vendedor
v2 = float(input())  # montante total das vendas efetuadas por este vendedor
total = (v1+(v2*15/100))
print('TOTAL = R$ {:.2f}'.format(total))

''' 
ou
print(f'TOTAL = R$ {total:.2f}')
'''
