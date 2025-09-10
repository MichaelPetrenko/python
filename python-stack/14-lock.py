import threading

# Общий ресурс
counter = 0

# Создаём блокировку
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        # Захватываем блокировку
        lock.acquire()
        counter += 1
        # Освобождаем блокировку
        lock.release()

# Создаём и запускаем два потока
thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=increment)
thread1.start()
thread2.start()

# Ожидаем завершения обоих потоков
thread1.join()
thread2.join()

# Выводим значение счетчика
print("counter = ", counter)