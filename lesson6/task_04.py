"""
Задание 4.
Реализуйте базовый класс Car. У данного класса должны быть следующие публичные атрибуты:
speed, color, name, is_police (булево).
А также публичные методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс публичный метод show_speed,
который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"Машина {self.name} поехала"

    def stop(self):
        return f"Машина {self.name} остановилась"

    def turn(self, direction):
        return f"Машина {self.name} повернула {direction}"

    def show_speed(self):
        return f"{self.name}: {self.speed} км/ч"


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'Внимание: Автомобиль {self.name} превысил скорость на {self.speed - 60} км/ч'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'Внимание: Автомобиль {self.name} превысил скорость на {self.speed - 40} км/ч'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'Автомобиль {self.name} является полицейским'
        else:
            return f'Автомобиль {self.name} не является полицейским'

vaz = TownCar(68, 'Красная', 'Lada', False)
ford = PoliceCar(112, 'Белый', 'Ford', True)
nissan = SportCar(99, 'Черный', 'Nissan', False)
gaz = WorkCar(58, 'Белый', 'Газель', False)


print(f'{ford.go()} со скоростью {ford.show_speed()}')
print(f'{ford.name} цвета {ford.color}')
print(f'Когда {vaz.turn("Налево")}, то {ford.stop()}')
print(ford.turn("назад"))
print(f'{nissan.name} полицейская машина? {nissan.is_police}')
print(f'{ford.name} полицейская машина? {ford.is_police}')

print(nissan.show_speed())
print(vaz.show_speed())
print(ford.police())
print(ford.show_speed())