# Задание №2

aCounter = 0
eCounter = 0
iCounter = 0
oCounter = 0
uCounter = 0

wovelsCounter = 0
consonantsCounter = 0

word = input("Введите английское слово : ")

aCounter += word.count("a")
eCounter += word.count("e")
iCounter += word.count("i")
oCounter += word.count("o")
uCounter += word.count("u")

wovelsCounter = aCounter + eCounter + iCounter + oCounter + uCounter
consonantsCounter = len(word) - wovelsCounter

print("Количество согласных букв :", consonantsCounter)
print("Количество гласных букв :", wovelsCounter)
print("Количество букв a :", aCounter)
print("Количество букв e :", eCounter)
print("Количество букв i :", iCounter)
print("Количество букв o :", oCounter)
print("Количество букв u :", uCounter)

if (aCounter == 0) or (eCounter == 0) or (iCounter == 0) or (oCounter == 0) or (uCounter ==0):
    print("False")