a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
otvet = a / b / c
print(f"Ваш ответ: {otvet}")

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
otvet = a * b / c
print(f"Ваш ответ: {otvet}")

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
otvet = a / b * c
print(f"Ваш ответ: {otvet}")

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
otvet = a+b/c
print(f"Ваш ответ: {otvet}")

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
otvet = (a+b) / c
print(f"Ваш ответ: {otvet}")

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
otvet = a+b/b+c
print(f"Ваш ответ: {otvet}")

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
otvet = (a+b) / (b+c)
print(f"Ваш ответ: {otvet}")

from math import sin, radians
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
otvet = a / round(sin(radians(b)), 2)
print(f"Ваш ответ: {otvet}")

from math import sin, radians
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
x = int(input("Введите третье число: "))
otvet = 1/2 * a * b * round(sin(radians(x)), 2)
print(f"Ваш ответ: {otvet}")

from math import cos, radians
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
otvet = (2 * b * c * round(cos(radians(b)), 2)) / (b+c)
print(f"Ваш ответ: {otvet}")

