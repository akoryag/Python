"""
Поработайте с переменными, создайте несколько, выведите на экран.
Запросите у пользователя некоторые числа и строки и сохраните в переменные, затем выведите на экран
"""

user_name = 'test boy'
user_message = 'empty box'
count = 1

print(f'({count}) Привет! Я {user_name}. Моё сообщение "{user_message}"')

user_name = input('Введите свое имя: ')
user_message = input('Введите свое сообщение: ')
count = int(input("Введите номер: "))

print(f'({count}) Привет {user_name}! Принимаю сообщение "{user_message}"')
