# Задание №1

# Создайте функцию, которая принимает в качестве параметра - натуральное целое число.
# Данная функция находит факториал полученного числа
# Например, факториал числа 3 это число 6.

# Теперь создайте список факториалов чисел от получившегося ранее факториала 6, до 1.
# В итоге, на вход программа получает например число 3, возвращает число 6 (факториал числа 3) и вам нужно сделать
# список из факториалов числа 6 в убывающем порядке. Находим факториал числа 6 - это 720, затем от числа 5 - это 120 и
# так далее вплоть до 1

# То есть, результирующий список будет выглядеть в нашем примере так:
# [720, 120, 24, 6, 2, 1]

def get_factorial(number):
    factorial = 1
    while number > 1:
        factorial *= number
        number -= 1

    return factorial


initial_number = int(input("Введите натуральное число для определения факториала : "))
factorial_number = get_factorial(initial_number)
result_list = list()

for i in range(factorial_number, 0, -1):
    result_list.append(get_factorial(i))

print(result_list)