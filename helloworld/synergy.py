print("Hello world!")
print("abcd", "sdsds", sep="-")

print(input())

# Переменные
x = 8
x = 9
print("x = ", x)

# Арифметические операции
a = 5
a = 5 + 6
b = 8 - 2
c = 4 * 5
d = 7 // 5  # Челочисленное деление
e = 7 % 5   # Остаток от деления
f = 2 ** 5  # 2 в степени 5

print(a, b, c, d, e, f)

a = 5
a = a + 10
a += 10
print(a)

# Нужно привести типы
a = input()  # a = 4
print(a * 5) # 44444

a = int(input())  # a = 4
print(a * 5) # 20

a = int(input())
b = int(input())
print (a * b)

# Разбить строку по разделителю
a, b = input().split() # Разделение по пробелу
print(a)
# 3 4 5
# ['3', '4', '5']

# Конвертировать в int числа, которые вводим
a, b = map(int, input().split())
print(a * b)

# или проще
a, b = input().split()
a = int(a)
b = int(b)
print(a * b)

# Ограничения в вычислениях
d = 242195195198198189198189198198418481815182529516518651816518965186511845 * 11591951185115151515159911191951591591591159191911
print(d)

# Вещественные числа
a = 10
b = 3
# / - вещественное деление
# // - целое деление
# % - остаток от деления
print(a / b)

# Точность
a = 22 / 7 # 3.142857142857143
b = a ** 100
c = 22 ** 100
d = 7 ** 100
res = b / c * d
print(res) # 0.999999999999998, а не 1! Накопилась погрешность

# Деление на 0
a = 22 / 0 # ZeroDivisionError: division by zero

# Вещественные числа
a = float(input())
print(a) # 4.0

# Логические операторы
a = 5
b = 7

# a < b - логическая операция
print(a <= b) # True
print (a == b)
print (a != b)

a = int(input("Введите первое число : "))
b = int(input("Введите второе число : "))

# Вложенный if
if a < b:
    print("less")
else:
    if a == b:
        print("equal")
    else:
        print("grater")

# Вариант с elif
if a < b:
    print("less")
elif a == b:
    print("equal")
else:
    print("grater")

# И, или - or, and, if not 
cash = int(input("cash : "))
cost = int(input("cost : "))
cassa = int(input("cassa : "))

if (cash >= cost) and ((cash - cost) <= cassa):
    print("Денег хватило")
else:
    print("Денег не хватило")

# Циклы while и for
a = int(input("Input number : "))
cnt = 0
while a >= 0:
    a -= 2
    print("a = ", a)
    cnt += 1
print(cnt)

# Cola
clients = int(input("Clients : "))
cola = int(input("Cola : "))
cnt = 0

while (clients > 0) and (cola >= 0):
    cans = int(input("Cans to buy : "))
    clients -= 1
    if cola >= cans:
        cnt += 1
        cola -= cans

print("Cnt = ", cnt)

# Numbers from 1 to 10
for i in range(1, 11): # 3 параметр - на сколько увеличивать
    print(i)

# Numbers from a to b with step 2
a = int(input("First number : "))
b = int(input("Second number : "))

for i in range(a, b, 2): # 3 параметр - на сколько увеличивать
    print(i)

# range(10) -> range(0, 10, 1)

# else in while
a = 1
while a < 5:
    a += 1
    print(a)
else: # only one time
    print("only one time")

# Увольнение людей в компании
n = int(input("Введите количество людей в компании : "))

for i in range(n):
    salary = int(input("Зарплата : "))
    if (salary % 2 == 0):
        print(i + 1, "уволен")

# Урок 7. Строки
s1 = 'abcde'
s2 = 'abcdef'
print(s2[0])  # Вывести первый символ
print(s2[-1]) # Вывести последний символ - отрицательная индексация
# Поменять таким образом букву в слове не получится

s3 = s1 + s2
print(s3)
print(len(s3)) # длина строки

s4 = 'abcdefghijkl'
# Срез строки
print(s4[0:4:1]) # От первого параметра вкл до второго невкл, шаг
print(s4[5::-1]) # Срез в обратном порядке до начала строки
print(s4[5::1]) # Срез в прямом порядке до конца строки

tmp = [4, 3, 2, 9, 7]
print(tmp[::2]) # Вывести все элементы массива с шагом 2
print(tmp)

tmp = "3 + 8 + 9 + 10"
t = tmp.split(" + ")
print(t)
print(" + ".join(t)) # Склеили обратно

name = "Dima"
print("Hello,", name)
print(f"Hello, {name}") # Форматирование строки
test = f"Hello, {name}"
print(test)

s1 = "sdfkjbhsdf"
print(s1.upper())
print(s1.lower())

print(ord('a')) # Номер символа в таблице ASCII
print(chr(97)) # Обратная функция

# Шифр Цезаря
t = 'abzr'
for c in t:
    code = ord(c) + 3
    if code > 122:
        print(chr(97 + code - 122), end='')
    else:
        print(chr(ord(c) + 3), end='')

# Урок 8. Списки
from os.path import split

a = [3, 4, 9, 1]
print("First element", a[0]) # Обратиться к элементу массива

# В питоне есть отрицательная индексация - можно обращаться к элементам с конца.
print("Last element : ", a[-1]) # Последний элемент
print("Before last element : ", a[-2]) # Предпоследний элемент

a[1] = 12
print(a)

# Добавить элемент в конец списка
a.append(123)
print("вывести массив со скобочками", a) # вывести массив со скобочками
print("Длина списка", len(a))
print("вывести массив без скобочек и разделителей", *a)

# Добавить элемент внутрь массива со сдвигом
a.insert(3, 67)
print(a)

# Удаление последнего элемента в массиве
a.pop()
print(a)

# Удаление элемента по индексу
a.pop(2)
print(a)

# Очистка списка
a.clear()
print(a)

# Развернуть массив
a = [1, 2, 3, 4, 5, 5, 5]
a.reverse()
print(a)

# Посчитать уникальные элементы в массиве
print(a.count(5))

# Создаем массив в цикле
n = int(input("Введите длину массива : "))
res = []
for i in range(n):
    a = int(input(f"Введите {i} элемент массива : "))
    res.append(a)

print(res)

# Создаём массив из строки с пробелами
res = list(map(int, input().split()))
print(res)

# Банкомат - i = индекс
# 10 50 50 100 500 50 1000
tmp = list(map(int, input("введите номиналы банкнот через пробел : ").split()))
res = []
for i in range(0, len(tmp)):
    if tmp[i] != 50:
        res.append(tmp[i])

print(res)

# Банкомат - i = значение
# 10 50 50 100 500 50 1000
n = int(input("Введите количество банкнот : "))
tmp = list(map(int, input("введите номиналы банкнот через пробел : ").split()))
res = []
for i in tmp:
    if i != 50:
        res.append(i)

print(res)

# Создание списков
a = [3 for i in range(5)] # создать массив из 5 элементов a
print(a)

# Изменяемость и неизменяемость типов (примитивы, объекты)
# int, float - неизменяемые типы (примитив)
a = 5
b = a
a = 7
print(b) # b = 5

# string - неизменяемый тип (примитив)
a = 'asd'
b = a
a = 'fddg'
print(b)

# list - ссылочный тип
a = [5]
b = a
a[0] = 6
print(b) # [6]

# Урок 9. Множества (set)

# Множества (Set) - структура данных, которая хранит уникальные объекты
tmp = set()
tmp2 = {2, 3, 3, 4} # Создание множества
tmp2.add(7)
tmp2.remove(7) # Вызовет ошибку при отсутствии элемента
tmp2.discard(7) # Не вызовет ошибку при отсутствии элемента
print(tmp2)

# Промокоды
n = int(input("Введите количество промокодов : "))
used = set()
for i in range(n):
    promo = input("Введите промокод : ")
    if promo in used:
        print("Sorry, already used")
    else:
        used.add(promo)
print("Использовано промокодов : ", len(used))
used.clear() # Очистить множество

# Компании, люди с именами - уволить сотрудников с похожими именами
company1 = int(input("Input number of peoples in company 1 : "))
company_names1 = [] # Пустой список
for i in range(company1):
    name = input("Input name : ")
    company_names1.append(name)

company2 = int(input("Input number of peoples in company 2 : "))
company_names2 = []
for i in range(company2):
    name = input("Input name : ")
    company_names2.append(name)

uniq1 = set(company_names1)
uniq2 = set(company_names2)
print("Unique names : ", uniq1.union(uniq2)) # Объединение множеств
print("Пересечение множеств : ", uniq1.intersection(uniq2)) # Пересечение множеств

# set - изменяемый тип, неизменяемый тип - frozenset - нельзя модифицирующие операции, добавлять элементы

tmp = {1, 2, 3, 9, 0}
for el in tmp:
    print(el) # не в изначальном порядке

# Урок 10. Словари (Map в Java, Dictionary) - набор ключей и значений. Ключ должен быть уникальным
bank = {'anton': 10, 'dima': 20, 'petya': 4}
print(bank['anton'])
print(bank.get('anton')) # Так тоже работает

bank['anton'] = 159
print(bank)

# Банк
bank = dict()
n = int(input("Please enter number : "))

for i in range(n):
    req = input("Enter 'create' or 'add' : ")
    if req == "create":
        key = input("Enter key : ")
        bank[key] = 0
    elif req == "add":
        key = input("Enter key : ")
        amount = int(input("Enter amount : "))
        if key in bank.keys():
            bank[key] += amount
        else:
            print("Sorry, no such key")
    else:
        print("Sorry, bad request")

print(bank)

# Методы словарей
tmp = {'k1': 1, 'k2': 10, 'qwerty': 5}
print(tmp.keys()) # Набор ключей
print(tmp.values()) # Набор значений
print(tmp.items()) # Map.Entry из Java - пары ключ-значение

# Итерация по словарям
for k in tmp.keys():
    print(k)

tmp.pop('k1') # Удаление значения из словаря
print(tmp)

# Ключом словаря может быть любой неизменяемый тип (примитив).
# В Java ключом может быть любой объект

# Урок 11. Функции

def chet(a):
    return a % 2 == 0

print(chet(23))
print(chet(24))

def tmp(name):
    print(f"Hello, {name}!")

tmp("Michael")

def vis(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

print(vis(2024))
print(vis(2025))

def nechet(n):
    return n % 2 != 0

def res(l):
    for el in l:
        if nechet(el):
            print(el)

tmp = [1, 2, 234, 5, 457, 5, 68, 69]
res(tmp)

def new_year():
    print("Happy new year!")

def birthday():
    name = input("Input name : ")
    print(f"Happy Birthday, {name}!")

def march8():
    print("Happy 8th of March!")

n = int(input("Введите количество команд : "))
for i in range(n):
    cm = input("Введите команду : ")
    if cm == "new year":
        new_year()
    elif cm == "birthday":
        birthday()
    elif cm == "8 march":
        march8()
    else:
        print("Неправильная команда")

# Тема 4. Функции
# Урок 12. Сортировки

# Сортировка пузырьком - пузырьковая сортировка
a = [4, 9, 0, 18, 17, 23, 4, 1, 0]
n = len(a)

for i in range(n):
    for j in range (n - 1 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j] # Заменить элементы местами

print(a)

b = [4, 9, 0, 18, 17, 23, 4, 1, 0]
b.sort() # Обычная быстрая сортировка
print()

def cmp(x):
    return x % 10

b.sort(key = cmp) # Сортировка по остатку от деления на 10
print(b)

# SEO
n = 5
sph = [12, 30, 97, 5, 6]
hours = [10, 120, 4, 8, 9]

res = []
for i in range(n):
    r = sph[i] * hours[i]
    res.append(r)

res.sort()
print(res)

# сортировка по произведению первой и второй цифры числа
tmp = [12, 34, 23, 53, 65, 34, 61]

def cmp(x):
    return (x // 10) * (x % 10)

tmp.sort(key=cmp)
print(tmp)

# Максимум из значений
a = 5
b = 8
c = 1
d = -19

print(max(a, b, c, d))
print(min(a, b, c, d))

tmp = [1, 2, 3443, 6, -10]
print(max(tmp))

# Кортежи (tuple) - неизменяемые списки
a = (2, 4, 9, 7)
b = tuple()
print(a.count(2)) # Количество чисел 2

poets = [('Ptushkin', 1203, 1299), ('Cheburashkin', 999, 1201), ("Petrogradskiy", 1931, 1956)]
# poets[0][1] = 1204 - так не получится
poets[0] = ("Ptushkin", 1204, 1299) # Поменять весь кортеж
print(poets)

# Урок 13. Двумерные списки

tmp = [[1, 2, 3], [4, 5], [9, 8, 7]]
print(tmp[1][1])

tmp[1][0] = 9
print(tmp[1][0])

tmp[1] = [4, 9, 0, 3]
print(tmp[1])

tmp.append([6, 9, 2])
print(tmp)

for i in tmp:
    print(*i) # Убрать скобочки и запятые

n = 2
tmp = []
for i in range(n):
    a = list(map(int, input("Введите элементы : ").split()))
    tmp.append(a)
print(tmp) # [[1, 2], [5, 3, 1]]

tmp = [[1 for i in range(3)] for i in range(4)]
print(tmp) # [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]

# Дом x этажей y квартир, нумерация разная на четных и нечетных
def print_list(t):
    for i in t:
        print(*i)
x = int(input("x = "))
y = int(input("y = "))
house = [[0 for i in range(y)] for i in range(x)]
cnt = 1

for i in range(-1, -x -1, -1):
    if i%2 == 1:
        for j in range(y):
            house[i][j] = cnt
            cnt += 1
    else:
        for j in range(-1, -y -1, -1):
            house[i][j] = cnt
            cnt += 1

print_list(house)

# Трёхмерный список
t3 = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print(t3[0][0][0])

# Урок 14. Рекурсия

def test(a, b = 4, c = 9): # Дефолтное значение - для последних элементов
    return a + b + c

print(test(3, 4, 9))
print(test(3, 4))
print(test(3))

# Так как питон интерпретируемый, а не компилируемый, читает строки по очереди - функция должна быть выше её вызова

# Рекурсивная функция
def tmp(x):
    if x < 0:
        return
    print(x)
    tmp(x - 1)

n = 10
tmp(n) # 10 9 8 7 6 5 4 3 2 1 0

def tmp(x):
    if x < 0:
        return
    tmp(x - 1)
    print(x)

n = 10
tmp(n) # 0 1 2 3 4 5 6 7 8 9 10 - раскручивается стэк вызовов функций

# Найти n-ное число Фибоначчи - 0 1 1 2 3 5 8 13 ...
def fib(num):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    res = fib(num - 1) + fib(num - 2)
    return res

print("fib 5 = ", fib(5))
print("fib 6 = ", fib(6))
print("fib 7 = ", fib(7))
print("fib 8 = ", fib(8))

# Глубина рекурсии - import sys - sys.setrecursionlimit(2000) - так как по дефолту около 1000

# Урок 15. ООП

# Класс - шаблон для создания объектов одного и того же типа.
# У него есть свойства класса - атрибуты объектов, которые с помощью этого класса создаются, и методы.
# Методы нужны для описания поведения объектов класса

class Human(object):
    name = "Ivan" # Дефолтные значения
    height = 175
    age = 25

    def __init__(self, n, h, a):
        self.name = n
        self.height = h
        self.age = a

    def say_hi(self):
        print(f"Привет! Меня зовут {self.name}, мне {self.age} лет, мой рост - {self.height}")

    def get_older(self):
        self.age += 5

    @staticmethod
    def goodbye():
        print("Goodbye!")

# default_human = Human()
# print(default_human.height)
# default_human.name = "Anton"
# print(default_human.name)

h1 = Human("Anton", 120, 12)
h2 = Human("Dima", 190, 23)
print(h2.name)
h1.say_hi()
h1.get_older()
h1.say_hi()
h2.say_hi()

h2.goodbye()
Human.goodbye()

# Тема 5. Работа с классами, объектами и файлами
# Урок 16. Классы и объекты

class Car(object):
    brand = "Mazda"
    color = "black"
    max_speed = 100
    __password = 1234 # Приватное поле __

    def __init__(self, brand, max_speed):
        self.brand = brand
        self.max_speed = max_speed

    def upgrade(self):
        self.max_speed += 25
        self.__password = 345
        self.__update_password()

    def get_password(self):
        return self.__password

    def __update_password(self):
        self.__password = 234

class Truck(Car):
    max_weight = 10

    def __init__(self, brand, max_speed, max_weight):
        self.brand = brand
        super().__init__(max_speed, max_weight)

    def add(self):
        self.max_weight += 10

nissan = Car("Nissan", 190)
nissan.upgrade()
print(nissan.brand, nissan.max_speed)

gazel = Truck("Gazel", 60, 90)
gazel.upgrade()
gazel.add()
print(gazel.max_speed, gazel.max_weight)

mazda = Car("Mazda", 200)
mazda.upgrade()
print(mazda.get_password())

mazda.__password = 987 # не получится
print(mazda.get_password())
mazda._Car__password = 987 # Получилось? Как рефлексия в джаве
print(mazda.get_password())

# Урок 17. О-нотация, исключения

try:
    print(45 // 0)
except ZeroDivisionError:
    print("Нельзя делить на 0")

t = [1, 2, 5]
try:
    print(t[10])
except ZeroDivisionError:
    print("ZeroDivisionError")
except IndexError:
    print("IndexError")

try:
    print(45 // 0)
except Exception:
    print("Ошибка")
else:
    print("Сюда попадаем, только если нет ошибки")
finally:
    print("Finish")

# Базовые операции - сложение, вычитание, присваивание - О(1)
# Константы отбрасываем

n = int(input())
m = int(input())
a = 1

for i in range(n):
    for j in range(n):
        a += 1 # O (n ^ 2 + m)

# Питон выполняет в секунду 10^6 базовых операций.