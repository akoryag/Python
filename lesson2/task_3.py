"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""
month_list = range(1, 12)
month_number = int(input("Введите номер месяца от 1 до 12: "))
season_list = ['Зима', 'Весна', 'Лето', 'Осень']
season_dict = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}
if month_number not in month_list:
    print("Номер не соответсвтует диапазону от 1 до 12")
else:
    if month_number in range(9, 11):
        print(f'Результат через список: {season_list[3]}')
        print(f'Результат через словарь: {season_dict.get(4)}')
    elif month_number in range(6, 8):
        print(f'Результат через список: {season_list[2]}')
        print(f'Результат через словарь: {season_dict.get(3)}')
    elif month_number in range(3, 5):
        print(f'Результат через список: {season_list[1]}')
        print(f'Результат через словарь: {season_dict.get(2)}')
    else:
        print(f'Результат через список: {season_list[0]}')
        print(f'Результат через словарь: {season_dict.get(1)}')
