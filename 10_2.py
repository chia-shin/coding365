import sys
a, b, c = [0,0,0,0],[0,0,0,0],[0,0,0,0]
def ya(a):
    a = [int(input()),int(input()),int(input()),0]
    if a[1] == 2:
        a[3] = int(input())
        if (a[3]>58 or a[3]<11 or 21>a[3]>18 or 31>a[3]>28 or 41>a[3]>38 or 51>a[3]>48):
            print("-1")
            sys.exit()
    if (a[0]<1000 or  a[1]>2 or a[1]<1 or a[2]>58 or a[2]<11 or 21>a[2]>18 or 31>a[2]>28 or 41>a[2]>38 or 51>a[2]>48):
        print("-1")
        sys.exit()
    return a

a, b, c, s = ya(a), ya(b), ya(c), 0

if ((a[2] == b[2]) or  (a[2] == b[3])):
    print("%d,%d,%d" % (a[0],b[0],a[2]))
    s=s+1
if ((a[2] == c[2]) or  (a[2] == c[3])):
    print("%d,%d,%d" % (a[0],c[0],a[2]))
    s=s+1
if ((a[3] == b[2]) or  (a[3] == b[3])):
    print("%d,%d,%d" % (a[0],b[0],a[3]))
    s=s+1
if ((a[3] == c[2]) or  (a[3] == c[3])):
    print("%d,%d,%d" % (a[0],c[0],a[3]))
    s=s+1
if ((b[2] == c[2]) or  (b[2] == c[3])):
    s=s+1
    print("%d,%d,%d" % (b[0],c[0],b[2]))
if ((b[3] == c[2]) or  (b[3] == c[3])):
    print("%d,%d,%d" % (b[0],c[0],b[3]))
    s=s+1
if s==0:    print("correct")