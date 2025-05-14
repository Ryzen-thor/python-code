"""
    It is a function that takes another function as argument and extends its behaviour without changing the original function explicitly.

    So decorator takes function as argument and return function as well.
"""


#This function return the price after tax
def net_price(price, tax):
    return price * (1+tax)

"""
    But suppose we want say $ symbol as well or different symbol based on location without altering existing functions. We can use decorator. 
"""
# def currency(fn):
#     def wrapper(*args, **kwargs):
#         #can do some pre-fn processing
#         fn(*args, **kwargs) #calling the fn passed as parameter in function
#         #post-fn execution processing
#     return wrapper

def currency(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        return f"${result}"
    return wrapper

# Essentially we are decorating the price function with currency decorator
price=currency(net_price) 
# Now since the price is function itself which is wrapper function we can pass any argument, and this argument will be available to original function and then we can execute the fn(*args, **kwargs). Store the result (net_price) and return modfied value without changing anything of original function net_price
print(price(100,0.05))

"""
    So we know that currency(net_price) this is decorator now there shorcut as well
    we can add as @currency before the net_price function definition.

    Now if you do help(price) we will see that its a wrapper function.
    Also, with price.__name__ it would return wrapper.
    So, we lost original function signature and documentation.
    To fix this we can use wraps functon from functools library.
"""
print(help(price))
from functools import wraps
def greeting(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print("----- Hello From Wrapper", end=" ")
        name = fn(*args, **kwargs)
        return name
    return wrapper

@greeting
def print_name(name):
    """ Function which accepts name and return name"""
    return name

print(print_name("Aman"))
print(help(print_name))
print(print_name.__name__)

# ------------- Decorator with arguments
"""
    The new repeat function returns a decorator. And it's often referred to as a decorator factory.
"""
def reapeat(times):
    def decorate(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = fn(*args, **kwargs)
            return result
        return wrapper
    return decorate

@reapeat(10)
def print_name(name):
    print(name)

print_name("Thor")


"""
    The start() decorator factory takes an argument and returns a callable(decorate). The callable takes fn as argument and has also access to n due to closure.

    Now we can have a class decorator as well we just have to override the __call__ method to make class decorator.
"""
def star(n):
    def decorate(fn):
        def wrapper(*args, **kwargs):
            print(n*"*")
            result = fn(*args, **kwargs)
            print(result)
            print(n*"*")
            return result
        return wrapper
    return decorate

@star(5)
def add(a,b):
    return a+b

add(10,20)

class Star:

    def __init__(self, n):
        self.n=n

    def __call__(self, fn):
        def wrapper(*args, **kwargs):
            print(self.n*"*")
            result = fn(*args, **kwargs)
            print(result)
            print(self.n*"*")
            return result
        return wrapper
    
@star(5)
def add(a,b):
    return a+b

add(3,5)

