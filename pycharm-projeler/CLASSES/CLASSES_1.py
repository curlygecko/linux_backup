class Employee:

    raise_amount = 1.04

    def __init__(self,first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+"."+last+"@gmail.com"

    def fullname(self):
        return "{} {} {}".format(self.first, self.last, self.pay)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount )



emp_1 = Employee("dogukan", "kutlu", 50000)
emp_2 = Employee("batıkan", "kutlu", 60000)


print(emp_1.raise_amount)
print(Employee.raise_amount)


