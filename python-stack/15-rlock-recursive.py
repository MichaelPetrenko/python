import threading

# Общий ресурс
counter = 0

# Создаём рекурсивную блокировку
lock = threading.RLock()

def increment():
    global counter
    with lock:
        counter += 1
        # Вложенное захватывание RLock
        with lock:
            counter += 1

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