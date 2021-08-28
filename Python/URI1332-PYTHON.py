# Exercicio 1332 de Python do URI, author:Julia Suriani
n = int(input())
for i in range(n):
    num = input()
    if len(num) > 3:
        print('3')
    if ((num[0:1] == 't') and (num[1:2] == 'w')) or ((num[0:1] == 't') and (num[2:3] == 'o')) or (
            (num[1:2] == 'w') and (num[2:3] == 'o')):
        print('2')
    if ((num[0:1] == 'o') and (num[1:2] == 'n')) or ((num[0:1] == 'o') and (num[2:3] == 'e')) or (
            (num[1:2] == 'n') and (num[2:3] == 'e')):
        print('1')
