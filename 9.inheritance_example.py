"""
    It is one of the fundamental concept of OOP, where if we have two or more class with same attrbitue/method we can resue them instead of rewriting it again.


"""

class Person:
    def __init__(self, name):
        self.name=name

    def greet(self):
        return f"Hi, it's {self.name}"
    
class Employee(Person):
    def __init__(self, name, job_title):
        super().__init__(name)
        self.job_title=job_title


# Here since Employee class is subclass/child class of Person class it automatically inherits the greet method

emp1=Employee("Mark", "Software Engineer")
print(emp1.greet())

#you can test if it is a subclass of Parent
print(issubclass(Employee,Person))

#also you can check if emp1 object is an instance of both Employee and Person class
print(isinstance(emp1, Employee)) #True
print(isinstance(emp1,Person)) #True

person1=Person("Thomas")
print(isinstance(person1, Employee)) #False
print(isinstance(person1, Person))#True

#ca ncheck the type 
print(type(emp1)) #Employee class
print(type(person1)) #Person class


"""
    Multiple inheritance, you can inherit as many class as you want.
    And there is a concept of MRO (Method Resolution Operator), so if two class have same method and child class is referring both these class then which method to refer?
    It will use MRO concept, where it will first look for method in its own class then later as per the order of class inherit it would search and if it finds it then it will be stop and use that method.
    Ex: class C(A,B)
    Then we can see class C inherits A and B, since A is first it would look at A class later B if not found
"""

class A:

    def greet(self):
        print("Greet from class A")

class B:

    def greet(self):
        print("Greet from class B")

class C(A,B):
    pass

c=C()
c.greet()#Greet from class A


#method orverloading and overriding
"""
    python does not support overloading, it is method overloading concept where we could have same function/method name but with different parameter.
    Example:-
    clas Calculation:
        def add(a:int, b:int):
            return a+b
        def add(a:int, b:int, c:int):
            return a+b+c

    But in python, it would not be able to differentiate because this is what call compile time polymorphism, and compiler differentiate those function based on function signature and since python is interpreted language.

    Python does support method overrriding.
    Here, we could have same method name but we can override in in child class.
    Meaning overriding is happens because of inheritance.
"""
class Employee:
    def __init__(self, name, base_pay):
        self.name=name
        self.base_pay=base_pay

    def salary(self):
        return self.base_pay

class FullTimeEmployee(Employee):
    def __init__(self, name, base_pay, bonus):
        super().__init__(name,base_pay) 
        self.bonus=bonus

    # This is an example of overriding since salary of full time employee is base pay and bonus also hence we can override the salary method
    def salary(self):
        return self.base_pay + self.bonus
    
# Normal employee (contract)
contract_emp = Employee("Thomas", 30000)
print(contract_emp.salary())

fulltime_emp = FullTimeEmployee("Peter", 30000, 20000)
print(fulltime_emp.salary())