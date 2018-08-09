a = [int(i) for (i) in (input().split())]

avg = (a[0]+a[1]+a[2]+a[3]+a[4])/5.0
dif = ((a[0]-avg)**2 + (a[1]-avg)**2 + (a[2]-avg)**2 + (a[3]-avg)**2 + (a[4]-avg)**2) / 5.0
sta = dif**0.5

avg, dif, sta = int(avg*100)/100.0, int(dif*100)/100.0, int(sta*100)/100.0

print ("%.2f\n%.2f\n%.2f" % (avg,dif,abs(sta)))