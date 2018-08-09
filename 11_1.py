import math
a=sorted([int(input()),int(input())])
b=sorted([int(input()),int(input())])
c=sorted([int(input()),int(input())])

def com(lon,a, b):
    temp = [0,0]
    if b[0]<=a[0]<=b[1]:
        lon += (a[0]-b[0]) - (temp[1]-temp[0])
        a[0],b[0]=b[0],a[0]
    if b[0]<=a[1]<=b[1]:
        lon += b[1]-a[1] - (temp[1]-temp[0])
        a[1],b[1]=b[1],a[1]
    elif b[1]<a[0] or b[0]>a[1]:
        lon += (b[1]-b[0]) - (temp[1]-temp[0])
        if b[1]<a[0]:
            temp = [b[1],a[0]]
            a[0],b[0]=b[0],a[0]
        else:
            temp = [a[1],b[0]]
            a[1],b[1] = b[1],a[1]
    return(lon,a,temp)
	
lon = a[1]-a[0]
lon,a,temp = com(lon,a,b)
lon = a[1]-a[0]
lon,a,temp = com(lon,a,c)
print(lon)