# Задание №3

a = int(input("Введите число a : "))
b = int(input("Введите число b : "))
resultString = ""

if a % 2 != 0:
    a += 1

for i in range(a, b + 1, 2):
    resultString += str(i) + " "

print(resultString)