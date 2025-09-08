"""
1. Single Responsibility Principe

Принцип единственной обязанности требует того, чтобы один класс выполнял только одну работу. Таким образом,
если у класса есть более одной работы, он становится зависимым. 
"""

# Wrong - geter and db save
class User1:

    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        pass

    def save(self, user):
        pass

# True 0- different classes
class User2:

    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name

class UserDB:

    def get_user(self, id) -> User2:
        # Request to DB
        pass

    def save(self, user: User2):
        # Request to DB
        pass

"""
2. Open-Closed Principe
(Принцип открытости/Закрытости)

Программные сущности (классы, модули, функции) должны быть открыты для расширения, но не модификации
"""

# Wrong - need to extend method give_discount
class Discount1:

    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discount(self):
        if self.customer == 'fav':
            return self.price * 0.2
        if self.customer == 'vip':
            return self.price * 0.4

# True
class Discount2:

    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def get_discount(self):
        return self.price * 0.2

class VIPDiscount2(Discount2):

    def __init__(self, customer, price):
        super().__init__(customer, price)

    def get_discount(self):
        return super().get_discount() * 4


"""
3. Liskov Substitution Principe
(Принцип подстановки Лисков)

Главная идея, стоящая за этим принципом в том, что для любого класса клиент должен иметь возможность использовать любой
подкласс базового класса, не замечая разницы между ними, и следовательно, без каких-либо изменений программы.
Это означает, что клиент полностью изолирован и не подозревает об изменениях в иерархии классов.
"""

"""
4. Interface Segregation Principe
(Принцип разделения интерфейсов)

Создавайте тонкие интерфейсы, которые ориентированы на клиента. Клиенты не должны зависеть от интерфейсов,
которые они используют. Этот принцип устраняет недостатки реализации больших интерфейсов.
"""

#Wrong - Human, Cat
class Creature1:

    def __init__(self, age) -> None:
        self.age = age

    def run(self):
        pass

    def swim(self):
        pass

    def speak(self):
        pass

# True
class Creature2:

    def __init__(self, age) -> None:
        self.age = age

class RunInterface:
    def run(self):
        pass

class SwimInterface:
    def swim(self):
        pass

class SpeakInterface:
    def speak(self):
        pass

class Human(Creature2, RunInterface, SwimInterface, SpeakInterface):
    def __init__(self, age):
        super().__init__(age)


"""
5. Dependency Inversion Principle
(Принцип инверсии зависимостей)

Зависимость должна быть от абстракций, а не от конкретики.
Модули верхних уровней не должны зависеть от модулей нижних уровней.
Классы и верхних, и нижних уровней должны зависеть от одних и тех же абстракций.
Абстракции не должны зависеть от деталей. Детали должны завистеть от абстракций
"""

# Wrong
class ElkLogging1:
    def log(str):
        print(str)

class ConsoleLogging1:
    def log(str):
        print(str)

class Logger1:
    def __init__(self) -> None:
        self.elk_logging = ElkLogging1()
        self.console_logging = ConsoleLogging1()

    def elk_log(self, log):
        self.elk_logging.log(log)

    def console_log(self, log):
        self.console_logging.log(log)

# True
class ElkLogging2:
    def log(str):
        print(str)

class ConsoleLogging2:
    def log(str):
        print(str)

class Logger():

    def __init__(self, logging_wrapper) -> None:
        self.logging_wrapper = logging_wrapper

    def log(self, log):
        self.logging_wrapper().log(log)
