# Задание №3

minAmount = int(input("Введите минимальную сумму инвестиций : "))
mikeCash = int(input("Количество денег у Майка : "))
ivanCash = int(input("Количество денег у Ивана : "))

if (mikeCash >= minAmount) and (ivanCash >= minAmount):
    print("2")
elif (mikeCash >= minAmount) and (ivanCash < minAmount):
    print("Mike")
elif (mikeCash < minAmount) and (ivanCash >= minAmount):
    print("Ivan")
elif (mikeCash + ivanCash) >= minAmount:
    print("1")
else:
    print("0")