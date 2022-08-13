"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль (try except).

"""


def division(first_elm, second_elm):
    try:
        return first_elm / second_elm
    except ZeroDivisionError:
        return "Пытаетесь делить на 0!"


try:
    first_elm = int(input("Введите первое число: "))
    second_elm = int(input("Введите второе число: "))
    print(division(first_elm, second_elm))
except ValueError:
    print("Пожалуйста, вводите только числа")
