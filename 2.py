import math
a,b,c=int(input()),int(input()),int(input())

if a!=0:
    x1 = ((-b)+(math.sqrt(b*b-4*a*c)))/(2*a)
    x2 = ((-b)-(math.sqrt(b*b-4*a*c)))/(2*a)
    print ("%.1f\n%.1f" % (x1,x2))
else :
    x1 = (-c)/b
    print ("%.1f\n%.1f" % (x1,x1))