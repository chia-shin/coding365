IN = [int(i) for (i) in (input().split())]

def tri(a, b, c):
    if a>0 and b>0 and c>0 and a+b>c and a+c>b and b+c>a:
        if a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:    return 1
        elif a*a+b*b<c*c or a*a+c*c<b*b or b*b+c*c<a*a:     return 2
        else:   return 3
    else:   return 0

ans = tri(IN[0],IN[1],IN[2])

if ans==0:      print("Not Triangle")
elif ans==1:    print("Right Triangle")
elif ans==2:    print("Obtuse Triangle")
elif ans==3:    print("Acute Triangle")