x = int(input())

x = str(x)
x = list(x)
arr2 =[6,2,5,5,4,5,6,3,7,6]
y = 0

for i in range(len(x)):
    y += arr2[int(x[i])]

print(y)