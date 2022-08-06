"""
Задание 1. Создать список и заполнить его элементами различных типов данных.
Реализовать проверку типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

Пример:
для списка [5, "string", 0.15, True, None]
результат

<class 'int'>
<class 'str'>
<class 'float'>
<class 'bool'>
<class 'NoneType'>
"""

var_int = 9
var_str = "Hello world"
var_float = 1.8
var_bool = True
var_err = None
full_list = [var_int, var_str, var_float, var_bool, var_err]
for data in full_list:
    print(f'Значение {data} это {type(data)}')
