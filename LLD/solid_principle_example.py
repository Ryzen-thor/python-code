"""
    Single Responsibilty Principle
    This principle states that a single class should have a single responsibilty to handle or single reason for a change. 
    Create high cohesive and robust class, methods and functions
    High cohesion mean thats elements are closely related and focused on a single purpose while low cohesive meaning elements are loosely related and serve multiple purpose.
    Promote class composition
    Avoid code duplication
    
    
"""
class Person:
    
    def __init__(self,name:str):
        self.name=name 
        #extra attributes
    
    def console_print(self):
        print(f"Hi, I'm {self.name}. How are you?")
        
    def save_db(self):
        print(f"Saving {self.name} in DB process")
        
"""
    We can see its breaking SRP princle because single class has responsibilty of managing the person attributes, printing them on console, saving them on DB etc.
    
    Now suppose we want to change the saiving person to db logic, then we need to change the Person class although its just different DB process.
"""

class Person:
    def __init__(self, name: str):
        self.name=name
    def __str__(self):
        return f"Person(name={self.name})"
        
class ConsolePersonPrinter:
    
    def print_(self, person: Person):
        print(f"Hi, I'm {person.name}. How are you?")

class PersonDB:
    
    def save(self, person):
        print(f'Save the {person} to the database')

printer = ConsolePersonPrinter()
printer.print_(Person("Aman"))

john = Person("John")
db=PersonDB()
db.save(john)

"""
    Open Closed Principle
    Open for extension but closed for modification
    Purpose is to make it easy to add new features(use case) in a system without directly modify the existing code.
     
"""

class Person:
    def __init__(self, name: str):
        self.name=name
    def __str__(self):
        return f"Person(name={self.name})"
    
class PersonStorage:
    def save_to_database(self, person):
        print(f"Save the {person} to database")
        
    def save_to_json(self, person):
        print(f"Save the {person} in json file")
        
"""
    Now here there is two way to save person (database and json file). But there is new use case (feature) where we want to save as xml format as well.
    Then we have to modify the PersonStorage class.
    This is violating the principle it is in fact open for modification.
    
    So the way to add new feature without chaging the existing class/codebase is to use interface/abstraction.
    We will ake PersonStorage class abstract and then create the concrete class for DB, json, xml etc.
"""
from abc import ABC, abstractmethod
class PersonStorage(ABC):
    
    @abstractmethod
    def save(self, person):
        pass
    
"""
Now we will implement concrete indivdual class
"""

class PersonDB(PersonStorage):
    def save(self, person):
        print(f'Save the {person} to database')
        
#There is new use case to save person in json

class PersonJSON(PersonStorage):
    def save(self,person):
        print(f'Save the {person} to json file')
        
person = Person("Tony Stark")
json_file = PersonJSON()
json_file.save(person)


"""
    LSP (Liskov Substitution Principle)
    It states that child class must be subsituable for its parent class. It aims to ensure that child class can assume the place of its parent without casuing any error.
    
    It is also kinda even though object is of child class but datatype can be of child or parent as well since child class is subsituable in parent class. 
"""

class Account(ABC):
    @abstractmethod
    def withdraw(self):
        pass
    @abstractmethod
    def deposit(self):
        pass
    
"""
Now Account is interface like a contract and it will be the parent class. Client will only know the interface that is Account and their methods.
"""
class CurrentAccount(Account):
    def withdraw(self):
        print("Withdrawing Money from Current")
    def deposit(self):
        print("Deposit Money in Current")
        
class SavingsAccount(Account):
    def withdraw(self):
        print("Withdrawing Money from Savings")
    def deposit(self):
        print("Deposit Money in Savings")
        
"""
Now client can have a Account type with object either current or saving and it can call withdraw and deposit
"""

account:Account = SavingsAccount() 
account.deposit() 

"""
    Now suppose there if new FixedDeposit Class. Since FixedDeposit shoulld not have withdraw function, but by inheriting the interface it has to deposit as well. We can do one thing we can raise the exception.
    
"""

class FixedDeposit(Account):
    def deposit(self):
        print("FD for 1 year")
        
    def withdraw(self):
        raise "Can't withdraw money since its FD"
        
fdaccount: Account= FixedDeposit()
# fdaccount.withdraw()

"""
Although this works but its bad desgin why? Because client (who is creating the object) has to handle this exception. Client only knows the interface and from that it would assume for any object there will be two methods deposit and withdraw. So when client calls the withdraw on FD then it would get exception which client doesn't know. 

Also this violates the LSP principle because Parent class is not replaceable with child class. Parent is Account and child is FixedDeposit and with FD object we can not have Account as Type.

One more example:
Consider a Bird class with a fly() method and a Penguin class inheriting from it. If the Penguin class overrides fly() to throw an exception (because penguins don't fly), it violates LSP. You can't reliably substitute a Penguin for a Bird in code that expects flying behavior without breaking the program. 

Now question is how to solve it?
Answer is to have sperate interface.
Lets create two interface
1) NonWithdrawableAccount
2) WithdrawableAccount
"""

class NonWithdrawableAccount(ABC):
    @abstractmethod
    def deposit(self):
        pass

class WithdrawableAccount(NonWithdrawableAccount):
    @abstractmethod
    def withdraw(self):
        pass
        
class SA(WithdrawableAccount):
    def withdraw(self):
        print("Can withdraw from Savings Account..")
    def deposit(self):
        print("Can deposit from Savings Account...")
        
class CA(WithdrawableAccount):
    def withdraw(self):
        print("Can withdraw from CurrentAccount..")
    def deposit(self):
        print("Can deposit from CurrentAccount...")
        
class FD(NonWithdrawableAccount):
    def deposit(self):
        print("Can deposit in FD...")
        
class Main():
    #Client
    sa: WithdrawableAccount=SA()
    sa.deposit()
    sa.withdraw()
    
    fd:NonWithdrawableAccount=FD()
    fd.deposit()