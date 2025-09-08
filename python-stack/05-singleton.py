# Пример реализации синглтона на языке Python:

class Singleton(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            print(1)
            cls.obj = range(0, 10_000_000_000)
            cls.instance = super(
                Singleton, cls
            ).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        pass

    def foo(self):
        return "Singleton"

foo = Singleton() # 1
foo1 = Singleton()