"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open('task_05.txt', 'w', encoding='utf-8') as f:
    my_digits = input('Числа через пробел: ')
    f.write(my_digits)
with open('task_05.txt', 'r', encoding='utf-8') as r:
    my_list = r.read().split()
    print(f'Сумма чисел = {sum(map(int, my_list))}')