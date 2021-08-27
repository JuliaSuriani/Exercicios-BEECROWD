# Exercicio 1061 de Python do URI author:Julia Suriani

dia, data1 = input().split()
data1 = int(data1)
h1, m1, s1 = map(int, input().split(":"))

dia, data2 = input().split()
data2 = int(data2)
h2, m2, s2, = map(int, input().split(":"))

s = s2 - s1
m = m2 - m1
h = h2 - h1
d = data2 - data1

if s < 0:
    s += 60
    m -= 1

if m < 0:
    m += 60
    h -= 1

if h < 0:
    h += 24
    d -= 1

print('{} dia(s)'.format(d))
print('{} hora(s)'.format(h))
print('{} minuto(s)'.format(m))
print('{} segundo(s)'.format(s))

