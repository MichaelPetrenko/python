# Факториал
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Пример использования:
print(factorial(5)) # Вывод: 120

# Числа Фибоначчи
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Пример использования:
print(fibonacci(6)) # Вывод: 8

# Разворот строки
def reverse_string(s):
    if len(s) <= 1:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])

print(reverse_string("asdf"))

