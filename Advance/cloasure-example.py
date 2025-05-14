"""
    Function in python are first class function meaning we can use function inside the function, pass function as parameter to function, assign function to a variable etc
"""

# def func1():
    
#     def func2():
#         return 2
#     return func2

# x=func1()
# print(x)
# print(x())


"""
    Outer function body executes the inner function.
    
    It(inner) can access the message because it is close to its scope and it is call nonlocal scope. 
"""
# def outer():
    
#     # ---------------
#     # This is closure
#     # By definition, a closure is a nested function that references one or more variables from its enclosing scope.
#     message="Outer message"
    
#     def inner():
#         print(message)
#     # ---------------
    
#     inner()
# outer()

# def outer():
#     message="Outer message"
#     def inner():
#         # nonlocal message
#         message="Inner Message"
#         print(message)
#     inner()
    
# outer()


"""
    Here below, outer function executes and return a function(inner). When fn function executes, the outer is already executed before
    
    Meaning, the scope of outer is gone because we have executed it (fn=outer()). 
    Now message belongs to the scope of outer function, so it should be destroyed with the scope of outer function.
    
    However, still fn printed the message and this is called closure.
"""
def outer():
    
    message="Hello from closure"
    def inner():
        print(message)

    return inner

fn=outer()
fn()