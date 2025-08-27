# timeit
import timeit

def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp
    return arr

s = """def swap_test():
    arr = [1, 2, 3, 4]
    print(swap(arr, 1, 2));
"""

print(timeit.timeit(stmt=s, number=100)); # number - число запусков функции