IN = [int(i) for i in input().split(" ")]

def get(a, b, c):
    if  a>0 and b>0 and c>0 and a+b>c and a+c>b and b+c>a :
        if  a == b == c :                   return 2
        elif a == b or a == c or b == c :   return 3
        else:                               return 4
    else:   return 1

print(get(IN[0],IN[1],IN[2])) 