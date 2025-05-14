"""
    Also called magic method or special method.
    It provide as operator overloading feature and custom class behaivour.
    
    Operator overloading means suppose we do a+b where both are int then it would do arthimetic operations and if both are str then it would concate these two varaible.
    So this + perform different operations based on data type. And this is called operator overloading.
    
    Will see about custom class behaivour through example.
"""

class A:
    def __init__(self):
        self.a=10
        self.some="Random word"
        
class B:
    def __init__(self):
        self.b=30
        self.other="blash blah"
        
    def __add__(self,other):
        return self.b+other.a
        
# What would happen if we do a+b where a is instance of A class and same way b
a=A()
b=B()
print(b+a) #TypeError: unsupported operand type(s) for +: 'A' and 'B'

