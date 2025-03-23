a = int(input())
b = int(input())
c = int(input())

x = a - b - c
y = a - c * b

arr = []
arr.append(x)
arr.append(y)

print(min(arr))