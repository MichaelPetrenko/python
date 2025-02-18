# Задание №1

numbersCnt = int(input("Сколько чисел будет введено? : "))
zeroCnt = 0

for i in range(numbersCnt):
    currentNum = int(input("Введите число : "))
    if currentNum == 0:
        zeroCnt += 1

print("Количество введенных чисел, равных нулю : ", zeroCnt)