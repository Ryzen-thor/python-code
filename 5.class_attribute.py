"""
    Variable defined with self are instance variable and different instance will have their own instance value.

    And variable defined outside any method under class are class attribute and they will remain same for all instance and can be access through instacne.attribute or classname.attribute.

    If we consider below example when we access variable by test.x (instance) then python would first look for x under instance attribute list and if it finds it then it would print it (20 in this case). But suppose if there is no attrbitue named x under instacne attribute list then python would start looking for class attrbiute list and if it finds then it would print it (10).

    But if you directly access it theough classname then it would access the value of x from class atttrbiute list
"""

class Test:
    x=10 #class attribute

    def __init__(self):
        self.x=20 #instance attribute

test=Test()
print(test.x) # print 20
print(Test.x) # print 10


"""
    use of class attribute 
    1) Storing class constants: Defining constant which would be same accross all isntance. For example for Circle class pi constant should be same for all instance hence pi=3.14

    2) Tracking data accross of all instances: Like for example number of connections object. Refer below example class Connection. This way we can track like how many connection object we have 

    3) Default value: Same way as constant, suppose you have a product and you want to apply default discout value to all object then we can use class attrbitue like 

    class Product:
        default_discout=10  
"""

class Connection:
    connection_list=[]
    pi=3.14 # Just example

    def __init__(self, radius):
        self.radius=radius

        self.connection_list.append(self)

