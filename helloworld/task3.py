# Задание №1

firstSide = float(input("Пожалуйста, введите длину первой стороны прямоугольника: "))
secondSide = float(input("Пожалуйста, введите длину второй стороны прямоугольника: "))

rectangleArea = firstSide * secondSide
rectanglePerimeter = 2 * (firstSide + secondSide)

print("Площадь прямоугольника - ", rectangleArea, ", периметр прямоугольника - ", rectanglePerimeter, sep="")