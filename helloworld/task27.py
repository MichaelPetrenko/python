# Задание №1

# Создайте класс Касса, который хранит текущее количество денег в кассе, у него есть методы:

# top_up(X) - пополнить на X
# count_1000() - выводит сколько целых тысяч осталось в кассе
# take_away(X) - забрать X из кассы, либо выкинуть ошибку, что не достаточно денег

class Cashbox(object):
    _amount = 0

    def __init__(self, amount_value):
        self._amount = amount_value

    def top_up(self, x):
        self._amount += x
        print('Текущее значение :', self._amount)

    def count_1000(self):
        return self._amount // 1000

    def take_away(self, x):
        if x > self._amount:
            print('Недостаточно денег в кассе!')
        else:
            self._amount -= x
            print('Текущее значение :', self._amount)

cashbox = Cashbox(100)
cashbox.top_up(5000)
cashbox.top_up(200)
print(f'В кассе {cashbox.count_1000()} тысяч')
cashbox.take_away(3000)
cashbox.take_away(6000) # Недостаточно денег