# Задание №2

# В первую строчку вводится число N (1 ≤ N ≤ 100 000). В следующую строку через пробел вводятся N чисел
# (1 ≤ Ai ≤ 10e9). Вам требуется написать метод, который получает на вход массив и изменяет его таким образом,
# чтобы на первом месте стоял последний элемент, на втором - первый, на третьем - второй и т. д.
# Выведите N чисел - измененный массив.

def reverse_list(numbers: list) -> list:
    last_element = numbers.pop()
    numbers.insert(0, last_element)
    return numbers

list_length = int(input("Введите длину массива чисел : "))
numbers_string = input(f"Введите {list_length} чисел через пробел : ")
numbers_list = list(map(int, numbers_string.split()))

if list_length != len(numbers_list):
    print("Введено неверное количество чисел!")
else:
    print(reverse_list(numbers_list))