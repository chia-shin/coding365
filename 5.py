import math
a = [int(i) for (i) in (input().split())]

avg = (a[0]+a[1]+a[2]+a[3]+a[4])/5.0
dif = ((a[0]-avg)*(a[0]-avg) + (a[1]-avg)*(a[1]-avg) + (a[2]-avg)*(a[2]-avg) + (a[3]-avg)*(a[3]-avg) + (a[4]-avg)*(a[4]-avg)) / 5.0
sta = math.sqrt(dif)

avg, dif, sta = int(avg*100)/100.0, int(dif*100)/100.0, int(sta*100)/100.0

print ("%.2f\n%.2f\n%.2f" % (avg,dif,abs(sta)))