# Задание №1

# В первой строке вводится число N. Далее в N строк вводится N чисел (1 ≤ N ≤ 10000), по одному числу на строке.
# Все числа по модулю не превышают 10e5. Переверните массив чисел. Выведите N чисел - перевернутый массив

quantity = int(input("Введите количество чисел : "))
resultList = []

for i in range(quantity):
    resultList.append(int(input(f"Введите число №{i + 1} : ")))

resultList.reverse()
print("Перевёрнутый массив : ", resultList)