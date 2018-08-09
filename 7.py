A, B, C = int(input()), int(input()), int(input())

SumA = A*380
if A>30:    SumA = SumA*0.8
elif A>20:  SumA = SumA*0.85
elif A>10:  SumA = SumA*0.9

SumB = B*1200
if B>30:    SumB = SumB*0.8
elif B>20:  SumB = SumB*0.85
elif B>10:  SumB = SumB*0.95

SumC = C*180
if C>30:    SumC = SumC*0.7
elif C>20:  SumC = SumC*0.8
elif C>10:  SumC = SumC*0.85
    
print(int(SumA + SumB + SumC))