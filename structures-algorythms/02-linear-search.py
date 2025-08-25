def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1 # Если элемент не найден

# Пример использования:
arr = [10, 20, 30, 40, 50]
target = 30
print("Индекс элемента:", linear_search(arr, target))