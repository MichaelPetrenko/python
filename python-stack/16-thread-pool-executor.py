from concurrent.futures import ThreadPoolExecutor

# Создание ThreadPoolExecutor с 5 потоками
executor = ThreadPoolExecutor(max_workers=5)

# Создание ThreadPoolExecutor с количеством потоков по умолчанию
executor = ThreadPoolExecutor()

def task(x):
    return x*x

# Планирование выполнения задачи
future = executor.submit(task, 5)

# Получение результата задачи
res = future.result()
print(res) # 25