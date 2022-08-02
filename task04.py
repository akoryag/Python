"""
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""
digits = int(input("Введите целое положительное число: "))

remainder = digits % 10
digits = digits // 10
while digits > 0:
    if digits % 10 > remainder:
        remainder = digits % 10
    digits = digits // 10
print("Самая большая цифра: ", remainder)