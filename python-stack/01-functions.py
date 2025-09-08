# Определения простой функции в Python

def my_print():
    print('Hello world')

# Функции с необязательными аргументами

def foo(name='Мир', age=None):
    if age is not None:
        print(f"Привет, {name}! Тебе {age} лет!")
    else:
        print(f"Привет, {name}!")

my_print()
foo("Alice")
foo()
foo("Alice", 7)

# Функция может принимать другие функции или методы

# def ex_filter_func(filter_):
#     employees = ["Bob", "Alan", "Dylan"]
#     return [
#         employee
#         for employee in employees
#             if filter_(employee) 
#     ]

# ex_filter_func(
#     lambda x: x["Age"] > 15
# )

# Пример использования лямбда-функции

mysum = lambda a, b: a + b
print(mysum(5, 3)) # Вывод: 8

# Создание lambda-функции для проверки, является ли число четным
even_number = lambda x: x % 2 == 0
print(even_number (4)) # Вывод: True

# Создание lambda-функции для умножения числа на само себя
square = lambda x: x * x
print(square(4)) # 16

def my_print_from_func(func):
    if callable(func):
        print(func())
    else:
        print("func is not callable")

def hello_str(): return "Hello"
my_print_from_func(hello_str)