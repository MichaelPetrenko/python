# Алгоритм замены элементов в массиве
def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp
    return arr

arr = [7, 5, 2, 9]
a = 0
b = 2
swap(arr, a, b)

print(arr) # 2 5 7 9