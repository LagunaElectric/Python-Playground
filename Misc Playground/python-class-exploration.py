# Python Class Exploration

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@testcompany.com"

    def __str__(self):
        nl = '\n'
        str_out = f"First Name: {self.first}\n" \
            f"Last Name: {self.last}\n" \
            f"Email: {self.email}\n" \
            f"Pay: ${self.pay / 1000}k/yr\n"

        return str_out


emp_1 = Employee("Ronald", "Headrick", 50000)

print()
print()
print()
print(emp_1.__str__())
