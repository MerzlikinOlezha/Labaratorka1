import time
a=float(input("Введите длину первого катета: "))
b=float(input("Введите длину второго катета: "))
c=(a*a+b*b)**0.5
P=a+b+c
S=(a*b)/2
print("Периметр равен " + str(P) + " см")
print("Площадь равна " + str(S) + " см^2")
time.sleep(1000000)

