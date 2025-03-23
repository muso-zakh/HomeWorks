a = ['Alice','Ariel','Aurora','Phil','Peter','Olaf','Phoebus','Ralph','Robin']
b = ['Bambi','Belle','Bolt','Mulan','Mowgli','Mickey','Silver','Simba','Stitch']
c = ['Dumbo','Genie','Jiminy','Kuzko','Kida','Kenai','Tarzan','Tiana','Winnie']

n = int(input())
s = 0
x = 0
for i in range(n):
    p = input()
    if p in a:
        p = 1
    elif p in b:
        p = 2
    else:
        p = 3
    
    s += abs(p - x)
    x = p

print(s-1)