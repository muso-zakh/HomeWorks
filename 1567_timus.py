a = ['a','d','g','j','m','p','s','v','y','.', ' ']
b = ['b','e','h','k','n','q','t','w','z',',']
c = ['c','f','i','l','o','r','u','x','!']

n = input()
n = list(n)
s = 0
x = 0
for i in n:
    if i in a:
        x = 1
    elif i in b:
        x = 2
    else:
        x = 3
    
    s += x

print(s)