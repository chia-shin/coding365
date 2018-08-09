import string
import sys
A=['','','','']
B=['','','','']
C=['','','','']
a=[0,0,0,0]
b=[0,0,0,0]
c=[0,0,0,0]
i = 0

while i<4:
    A[i]=input()
    if len(A[0])!=4:
        print("-1")
        sys.exit()
    if i==2:
        if A[i]!='':
            a[0]=int(A[i][0:1])
            a[1]=int(A[i][1:])
    if i==3:
        if A[i]!='':
            a[2]=int(A[i][0:1])
            a[3]=int(A[i][1:])
    i = i+1
    if A[1] == '1':
        i = i+1
i = 0
while i<4:
    B[i]=input()
    if len(B[0])!=4:
        print("-1")
        sys.exit()
    if i==2:
        if B[i]!='':
            b[0]=int(B[i][0:1])
            b[1]=int(B[i][1:])
    if i==3:
        if B[i]!='':
            b[2]=int(B[i][0:1])
            b[3]=int(B[i][1:])
    i = i+1
    if B[1] == '1':
        i = i+1
i = 0
while i<4:
    C[i]=input()
    if len(C[0])!=4:
        print("-1")
        sys.exit()
    if i==2:
        if C[i]!='':
            c[0]=int(C[i][0:1])
            c[1]=int(C[i][1:])
    if i==3:
        if C[i]!='':
            c[2]=int(C[i][0:1])
            c[3]=int(C[i][1:])
    i = i+1
    if C[1] == '1':
        i = i+1

if (a[0]>5 or a[2]>5 or a[0]<1 or a[2]<1 or b[0]>5 or b[2]>5 or b[0]<1 or b[2]<1 or c[0]>5 or c[2]>5 or c[0]<1 or c[2]<1):
    if a[0] != 0 and b[0] != 0 and c[0] != 0: 
        print("-1")
        sys.exit()
    else:
        print("correct")
        sys.exit()
elif (a[1]>9 or a[3]>9 or a[1]<1 or a[3]<1 or b[1]>9 or b[3]>9 or b[1]<1 or b[3]<1 or c[1]>9 or c[3]>9 or c[1]<1 or c[3]<1):
    if a[1] != 0 and b[1] != 0 and c[1] != 0: 
        print("-1")
        sys.exit()
    else:
        print("correct")
        sys.exit()

elif len(A[0]) != 4 or len(B[0]) != 4 or len(C[0]) != 4:
    print("-1")
    sys.exit()
elif A[2] != (B[2] or B[3] or C[2] or C[3]) and A[3] != (B[2] or B[3] or C[2] or C[3]):
    if  B[2] != (C[2] or C[3]) and B[3] != (C[2] or C[3]):
        if (A[1] != '1' and A[1] != '2') or (B[1] != '1' and B[1] != '2') or (C[1] != '1' and C[1] != '2'):
            print("-1")
            sys.exit()
        else:
            print("correct")
            sys.exit()
if A[2] == B[2] or  A[2] == B[3]: 
    print(A[0]+','+B[0]+','+A[2])
if A[2] == C[2] or A[2] == C[3]:
    print(A[0]+','+C[0]+','+A[2])
if A[3] == B[2] or A[3] == B[3]:
    print(A[0]+','+B[0]+','+A[3])
if A[3] == C[2] or A[3] == C[3]:
    print(A[0]+','+C[0]+','+A[3])
if B[2] == C[2] or B[2] == C[3]:
    print(B[0]+','+C[0]+','+B[2])
if B[3] == C[2] or B[3] == C[3]:
    print(B[0]+','+C[0]+','+B[3])