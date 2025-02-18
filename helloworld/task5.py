number = int(input("Введите число : "))

if number == 0:
    print("Нулевое число")
else:
    if number > 0:
        sign = "Положительное"
    else:
        sign = "Отрицательное"
    
    if number % 2 == 0:
        parity = "четное"
    else:
        parity = "нечетное"
    
    print(sign, parity, "число")
    if number % 2 != 0:
        print("Число не является четным")