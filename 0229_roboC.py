from math import sqrt
a, b = map(int, input().split())

x = (a + b) / 2
y = sqrt(a * b)

if x > y:
    print('>')
elif y > x:
    print('<')
else:
    print('=')