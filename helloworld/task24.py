# Задание №1

# Есть последовательность
# my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# Напишите рекурсивную функцию, которая выведет все элементы от первого до последнего и в конце отобразит
# сообщение Конец списка, если выводить больше нечего. Циклы использовать запрещено

def recursive_print(l):
    if len(l) == 0:
        print("Конец списка")
        return
    else:
        print(l.pop())
        recursive_print(l)

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
recursive_print(my_list)