"""
    We know that a class is a blueprint of an object.
    Similarly we can have a blueprint of class which is know as abstract class.
    This abstract class can not be initianted, it gives you structure to follow so that any class which  inherits this abstract class have to follow those structure meaning if abstract class have an abstract method (which is only method signature and no implementation) then chile class have to follow those methods and provide their own implementation.
    
    Python does not support this directly, but it offers a module name abc (abstract base class) to achieve abstraction.
    And @abstractmethod decorator to have abstract method.
    
    Lets take example where we have to implement payroll functionality, there are two types of employee FullTimeEmployee and PartTimeEmployee. Now there is method getSalary which will return salaries of their type.
    So here we could have first define Employee class which is abstract then there will be abstractmethod getSalary.
    With this now any class which inherits the Employee class will have to implement their own getSalary method
"""

from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name):
        self.name=name

    @property
    def name_(self):
        return self.name
    
    @abstractmethod
    def getSalary(self):
        pass
    
class FullTimeEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary=salary
        
    def getSalary(self):
        return self.salary
    
class PartTimeEmployee(Employee):
    def __init__(self, name, worked_hours, rate):
        super().__init__(name)
        self.worked_hours=worked_hours
        self.rate=rate
        
    def getSalary(self):
        return self.worked_hours*self.rate
    
class Payroll:
    def __init__(self):
        self.employees_list=[]
        
    def add(self, employee):
        self.employees_list.append(employee)
        
    def print_(self):
        for e in self.employees_list:
            print(f"{e.name} with salary {e.getSalary()}")
            
payroll = Payroll()

fte=FullTimeEmployee("Thomas Andre", 60000)
pte=PartTimeEmployee("John Wick", 40*22, 100)

payroll.add(fte)
payroll.add(pte)

payroll.print_()

    

