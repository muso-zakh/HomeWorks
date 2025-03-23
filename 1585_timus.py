n = int(input())
arr = []


for i in range(n):
    p = input()
    arr.append(p)

a = arr.count('Emperor Penguin')
b = arr.count('Macaroni Penguin')
c = arr.count('Little Penguin')
maxx = max(a, b, c)

if maxx == a:
    print('Emperor Penguin')
elif maxx == b:
    print('Macaroni Penguin')
else:
    print('Little Penguin')