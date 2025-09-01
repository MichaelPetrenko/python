def simple_hash_function(key, size):
    hash_value = 0
    for char in key:
        hash_value = (hash_value * 31 + ord(char)) % size
    return hash_value

# Пример использования:
key = "example"
size = 10
print("Хеш-индекс:", simple_hash_function(key, size))
# Вывод: индекс в диапазоне от 0 до size-1