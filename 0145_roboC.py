n = int(input())
x = list(map(int, input().split()))
x.sort()

for i in range(len(x)-2):
    if x[-3] + x[-2] > x[-1]:
        print(x[-3], x[-2], x[-1])
        break
    else:
        x.remove(x[-1])
else:
    print(-1)