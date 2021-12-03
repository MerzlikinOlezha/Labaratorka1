import time
b=float(input("Введите b: " ))
t=float(input("Введите t: " ))
a=float(input("Введите a: " ))
import math
e=math.exp((-b)*t)
sn=math.sin(a*t+b)
m=math.fabs(b*t+a)
y=e*sn-(m**0.5)
q=b*math.sin(a*t*t*math.cos(2*t))-1
print("Результат: y= " + str( y))
print("Результат: s= " + str( q))
time.sleep(1000000)
