import math
num1, num2 = int(input()), int(input())

Sum = abs(int((num1 + num2)*100)/100.0)
dif = abs(int((num1 - num2)*100)/100.0)
Pro = abs(int((num1 * num2)*100)/100.0)
Quo = abs(int((num1 / num2)*100)/100.0)

print ("Sum:%.2f\nDifference:%.2f\nProduct:%.2f\nQuotient:%.2f" % (Sum,dif,Pro,Quo))