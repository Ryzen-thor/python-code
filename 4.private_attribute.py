"""
    If you have class attrbitue/varaible or instance variable, 
    you can still access these varaible outside the class and modify it.
    In python we can use convention _ while defining the class or instance attribute, although you could still access it but its a convention so that other developers would know that it is a private attribute and something to use modify outside the class.
"""

class Smartphone:
    _category="Phone"
    def __init__(self, brand: str) -> None:
        self._brand = brand
    
    def print_detail(self):
        print(f"Smartphone brand is {self._brand}")


#you can still access these variable and modify its value
ph1 = Smartphone("Oneplus")
ph1.print_detail()
ph1._brand="Whatever"
ph1.print_detail()

print(Smartphone._category)
Smartphone._category="Random"
print(Smartphone._category)


"""
    Python has one more concept called Name mangling

    Here, we define varaible with double underscore __ and this way you can't access these variable like instance.__attribute or ClassName.__attribute
"""

class Table:
    __madeOf="Wood"

    def __init__(self, brand):
        self.__brand = brand

tb1=Table("IKEA")
# print(tb1.__brand)#AttributeError saying Table object has no attrbiute __band
# print(Table.__madeOf)#same error

"""
    However, we can still access the attribute like _class_attribute.
    This is because when we create any variable which start with __ python automatically change the name to _class_attribute style and this concept is called name mangling
"""

print(tb1._Table__brand) # This will print IKEA
print(Table._Table__madeOf)# same way this will print wood

"""
    Purpose of name mangling 
    It is mainly use to avoid name conflicts in subclass (during inheritance situation).
    It does not protect our variable it is more of a convention to signal that this attribute is intended for interal use within the class.

    In short, to avoid overiding the variable in subclass we use __attribute because outside the class you can't use __attribute since it would be replaced by _class__attrbitue and hence even if you use same attrbitue in subclass it won't be same. 
"""