class Employee:
    def __init__(self,name,salary):
        self.name=name
        self._salary=salary
    def show(self):
        print("Name is",self.name,"and salary is",self._salary)
emp=Employee("Jessa",40000)
emp.show()
print(emp.name)
