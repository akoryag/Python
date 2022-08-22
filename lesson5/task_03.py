"""
4)	Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

translate_list = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре"
}

conv_rows = []
with open("task_03.txt") as i:
    for row in i:
        name, value = row.split(' - ')
        conv_rows.append(f'{translate_list[name]} - {value}')
with open('task_03_ru.txt', 'w') as o:
    o.writelines(conv_rows)
