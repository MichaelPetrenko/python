# Задание №2

number = 46275 # abcde

e = number % 10
d = (number // 10) % 10
c = (number // 100) % 10
b = (number // 1000) % 10
a = (number // 10000) % 10

result = (d ** e * c) / (a - b)
print("Результат вычислений : ", result)