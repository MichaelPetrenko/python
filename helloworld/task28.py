# Задание №2

# Создайте класс Черепашка, который хранит позиции x и y черепашки, а также s - количество клеточек, на которое она
# перемещается за ход

# у этого класс есть методы:

# go_up() - увеличивает y на s
# go_down() - уменьшает y на s
# go_left() - уменьшает x на s
# go_right() - увеличивает x на s
# evolve() - увеличивает s на 1
# degrade() - уменьшает s на 1 или выкидывает ошибку, когда s может стать ≤ 0
# count_moves(x2, y2) - возвращает минимальное количество действий, за которое черепашка сможет добраться до x2 y2
# от текущей позиции

class Turtle(object):
    _x = 0
    _y = 0
    _s = 0

    def __init__(self, x, y, s):
        self._x = x
        self._y = y
        self._s = s

    def print_current_position(self):
        print(f'Текущая позиция: x = {self._x}, y = {self._y}')

    def go_up(self):
        self._y += self._s

    def go_down(self):
        self._y -= self._s

    def go_right(self):
        self._x += self._s

    def go_left(self):
        self._x -= self._s

    def evolve(self):
        self._s += 1

    def degrade(self):
        if self._s <= 1:
            raise ValueError('Скорость черепашки не может быть нулевой!')
        self._s -= 1

    def count_moves(self, x2, y2):
        distance_x = abs(x2 - self._x)
        distance_y = abs(y2 - self._y)
        steps_count = 0

        steps_count += distance_x // self._s
        steps_count += distance_y // self._s

        if distance_x % self._s != 0:
            steps_count += 1
        if distance_y % self._s != 0:
            steps_count += 1

        return steps_count

donatello = Turtle(0, 0, 3)
donatello.print_current_position()

donatello.degrade()
donatello.go_up()
donatello.go_left()
donatello.print_current_position()

donatello.evolve()
donatello.go_down()
donatello.go_right()
donatello.print_current_position()

count = donatello.count_moves(100, 100)
print("Количество действий : ", count)