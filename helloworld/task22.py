# Задание №2

# Словарь с информацией о питомце

import collections

pets = dict()

def get_age_suffix(age):
    if age % 10 == 1 and age % 100 != 11:
        # 1 год, 21 год, 31 год, но 11 лет - исключение
        return 'год'
    elif 2 <= age % 10 <= 4 and (age % 100 < 10 or age % 100 >= 20):
        # 22 года, 34 года, 2 года, 4 года, но 12 лет, 14 лет - исключение
        return 'года'
    else:
        # 5 лет, 25 лет, 39 лет, остальные случаи
        return 'лет'

def create():
    pet_name_key = input("Введите имя питомца : ")
    pet_type = input("Введите вид питомца : ")
    pet_age = int(input("Введите возраст питомца : "))
    owner_name = input("Введите имя владельца : ")
    last_index = 0
    if len(pets.keys()) != 0:
        last_index = collections.deque(pets.keys(), maxlen = 1)[0]

    pets[last_index + 1] = {
        pet_name_key: {
            'Вид питомца': pet_type,
            'Возраст питомца': pet_age,
            'Имя владельца': owner_name
        }
    }

def read(pet_id):
    if is_pet_exists(pet_id):

        pet_information = pets[pet_id]
        for pet_name_key in pet_information.keys():
            pet_type = pet_information[pet_name_key]['Вид питомца']
            pet_age = pet_information[pet_name_key]['Возраст питомца']
            owner_name = pet_information[pet_name_key]['Имя владельца']

            age_suffix = get_age_suffix(pet_age)
            output_string = f'{pet_id}: Это {pet_type} по кличке "{pet_name_key}". Возраст питомца: {pet_age} {age_suffix}. Имя владельца: {owner_name}.'
            print(output_string)
    else:
        print("Питомец с таким ID не существует!")

def update(pet_id):
    if is_pet_exists(pet_id):

        pet_name_key = input("Введите имя питомца : ")
        pet_type = input("Введите вид питомца : ")
        pet_age = int(input("Введите возраст питомца : "))
        owner_name = input("Введите имя владельца : ")

        pets[pet_id] = {
            pet_name_key: {
                'Вид питомца': pet_type,
                'Возраст питомца': pet_age,
                'Имя владельца': owner_name
            }
        }
    else:
        print("Питомец с таким ID не существует!")

def delete(pet_id):
    if is_pet_exists(pet_id):
        pets.pop(pet_id)
    else:
        print("Питомец с таким ID не существует!")

def is_pet_exists(pet_id):
  return int(pet_id) in pets.keys()

def pets_list():

    print("Текущее состояние базы : ")

    if len(pets.keys()) > 0:
        for k in pets.keys():
            read(k)
    else:
        print("Здесь еще нет ни одной записи.")

command = ""
while command != "stop":
    command = input("Пожалуйста, введите одну из команд: create, read, update, delete, stop : ")
    if command == "create":
        create()
        pets_list()
    elif command == "update":
        update(int(input("Введите айди питомца: ")))
        pets_list()
    elif command == "read":
        read(int(input("Введите айди питомца: ")))
    elif command == "delete":
        delete(int(input("Введите айди питомца: ")))
        pets_list()
    else:
        print("Неизвестная команда")