# Задание №2

# Вводятся два списка чисел, которые могут содержать до 100000 чисел каждый. Все числа каждого списка находятся на
# отдельной строке. Выведите, сколько чисел содержится одновременно как в первом списке, так и во втором.

first_set = set(map(int, input("Введите числа первой строки через пробел : ").split()))
second_set = set(map(int, input("Введите числа второй строки через пробел : ").split()))

intersect_elements = first_set.intersection(second_set)
print(f"Одновременно в первом и втором списке : {len(intersect_elements)} чисел")