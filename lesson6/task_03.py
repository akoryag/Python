"""
Задание 3.
Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку __str__
__str__(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.
"""


class Worker:

    def __init__(self, name, surname, position, salary, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._inc = {"salary": salary, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, salary, bonus):
        super().__init__(name, surname, position, salary, bonus)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_toatal_inc(self):
        return self._inc['salary'] + self._inc['bonus']

    def __str__(self):
        return f"Сотрудник: {self.get_full_name()}\nПозиция: {self.position}\nДоход: {self.get_toatal_inc()}"


pos_obj = Position('Алексей', 'Корягин', 'System Engineer', 100, 80)
print(pos_obj.get_full_name(), pos_obj.get_toatal_inc())
print(pos_obj)
