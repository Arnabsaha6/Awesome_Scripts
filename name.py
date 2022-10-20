print("Hello World")
echo zcmp

#Prime Number
import math

def primeCheck(x):
sta = 1
for i in range(2,int(math.sqrt(x))+1): # range[2,sqrt(num)]
if(x%i==0):
sta=0
print("Not Prime")
break
else:
continue
if(sta==1):
print("Prime")
return sta

num = int(input("Enter the number: "))
ret = primeCheck(num)
