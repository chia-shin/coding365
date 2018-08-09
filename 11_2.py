a,b,c,count=[],[0,0],0,0
for i in range(0,100):
    a.append(0)
while c<3:
    b = sorted([int(input()),int(input())])
    for i in range(b[0]+50,b[1]+50):
        a[i]=1
    c += 1
for i in range(0,100):
    if a[i]==1:
        count += 1
print(count)