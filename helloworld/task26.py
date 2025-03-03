# Задание №2

# Создайте класс Autobus, который наследуется от класса Transport.
# Дайте аргументу Autobus.seating_capacity() значение по умолчанию 50.
# Используйте переопределение метода.
# Используйте следующий код для родительского класса транспортного средства:
#
# class Transport:
#
#    def __init__(self, name, max_speed, mileage):
#        self.name = name
#        self.max_speed = max_speed
#        self.mileage = mileage
#
#    def seating_capacity(self, capacity):
#        return f"Вместимость одного автобуса {self.name}  {capacity} пассажиров"
#
# Ожидаемый результат вывода:
# Вместимость одного автобуса Renaul Logan: 50 пассажиров

class Transport:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name}  {capacity} пассажиров"

class Autobus(Transport):
    seating_capacity = 50

    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)

    def print_info(self):
        print(f"Название автомобиля: {self.name} Скорость: {self.max_speed} Пробег: {self.mileage}")

    def seating_capacity(self, capacity = 50):
        return super().seating_capacity(capacity = 50)

bus = Autobus("Renault Logan", 120, 134000)
bus.print_info()
print(bus.seating_capacity())