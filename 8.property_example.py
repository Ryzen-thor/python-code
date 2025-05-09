"""
    We can set or get attribute but sometime we need need some validation.
    For example, you have age attribute but you cannot set its value to -19 or 200 therefore we need some validation. 

    So we can provide some validation while setting the age attribute.

    But with convetional method way, there is backward compability issue. Meaning if someone already using the Person class and then we add these getter/setter method they cannot use it.

    TO have backward campability we can use @property
"""

class Person:

    def __init__(self, name, age):
        self.name=name 
        self.age=age

    @property
    def age(self):
        return self._age    

    @age.setter
    def age(self, value):
        if value <= 0:
            raise ValueError('The age must be positive')
        self._age=value

person1 = Person("Thor",1500)
print(person1.age)