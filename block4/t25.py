n = int(input("Введите двузначное число: "))

a = n // 10
b = n % 10

S = a + b

if 10 <= S < 100:
    print(f'Да , сумма цифр {S} являеться двузначным числом.')
else:
    print(f'Нет , сумма цифр {S} не являеться двузначным числом.')


if n > S:
    print(f'число {n} больше сумме цифр {S} ')
else:
    print(f'число {n} меньше или равно сумме своих цифр {S} ')
