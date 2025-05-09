"""
    We know that to use any method(function inside class) we have to create object from that class first.

    But what if we want a method which does not require instace and can be directly call using classname.

    And that method is call classmethod.

    Like instance method have self since they are bount to instace.
    Similarly, we have cls as parameter

    We use classmethod to create instance of class in different way (we will understand it with example). This returning of instance in various way is called factory method also.

    Remember classmethod can not access the instance attribute/variable they can only access class attribute while instace methods can access both.
"""

class Person:

    def __init__(self, name, age):
        self.name=name
        self.age=age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

    @classmethod
    def new_person(cls, name,age):
        return Person(name,age)
    
    @classmethod
    def new_person_from_csv(cls, detail):
        guy=detail.split(",")
        return Person(guy[0],guy[1])


person1=Person("Thor odinson",1500) # conventional way to create obj/instance
person1.introduce()

#creating instance through classmethod
person2=Person.new_person("Loki odinson",600)
person2.introduce()

#creating instance with various format
person3=Person.new_person_from_csv("Tony Stark, 56")
person3.introduce()