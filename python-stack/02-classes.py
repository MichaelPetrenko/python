from abc import ABC, abstractmethod

class Employee(ABC):

    def __init__(self, age, name, salary) -> None:
        self.age = age
        self.name = name
        self.salary = salary

    def set_salary(self, salary):
        self.salary = salary

    @abstractmethod
    def training(self):
        raise NotImplementedError('Method not implemented')

# employee = Employee(30, 'Vladislav', 100000);

class Accountant(Employee):

    def __init__(self, age, name, salary) -> None:
        super().__init__(age, name, salary)
        self.audit = False

    def set_audit(self, is_audit):
        self.audit = is_audit

    def conducts_audit(self):
        return self.audit

    def training(self):
        print("training...")