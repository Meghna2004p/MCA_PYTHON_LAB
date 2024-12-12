class Employee:
    company_name="ABCD"
    location="calicut"
    def __init__(self,id,name,salary):
        self.emp_id=id
        self.emp_name=name
        self.emp_salary=salary
    def details(self):
        print(self.emp_id,self.emp_name,self.emp_salary)
emp1=Employee(1,"Nithin",20000)
emp2=Employee(2,"Anu",50000)
emp1.details()
emp2.details()
