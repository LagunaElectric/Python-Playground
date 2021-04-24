# Bread Bank For Dash
from datetime import date
import uuid
import random


class Account:
    def __init__(self, person, bread_stack):
        self.client = person
        self.bread_stack = {bread_stack.TYPE: bread_stack.amount}
        self.id = uuid.uuid4()
        self.creation_date = date.today()

    def stack_bread(self, bread_stack):
        type = bread_stack.TYPE
        amount = bread_stack.amount
        self.bread_stack[type] += amount

    def __str__(self):
        out = ""
        out += f"Client: \n{self.client.__str__()}\n"
        out += f"Bread Stacks: \n{str(self.bread_stack)}\n"
        out += f"Hex ID: {self.id.hex}\n"
        out += f"Creation Date: {self.creation_date}"
        return out


class Person:
    def __init__(self, first_name="", last_name="", birth_date=date.today()):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.id = uuid.uuid4()

    def __str__(self):
        out = ""
        out += f"First Name: {self.first_name}\n"
        out += f"Last Name: {self.last_name}\n"
        out += f"Birthday: {self.birth_date}\n"
        out += f"Hex ID: {self.id.hex}"
        return out


class Employee(Person):
    def __init__(self, first_name, last_name, birth_date, salary):
        super().__init__(first_name, last_name, birth_date)
        self.salary = salary
        self.email = None
        self.phone_number = None


class Manager(Employee):
    def __init__(self, first_name="", last_name="", birth_date=date.today(), salary=0):
        super().__init__(first_name, last_name, birth_date, salary)
        self.access_code = None


class Bread():
    def __init__(self, type):
        self.TYPE = type


class BreadStack(Bread):
    def __init__(self, type, amount=0):
        super().__init__(type)
        self.amount = amount


class BreadVault:
    def __init__(self):
        self.balance = []


class BreadBank:
    def __init__(self, manager=Manager(), employee_list=[], accounts=[], vault=BreadVault()):
        self.manager = manager
        self.employees = employee_list
        self.accounts = accounts
        self.vault = vault

    def deposit(self, account, bread_stack=BreadStack("", 0)):
        self.accounts.find(account.id).stack_bread(bread_stack)


if __name__ == "__main__":
    bread_amt = random.randrange(25, 450)
    salary = 50000
    employees = [Employee("", "", date.today(), salary)] * 10
    accounts = [Account(Person(), BreadStack("Brioche", bread_amt))]*10
    bank = BreadBank(Manager(), employees, accounts, BreadVault())
    print(str(bank.employees))
    print(str(bank.accounts[0]))
