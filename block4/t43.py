a = int(input("Введите число а: "))
b = int(input("Введите число б: "))

if a % b == 0:
    print("Да, одно из чисел является делителем другого")
else:
    print('Нет, ни одно из чисел не является делителем другого')

if b % a == 0:
    print("Да, одно из чиселявляется делителем другого")
else:
    print('Нет, ни одно из чисел не является делителем другого')
