"""
    Queue works on FIFO (First IN First Out) way meaning first data inserted will be removed first.

    Operations:
    arr=[5,6,7]

    Enqueue(append): Add data at last
    arr.append(10) -> arr=[5,6,7,10]

    Dequeue: Remove the first data from list and return it.
    first_data = arr.popleft() -> arr=[6,7,10] and last_data=5

    getFront: Return the first data without removing it.
    first_data=arr.getFront() -> arr=[6,7,10] (still same) but first_data=6

    getRear: Return the last data without removing it.
    last_data=arr.getRear() -> arr=[6,7,10] (still same) but last_data=10

    isEmpty: Return True if there is no data else False.
    arr.isEmpty -> False 
"""

from collections import deque

q=deque([10,20,30])
print(q)

q.append(40)
print(q)
print(q.popleft())
print(q)