
class Employee:
    '所有员工基类'
    empCount = 0

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ",self.name,",Salary:",self.salary)

"创建对象"
emp1 = Employee("Zara",2000)
emp2 = Employee("Eric", 6000)
emp3 = Employee("Math",25000)

emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()

emp3.displayCount()