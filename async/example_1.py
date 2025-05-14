"""
    A coroutine is a function which has ability to paused its execution if if finds the operation is taking a while to complete.
    
    When the long running process is completed we can resume the paused coroutine and execute the remaining part of code.
    
    While coroutine is paused for long running process we can have our code run for other parts of code. This is call asynchronousprogram
    
    async - keyword creates the coroutine
    await - keyword pause the coroutine
"""

import asyncio
import time

async def square(number):
    return number*number

result=square(5) # Calling coroutine returns a coroutine object
print(result) 

"""
    To run this coroutine object we need to put these coroutine to event loop and then event loop executes them.
"""

result=asyncio.run(square(5)) # this asyncio.run would run coroutine on event loop

"""
    But we need await which pauses the coroutine and wait for the code to be completed and retunr the result.
    
    Point to be noted that await can only be inside the couroutine meaning functions with async
    
    Hence to make this work we need to create async main function
"""

async def main():
    
    x = await square(10)
    print(f"x={x}")
    
    y = await square(20)
    print(f"y={y}")
    
    print(f"Total={x+y}")
    
asyncio.run(main())

async def start_api(message,result=100, delay=3):
    print(message)
    await asyncio.sleep(delay)
    return result


# async def main():
#     start = time.perf_counter()
    
#     price = await start_api("Get stock price ...", 300)
#     print(price)
    
#     price = await start_api("Get stock price 2 ..",400)
#     print(price)
    
#     end = time.perf_counter()
    
#     print(f'It took {round(end-start,0)} second(s) to complete.')
    
# asyncio.run(main())

"""
    It is still running sync way.
    
    Task:
    It is a wrapper of a coroutine that schedules the coroutine to run on the event loop as soon as possible.
    
    Scheduling and execution happens in a non-blocking manner. In other words we can create the task and execute the other code instantly while task being running.
"""

async def main():
    start = time.perf_counter()
    
    task1 = asyncio.create_task(
        start_api("Stock price 1..", 1000)
    )
    
    task2 = asyncio.create_task(
        start_api("Stock price 2..", 4000)
    )
    
    price=await task1
    print(price)
    
    price=await task2
    print(price)
    
    end = time.perf_counter()
    print(f'It took {round(end-start,0)} second(s) to complete.')
    
asyncio.run(main())