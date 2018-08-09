a = [int(i) for (i) in (input().split())]

if a[0]>0 and a[1]>0 and a[2]>0 and a[0]+a[1]>a[2] and a[0]+a[2]>a[1] and a[1]+a[2]>a[0]:
    if a[0]*a[0]+a[1]*a[1]==a[2]*a[2] or a[0]*a[0]+a[2]*a[2]==a[1]*a[1] or a[1]*a[1]+a[2]*a[2]==a[0]*a[0]:  print("Right Triangle")
    elif a[0]*a[0]+a[1]*a[1]<a[2]*a[2] or a[0]*a[0]+a[2]*a[2]<a[1]*a[1] or a[1]*a[1]+a[2]*a[2]<a[0]*a[0]:   print("Obtuse Triangle")
    else:   print("Aute Triangle")
else:   print("Not Triangle")