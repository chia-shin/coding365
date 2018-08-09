a, b, c = float(input()), float(input()), float(input())

if (b*b-4*a*c)>=0:
    if a==0:
        x1 = (c*-1)/b
        print ("%.1f\n%.1f" % (x1,x1))
    else:
        T = (b*b-4*a*c)**0.5
        x1 = int((-b+T)/(2*a)*10)/10.0
        x2 = int((-b-T)/(2*a)*10)/10.0
        print ("%.1f\n%.1f" % (x1,x2))
else:
    T = ((b*b-4*a*c)*-1)**0.5
    x1 = int(-b/(2*a)*10)/10.0
    x2 = int(T/(2*a)*10)/10.0
    if x2<0:
        x2 = abs(x2)
        print ("%.1f-%.1fi\n%.1f+%.1fi" % (x1,x2,x1,x2))
    else:
        print ("%.1f+%.1fi\n%.1f-%.1fi" % (x1,x2,x1,x2))