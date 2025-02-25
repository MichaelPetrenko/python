# Задание №3

# Во входную строку водится последовательность чисел через пробел. Для каждого числа выведите слово ”YES” (в отдельной
# строке), если это число ранее встречалось в последовательности или ”NO”, если не встречалось.

numbers = list(map(int, input("Введите числа в строку через пробел : ").split()))
uniq_numbers = set()

for i in numbers:

    if i in uniq_numbers:
        print(f"{i} : YES")
    else:
        print(f"{i} : NO")

    uniq_numbers.add(i)