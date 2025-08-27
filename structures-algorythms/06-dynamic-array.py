class DynamicArray:
    def __init__(self):
        self.array = []
        self.size = 0

    def append(self, value):
        self.array.append(value)
        self.size += 1

    def __getitem__(self, index):
        return self.array[index]

    def __len__(self):
        return self.size

# Пример использования:
dynamic_array = DynamicArray()
dynamic_array.append(10)
dynamic_array.append(20)
print(dynamic_array[1]) # Вывод второго элемента
print(len(dynamic_array)) # Вывод размера массива