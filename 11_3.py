a,b,count=[],[0,0],0
for i in range(0,100):
    a.append(0)
while b!="":
    b[0] = input()
    if b[0] == "":    break
    b = [int(b[0]),int(input())] 
    b.sort()
    for i in range(b[0]+50,b[1]+50):
        a[i]=1
for i in range(0,100):
    if a[i]==1:
        count += 1
print(count)