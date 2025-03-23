n = int(input())
arr = []

if n < 1:
    for i in range(1,n-1,-1):
        arr.append(i)
else:
    for i in range(1, n+1):
        arr.append(i)

print(sum(arr))