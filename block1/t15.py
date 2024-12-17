# -1 / x в квадрате
x = int(input("Введите число: "))
otvet = (-1 / x * x)
print(f"Ваш ответ: {otvet}")

# a / bc
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
otvet = round(a / b * c)
print(f"Ваш ответ: {otvet}")

# a / b * c
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
otvet = round((a/b) * c)
print(f"Ваш ответ: {otvet}")

# a + b / 2
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
otvet = round(a+b / 2)
print(f"Ваш ответ: {otvet}")

# 5,45 * a+2b/2-a
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
otvet = 5.45 * a+2*b / 2-a
print(f"Ваш ответ: {otvet}")

# -b + в корне b в квадрате - 4 a * c / 2a
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
otvet = -b + ((b*b-4*a*c) ** 0.5) / 2 * a
print(f"Ваш ответ: {otvet}")

# -b + 1/a / 2 / c
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
otvet = -b + (1/a) / 2/c
print(f"Ваш ответ: {otvet}")

# 1 / 1 + a+ b /2
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
otvet = 1 / 1 + a+b / 2
print(f"Ваш ответ: {otvet}")

print(1 / (1+ 1/ (2+ (1/2 + (3/5)))))

m = int(input("Введите первое число: "))
n = int(input("Введите второе число: "))
otvet = round((2 ** m) ** n, 2)
print(f"Ваш ответ: {otvet}")
