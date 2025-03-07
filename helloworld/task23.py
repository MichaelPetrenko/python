# Задание №1

# Сложение матриц

import random

def print_list(t, name):
    print(f"{name} : ")
    print("----------------------")
    for i in t:
        print(*i)

matrix_width = int(input("Введите ширину матриц : "))
matrix_height = int(input("Введите высоту матриц : "))

matrix_1 = [[random.randint(-150, 150) for i in range(matrix_width)] for i in range(matrix_height)]
matrix_2 = [[random.randint(-150, 150) for i in range(matrix_width)] for i in range(matrix_height)]
matrix_res = [[0 for i in range(matrix_width)] for i in range(matrix_height)]

for i in range(matrix_height):
    for j in range(matrix_width):
        matrix_res[i][j] = matrix_1[i][j] + matrix_2[i][j]

print_list(matrix_1, "Первая исходная матрица")
print_list(matrix_2, "Вторая исходная матрица")
print_list(matrix_res, "Результат сложения матриц")