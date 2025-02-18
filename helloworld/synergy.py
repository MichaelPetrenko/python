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