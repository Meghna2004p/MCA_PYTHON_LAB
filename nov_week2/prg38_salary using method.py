class Employee:
    basic=0
    TA=0
    DA=0
    def salary(self):
        print("salary",self.basic+self.TA+self.DA)
emp1=Employee()
emp1.basic=20000
emp1.TA=500
emp1.DA=1000
emp1.salary()

emp2=Employee()
emp2.basic=50000
emp2.TA=500
emp2.DA=1000
emp2.salary()
