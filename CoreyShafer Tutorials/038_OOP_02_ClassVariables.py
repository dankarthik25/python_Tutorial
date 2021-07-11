# Class Variable are        : var that are shared among the object's(Instance's) or class

# Instance Variables are    : unique for each  Instance or object


class Employee:

    raise_amount = 1.04  # class variable
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)
        # self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

# Actually emp_1 does't have raise_amount but it will check in Employee class and then it will create raise_amount(attributes)
print('Class Employee: attributes and methods:\n', Employee.__dict__)
print('object emp1: attributes and methods:\n', emp_1.__dict__)     # it does't have any raise_amount(attributes)

emp_1.raise_amount = 1.05

print('object emp1: attributes and methods:\n', emp_1.__dict__)
print('Class Employee: attributes and methods:\n', Employee.__dict__)   # create the attributes

print(Employee.raise_amount)        # >>> 1.04
print(emp_1.raise_amount)           # >>> 1.05
print(emp_2.raise_amount)           # >>> 1.04


#
print(Employee.num_of_emps)
