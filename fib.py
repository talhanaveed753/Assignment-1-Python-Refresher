#fib.py

import functools
import time
from functools import lru_cache
import matplotlib.pyplot as plt

# Create a global variable to hold the time data
allTimes = []

def timer(func):
    """Time each fib calculation"""

    @functools.wraps(func)
    def wrapperTimer(*args, **kwargs):

        # Declare allTimes as global var
        global allTimes

        # Run a timer for each fib calculation
        start = time.perf_counter()
        value = func(*args, **kwargs)
        end = time.perf_counter()

        # Calculate and store the time values
        elapsedTime = end - start
        allTimes.append(elapsedTime)

        # Output required data
        print(f"Finished in {elapsedTime:0.8f}s: f({args[0]}) -> ", value)

        return value

    return wrapperTimer

@lru_cache
@timer
def fib(n: int) -> int:
    """Calculate fibonacci"""

    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

def graphData():
    """Graph results"""

    # Create list for x axis representing the nth fib number
    x = [i for i in range(0, 101)]

    # Plot and display the graphed data
    plt.plot(x, allTimes)
    plt.title("Time to Calculate nth Fibonacci")    # Title of the graph
    plt.xlabel("nth Fibonacci number")              # X-axis label
    plt.ylabel("Time to Calculate (seconds)")       # Y-axis label
    plt.show()                                      # Display the plot

if __name__ == "__main__":
    fib(100)    # Call to fib will calculate the desired values until nth value
    graphData() # Create a graph to represent data