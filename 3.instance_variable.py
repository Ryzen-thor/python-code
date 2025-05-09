"""
    class variable is associated with class and same way instance variable is aasociated with specific instance. 

    We know from class variable that when we have class attribute it is added on classname.__dict__ and since that is dictionary we can access those variable with classname.variablename and it will start looking for that variable under __dict__

    Now when we create new instance say
    home = HTMLdocument()

    Now home is instance of class HTMLDocument

    And home instance has its own __dict__ 
"""

from pprint import pprint


class Laptop:
    category= "Gaming Laptop"

    def __init__(self, brand: str, model: str):
        self.brand=brand #instance variables 
        self.model=model

# temp_lap=Laptop() # laptop instance without any instance variable will have empty dict {}
# pprint(temp_lap.__dict__)

lap1 = Laptop("Lenovo", "LOQ")
pprint(lap1.__dict__) # {'brand': 'Lenovo', 'model': 'LOQ'}

print(lap1.category) #Now here instance lap1 would first look for category variable inside the instance __dict__ when it won't find it then it would look inside the class __dict__

