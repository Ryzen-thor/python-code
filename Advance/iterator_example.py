"""
    An iterator is object which implements:

    __iter__: method which return objects itself.
    __next__: method that returns next item. If all item have been returned, then method rasies StopIteration exception.


    These two methods are know as Iterator Protocol

"""

class Square:

    def __init__(self, length):
        self.length=length
        self.current=0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current>=self.length:
            raise StopIteration
        
        self.current+=1
        return self.current ** 2
    
square = Square(5)
for sq in square:
    print(sq)


"""
    An iterable is an object that we can iterate over.
    An object is iterable when it implements the __iter__ method. And its iter method should return new iterator
"""

numbers = [1,2,3]
print(numbers.__iter__) # prints list_iterator
#to get iterator object we can use iter()
number_iterator=iter(numbers)
#Since its iterator we can have __next__ implemented
print(next(number_iterator))
print(next(number_iterator))


class Color:

    def __init__(self):
        self.rgb= ["red","green","blue"]
        self.__index=0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__index >= len(self.rgb):
            raise StopIteration
        
        color = self.rgb[self.__index]
        self.__index+=1
        return color
    
color = Color()

for col in color:
    print(col)

"""
    Now if we do next(color) we will get StopIteration exception since iterator is exhausted. We need to create new color object again
"""
# print(next(color))
color=Color()
for col in color:
    print(col)

"""

    First lets seperate Color class and Color Iterator using ColorIterator class.
"""

class Color:
    def __init__(self):
        self.rgb=["red","green","blue"]

    def __len__(self):
        return len(self.rgb)
    
    def __iter__(self):
        return self.ColorIterator(self)
    
    class ColorIterator:

        def __init__(self, color):
            self.__index=0
            self.__colors=color

        def __iter__(self):
            return self
        
        def __next__(self):
            if self.__index >= len(self.__colors):
                raise StopIteration
            
            color=self.__colors.rgb[self.__index]
            self.__index+=1
            return color

color = Color()
for col in color:
    print(col)