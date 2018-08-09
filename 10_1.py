import sys
a,s=[int(input()),int(input()),int(input()),0],0
if a[1]==2:
    a[3] = int(input())
    if (a[3]>58 or a[3]<11 or 21>a[3]>18 or 31>a[3]>28 or 41>a[3]>38 or 51>a[3]>48):
        print("-1")
        sys.exit()        
if (a[0]<1000 or  a[1]>2 or a[1]<1 or a[2]>58 or a[2]<11 or 21>a[2]>18 or 31>a[2]>28 or 41>a[2]>38 or 51>a[2]>48):
    print("-1")
    sys.exit()
                
b=[int(input()),int(input()),int(input()),0]
if b[1]==2:
    b[3] = int(input())
    if (b[3]>58 or b[3]<11 or 21>b[3]>18 or 31>b[3]>28 or 41>b[3]>38 or 51>b[3]>48):
        print("-1")
        sys.exit()    
if (b[0]<1000 or b[1]>2 or b[1]<1 or b[2]>58 or b[2]<11 or 21>b[2]>18 or 31>b[2]>28 or 41>b[2]>38 or 51>b[2]>48):
    print("-1")
    sys.exit()

c=[int(input()),int(input()),int(input()),0]
if c[1]==2:
    c[3] = int(input())
    if (c[3]>58 or c[3]<11 or 21>c[3]>18 or 31>c[3]>28 or 41>c[3]>38 or 51>c[3]>48):
        print("-1")
        sys.exit()    
if (c[0]<1000 or  c[1]>2 or c[1]<1 or c[2]>58 or c[2]<11 or 21>c[2]>18 or 31>c[2]>28 or 41>c[2]>38 or 51>c[2]>48):
    print("-1")
    sys.exit()
   
if ((a[2] == b[2]) or  (a[2] == b[3])):
    print("%d,%d,%d" % (a[0],b[0],a[2]))
    s+=1
if ((a[2] == c[2]) or  (a[2] == c[3])):
    print("%d,%d,%d" % (a[0],c[0],a[2]))
    s+=1
if ((a[3] == b[2]) or  (a[3] == b[3])):
    print("%d,%d,%d" % (a[0],b[0],a[3]))
    s+=1
if ((a[3] == c[2]) or  (a[3] == c[3])):
    print("%d,%d,%d" % (a[0],c[0],a[3]))
    s+=1
if ((b[2] == c[2]) or  (b[2] == c[3])):
    s+=1
    print("%d,%d,%d" % (b[0],c[0],b[2]))
if ((b[3] == c[2]) or  (b[3] == c[3])):
    print("%d,%d,%d" % (b[0],c[0],b[3]))
    s+=1
if s==0:    print("correct")