# Задание №2

x = int(input("Введите натуральное число : "))
dividersCnt = 0

for i in range(1, x + 1):
	if x % i == 0:
		print(i)
		dividersCnt += 1
 
print("Количество делителей : ", dividersCnt)