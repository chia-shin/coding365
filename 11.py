import math
a=[]
for i in range(0,6):    a.append(int(input()))

ans = a[1]-a[0]
		
if a[2]>a[1]:		
    ans = ((a[1]-a[0])+(a[3]-a[2]))
elif a[3]>a[1]:	
    ans = (a[3]-a[0])
	
if(a[4]>a[1] and a[4]>a[3]):	
    ans = ans + (a[5]-a[4])
elif(a[5]>a[1] and a[5]>a[3]):
    if (a[1]>=a[3]):	
        ans = ans + (a[5]-a[1])
    else:	
        ans = ans + (a[5]-a[3])

print(ans)
