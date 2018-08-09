inu,outu,sta,inm,outm = int(input()),int(input()),int(input()),int(input()),int(input())

a = inu*0.08+outu*0.139+sta*0.135+inm*1.128+outm*1.483
b = inu*0.07+outu*0.130+sta*0.121+inm*1.128+outm*1.483
c = inu*0.06+outu*0.108+sta*0.101+inm*1.128+outm*1.483

if  a<183:  a=183
if  b<383:  b=383
if  c<983:  c=983

if a<b and a<c:     print("183\n%d"% int(a))
elif b<a and b<c:   print("383\n%d"% int(b))
else:               print("983\n%d"% int(c))