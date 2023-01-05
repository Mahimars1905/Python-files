class Programmer:
    def __init__(self, name, age, salary):
        self.emp_name = name
        self.emp_age = age
        self.emp_salary = salary
        
    def prodetails(self):
        print(f"The name is {self.emp_name}, age is {self.emp_age} and salary is {self.Semp_salary}")


class Developer:
    def __init__(self, name, age, salary):
        self.emp_name = name
        self.emp_age = age
        self.emp_salary = salary
        
    def devdetails(self):
        print(f"The name is {self.emp_name}, age is {self.emp_age} and salary is {self.emp_salary}")

class Employee(Programmer, Developer):
    def empdetails(self):
        print(f"The name is {self.emp_name}, age is {self.emp_age} and salary is {self.emp_salary}")

pro = Programmer("Alok", 34, 34000)
dev = Developer("Rahul", 32, 32000)
emp = Employee("Ajay", 33, 33000)

# emp.devdetails()
# emp.prodetails()

pro.prodetails()
dev.devdetails()
