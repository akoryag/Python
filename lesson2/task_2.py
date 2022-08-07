"""
Задание 2. Для списка реализовать обмен значений соседних элементов,
т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().

Пример:
Введите целые числа через пробел: 1 2 3 4
Результат: 2 1 4 3

Введите целые числа через пробел: 1 2 3
Результат: 2 1 3
"""

list_digits = list(map(int, input("Введите целые числа через пробел: ").split()))
element = 0
for digits in range(int(len(list_digits) / 2)):
    list_digits[element], list_digits[element + 1] = list_digits[element + 1], list_digits[element]
    element += 2
print(" ".join([str(digits) for digits in list_digits]))
