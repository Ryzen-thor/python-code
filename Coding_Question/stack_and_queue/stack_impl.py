"""
    Stack works on LIFO (Last IN First Out) way meaning last data inserted will be removed first.

    Operations:
    arr=[5,6,7]

    push(append): Add data at last
    arr.append(10) -> arr=[5,6,710]

    pop: Remove the last data from list and return it.
    last_data = arr.pop() -> arr=[5,6,7] and last_data=10

    peek: Return the last data without removing it.
    last_data=arr.peek() -> arr=[5,6,7] (still same) but last_data=7

    isEmpty: Return True if there is no data else False.
    arr.isEmpty -> False 
"""

arr = [10,20,30]
arr.append(40)
print(arr)
data=arr.pop()
print(arr)
print(data)
data=arr[-1] #arr.peek()
print(data)
print(arr)

#arr.isEmpty()
if arr:
    print(False)
else:
    print(True)

print("--------------------------------------------------")

from typing import TypeVar, Optional, List, Generic

T = TypeVar("T")

class Stack(Generic[T]):

    def __init__(self, data: Optional[List[T]] = None):
        self.arr: List[T] = data if data else []

    def push(self, data: T) -> None:
        self.arr.append(data)

    def pop(self) -> Optional[T]:
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.arr.pop()

    def peek(self) -> Optional[T]:
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.arr[-1]
    
    def is_empty(self) -> bool:
        return len(self.arr) == 0
    
    def __str__(self) -> str:
        return f"Stack: {self.arr}"
    
stack=Stack([3,4,5])
print(stack)
stack.push(6)
print(stack)
stack.pop()
print(stack)

print(stack.peek())
print(stack.is_empty())