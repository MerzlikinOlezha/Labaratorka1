import time
a=int(input("Введите первое число: "))
b=int(input("Введите второе число: "))
a=a+b
b=b-a
b=-b
a=a-b
print("меняем местами")
print("первое число: " + str(a))
print("второе число: " + str(b))
time.sleep(100000)
