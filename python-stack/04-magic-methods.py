# Пример использования метода call

class Foo:
    def __call__(self, a):
        print("__call__", a)

foo = Foo()
foo(5) # __call__ 5

# Пример использования метода __setattr__
class Foo1:
    Age = None
    Salary = 0

    def __setattr__(self, name, value):
        print(f"{name=}", f"{value=}")
        if name == 'Salary':
            self.__dict__['Motivation'] = value * 0.5
            self.__dict__[name] = value

foo1 = Foo1()
foo1.Salary = 1000
print(foo1.Salary)      # 1000
print(foo1.Motivation)  # 500

# Пример использования метода __enter__
class Foo2:
    Age = None
    Salary = 0

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        return self.name

    # Пришлось добавить такой метод, погуглив
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting the context...")
        # Cleanup or release self.resource here

with Foo2(name = "Asd") as f:
    print(f)