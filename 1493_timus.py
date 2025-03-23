n = int(input())
n = str(n)

n = str(int(n) + 1).zfill(6)

for i in range(2):
    s = 0
    for i in range(len(n)//2):
        s += int(n[i])
    s2 = 0
    for i in range(len(n)//2):
        s2 += int(n[i+3])

    if s == s2:
        print('Yes')
        break
    else:
        n = str(int(n) - 2).zfill(6)
else:
    print('No')